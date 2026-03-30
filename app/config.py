from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    # --- Общие настройки ---
    DEBUG: bool = False
    SECRET_KEY: str

    # --- URLs ---
    BACKEND_URL: str

    model_config = SettingsConfigDict(
        env_file="../.env",
        env_file_encoding="utf-8",
        case_sensitive=True,
    )


settings = Settings()
