import pytest
from pydantic import ValidationError

from auth_service.presentation.api.schemas.auth import RegisterUserRequest


def test_registration_schema_accepts_valid_data() -> None:
    request = RegisterUserRequest(
        email="buyer@example.com",
        password="secure-password-123",
    )

    assert str(request.email) == "buyer@example.com"
    assert request.password == "secure-password-123"


@pytest.mark.parametrize(
    ("email", "password"),
    [
        ("not-an-email", "secure-password-123"),
        ("buyer@example.com", "short"),
    ],
)
def test_registration_schema_rejects_invalid_data(
    email: str,
    password: str,
) -> None:
    with pytest.raises(ValidationError):
        RegisterUserRequest(
            email=email,
            password=password,
        )
