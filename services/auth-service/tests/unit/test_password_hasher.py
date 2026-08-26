from auth_service.infrastructure.security.password_hasher import PasswordHasher


def test_hash_creates_verifiable_password_hash() -> None:
    password = "secure-password-123"
    hasher = PasswordHasher()

    hashed_password = hasher.hash(password)

    assert hashed_password != password
    assert hasher.verify(password, hashed_password)


def test_verify_returns_false_for_invalid_password() -> None:
    hasher = PasswordHasher()
    hashed_password = hasher.hash("secure-password-123")

    assert not hasher.verify("wrong-password", hashed_password)
