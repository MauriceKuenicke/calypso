import random
import string
import time
from typing import Awaitable, Callable

import calypso.modules.logger as logger
from fastapi import Request, Response


def _path_is_blacklisted(path: str):
    blacklist = ["_nuxt", "openapi.json", "favicon.ico"]
    return any(sub_string in path for sub_string in blacklist)


async def log_requests_middleware(
    request: Request, call_next: Callable[[Request], Awaitable[Response]]
) -> Response:
    """Middleware function that logs requests and responses.

    Args:
        request (fastapi.Request): The incoming request object.
        call_next (Callable): A callable that takes the request object
        and returns a response object.

    Returns:
        fastapi.Response: The outgoing response object.

    Example:
        >>> app.middleware("http")(log_requests_middleware)

    """
    # Generate request ID and append it to the header information
    idem = "".join(random.choices(string.ascii_uppercase + string.digits, k=10))
    request.headers.__dict__["_list"].append(
        (
            "request-ident".encode(),
            f"{idem}".encode(),
        )
    )

    start_time = time.time()
    response = await call_next(request)
    process_time = (time.time() - start_time) * 1000
    formatted_process_time = "{0:.2f}".format(process_time)

    if not _path_is_blacklisted(request.url.path):
        logger.CalypsoLogger.write_to_request_log(
            request_type=request.method,
            response_time_ms=float(formatted_process_time),
            status_code=response.status_code,
            request_identifier=idem,
            path=request.url.path,
        )

    return response
