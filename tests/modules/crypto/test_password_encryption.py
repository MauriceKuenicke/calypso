from calypso.modules import crypto


def test_successfull_password_authentication() -> None:
    """Test the successfull authentication of a password."""
    test_password: str = "MyTopSecretPassword123"
    hashed: str = crypto.encrypt_password(test_password)
    assert crypto.authenticate_password(test_password, hashed)


def test_unsuccessfull_password_authentication() -> None:
    """Test the unsuccessfull authentication of a password."""
    test_password: str = "MyTopSecretPassword123"
    hashed: str = crypto.encrypt_password(test_password)
    assert not crypto.authenticate_password("Will not match", hashed)
