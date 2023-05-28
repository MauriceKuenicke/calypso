import uuid


def gen_uuid_string() -> str:
    """Generate the string representation of a UUID.

    Returns:
        string

    """
    return str(uuid.uuid4())
