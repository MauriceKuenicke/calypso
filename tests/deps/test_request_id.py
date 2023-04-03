from calypso import deps
from fastapi import Request


def test_extract_request_id_successfull() -> None:
    """Test successfull id extraction."""
    test_id = "12345"
    header_key = "request-ident"

    request_object = Request(
        scope={
            "type": "http",
            "headers": [(header_key.encode(), test_id.encode())],
        }
    )

    assert deps.extract_request_id(request=request_object) == test_id
