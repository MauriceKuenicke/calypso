from typing import Awaitable, Callable

import pytest
from calypso.middleware import log_requests_middleware
from fastapi import Request
from fastapi.responses import JSONResponse


@pytest.fixture
def mock_callable() -> Callable[[Request], Awaitable[JSONResponse]]:
    """Return a callable testfunction."""

    async def test(request: Request) -> JSONResponse:
        assert "request-ident" in request.headers
        return JSONResponse(content="Test successfull.", status_code=200)

    return test


@pytest.mark.asyncio
async def test_log_requests_middleware(
    mock_callable: Callable[[Request], Awaitable[JSONResponse]]
) -> None:
    """Test if middleware adds the correct header identifier."""
    request = Request(
        scope={
            "type": "http",
            "headers": {},
            "method": "GET",
            "path": "/",
        }
    )
    await log_requests_middleware(request, mock_callable)
