from fastapi import Request


def request_id(request: Request) -> str:
    """Extract the request identifier from the header information.

    Args:
        request (fastapi.Request): The incoming request object.

    Returns:
        str: Request identifier string.

    """
    return request.headers.get("request-ident", "XXXXXXXXXX")
