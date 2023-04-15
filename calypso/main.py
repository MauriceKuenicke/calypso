from calypso import deps
from calypso.modules.logger import CalypsoLogger
from fastapi import Depends, FastAPI
from fastapi.responses import JSONResponse

from .middleware import log_requests_middleware

app = FastAPI()
app.middleware("http")(log_requests_middleware)


@app.get("/healthcheck", include_in_schema=False)
def read_root(rid: str = Depends(deps.extract_request_id)) -> JSONResponse:
    """Healthcheck Endpoint."""
    CalypsoLogger.info("Healthcheck received.", extra={"idem": rid, "mod": __name__})
    return JSONResponse(
        content={"status": "available"},
        headers={"cache-control": "no-cache"},
        status_code=200,
    )
