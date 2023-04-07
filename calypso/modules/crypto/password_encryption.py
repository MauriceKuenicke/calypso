import bcrypt

ENCODING = "UTF-8"


def encrypt_password(password: str) -> str:
    """Encrypt the password with a randomly generated salt.

    Args:
        password (str): Password which should be encrypted

    Returns:
        str: Generated hash value of the input

    """
    password_encoded = password.encode(ENCODING)
    hashed = bcrypt.hashpw(password_encoded, bcrypt.gensalt())
    return hashed.decode(ENCODING)


def authenticate_password(password: str, hash: str) -> bool:
    """Validate whether the input password matches the encrypted hash value.

    Args:
        password (str): Incoming password that will be validated
        hash (str): Encrypted hash value to validate the password against

    Returns:
        bool: Result of the authentication. `True` if
        password is valid. Otherweise `False`.

    """
    password_encoded = password.encode(ENCODING)
    hash_encoded = hash.encode(ENCODING)
    return bcrypt.checkpw(password_encoded, hash_encoded)
