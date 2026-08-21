from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    model_config = SettingsConfigDict(
        env_prefix="AUTH_", env_file=".env", env_file_encoding="utf-8", extra="ignore"
    )

    app_name: str
    debug: bool
    database_url: str
    jwt_secret_key: str
    jwt_algorithm: str
    access_token_expire_minutes: int
    refresh_token_expire_days: int


settings = Settings()  # type: ignore[call-arg]
