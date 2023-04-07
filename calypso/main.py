from fastapi import FastAPI, Depends
from .middleware import log_requests_middleware
from calypso.modules.logger import CalypsoLogger
from calypso import deps

app = FastAPI()
app.middleware("http")(log_requests_middleware)


@app.get("/")
def read_root(rid: str = Depends(deps.extract_request_id)) -> dict[str, str]:
    """Test Endpoint."""
    CalypsoLogger.debug("Hello World!", extra={"idem": rid, "mod": __name__})
    return {"Hello": "World"}
