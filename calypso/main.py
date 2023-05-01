from calypso import deps
from calypso.db.session import SessionLocal
from calypso.models import User
from calypso.modules.logger import CalypsoLogger
from calypso.startup import add_root_user_if_not_exist, get_root_user
from fastapi import Depends, FastAPI
from fastapi.responses import JSONResponse

from .middleware import log_requests_middleware
from starlette.responses import FileResponse
from starlette.staticfiles import StaticFiles
import os
from os import path

DEFAULT_STATIC_DIR = os.path.join(
    os.path.abspath(os.path.dirname(__file__)), os.path.join("static", "calypso", "dist")
)

app = FastAPI()
app.middleware("http")(log_requests_middleware)

frontend = FastAPI(openapi_url="")
@frontend.middleware("http")
async def default_page(request, call_next):
    response = await call_next(request)
    if response.status_code == 404:
        if DEFAULT_STATIC_DIR:
            return FileResponse(path.join(DEFAULT_STATIC_DIR, "index.html"))
    return response

@app.on_event("startup")
def initialize_root_user() -> None:
    """Create the initial root user inside the database if it doesn't exist already."""
    root_user: User = get_root_user()
    with SessionLocal() as db:
        add_root_user_if_not_exist(db, root_user)


@app.get("/healthcheck", include_in_schema=False)
def read_root(rid: str = Depends(deps.extract_request_id)) -> JSONResponse:
    """Healthcheck Endpoint."""
    CalypsoLogger.info("Healthcheck received.", extra={"idem": rid, "mod": __name__})
    return JSONResponse(
        content={"status": "available"},
        headers={"cache-control": "no-cache"},
        status_code=200,
    )

# we mount the frontend and app
if DEFAULT_STATIC_DIR and path.isdir(DEFAULT_STATIC_DIR):
    frontend.mount("/", StaticFiles(directory=DEFAULT_STATIC_DIR), name="app")
app.mount("/", app=frontend)