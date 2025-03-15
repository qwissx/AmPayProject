from pydantic import Field
from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    db_name: str = Field(..., env="DB_NAME")
    db_user: str = Field(..., env="DB_USER")
    db_port: str = Field(..., env="DB_PORT")
    db_host: str = Field(..., env="DB_HOST")
    db_pass: str = Field(..., env="DB_PASS")

    redis_host: str = Field(..., env="REDIS_HOST")
    redis_port: str = Field(..., env="REDIS_PORT")

    secret: str = Field(..., env="SECRET")
    hash: str = Field(..., env="HASH")

    sign_key: str = Field(..., env="IAJaZGQgV6RS")
    partner_api_key: str = Field(..., env="PARTNER_API_KEY")

    class Config:
        env_file = ".env"

    @property
    def db_url(self):
        return f"postgresql+asyncpg://{self.db_user}:{self.db_pass}@{self.db_host}:{self.db_port}/{self.db_name}"


settings = Settings()
