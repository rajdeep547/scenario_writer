from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    model_config = SettingsConfigDict(env_file=".env", env_file_encoding="utf-8")

    database_url: str = "postgresql://postgres:postgres@localhost:5432/scenario_writer"
    secret_key: str = "change-this-to-a-long-random-secret-key"
    algorithm: str = "HS256"
    access_token_expire_minutes: int = 60
    groq_api_key: str = ""
    debug: bool = True
    cors_origins: str = "http://localhost:5173,http://localhost:3000"

    @property
    def cors_origin_list(self) -> list[str]:
        return [origin.strip() for origin in self.cors_origins.split(",") if origin.strip()]


settings = Settings()
