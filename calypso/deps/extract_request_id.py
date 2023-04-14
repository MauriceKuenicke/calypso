from fastapi import Request


def extract_request_id(request: Request, header_key: str = "request-ident") -> str:
    """Extract the request identifier from the header information.

    Args:
        request (fastapi.Request): The incoming request object.
        header_key (str): The key which stores the request id inside the header.
        Defaults to 'request-ident'.

    Returns:
        str: Request identifier string.

    """
    return request.headers.get(header_key, "XXXXXXXXXX")
