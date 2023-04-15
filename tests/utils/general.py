import random
import string


def random_bool() -> bool:
    """Return a random Boolean. True or False."""
    return random.choice([True, False])


def random_string(k: int = 8) -> str:
    """Return a random ascii letter string.

    Args:
        k (int): Number of characters to return.

    Returns:
        str

    """
    return "".join(random.choices(string.ascii_letters, k=k))


def random_string_digits(k: int = 8) -> str:
    """Return a random ascii letter string that can also contain digits.

    Args:
        k (int): Number of characters to return.

    Returns:
        str

    """
    return "".join(random.choices(string.ascii_letters + string.digits, k=k))
