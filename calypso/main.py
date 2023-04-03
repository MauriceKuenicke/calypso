from fastapi import FastAPI, Depends
from .middlewares import log_requests_middleware
from calypso.modules.logger import CalypsoLogger
from calypso import deps

app = FastAPI()
app.middleware("http")(log_requests_middleware)


@app.get("/")
def read_root(rid: str = Depends(deps.extract_request_id)) -> dict[str, str]:
    """Test Endpoint."""
    CalypsoLogger.debug("Hello World!", extra={"idem": rid})
    return {"Hello": "World"}
