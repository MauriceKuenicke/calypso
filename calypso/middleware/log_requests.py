from calypso.modules.logger import CalypsoLogger
from typing import Callable, Awaitable
from fastapi import Request, Response
import random
import string
import time


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

    CalypsoLogger.info(
        f"{request.method} Request at {request.url.path}",
        extra={"idem": idem, "mod": __name__},
    )

    start_time = time.time()
    response = await call_next(request)
    process_time = (time.time() - start_time) * 1000
    formatted_process_time = "{0:.2f}".format(process_time)

    CalypsoLogger.info(
        f"Completed in: {formatted_process_time}ms",
        extra={"idem": idem, "mod": __name__},
    )
    CalypsoLogger.info(
        f"Status Code: {response.status_code}", extra={"idem": idem, "mod": __name__}
    )

    return response
