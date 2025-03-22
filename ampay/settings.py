from pydantic import Field
from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    prod: bool = Field(..., env="PROD")

    db_name: str = Field(..., env="DB_NAME")
    db_user: str = Field(..., env="DB_USER")
    db_port: str = Field(..., env="DB_PORT")
    db_host: str = Field(..., env="DB_HOST")
    db_pass: str = Field(..., env="DB_PASS")

    redis_host: str = Field(..., env="REDIS_HOST")
    redis_port: str = Field(..., env="REDIS_PORT")

    rabbitmq_host: str = Field(..., env="RABBITMQ_HOST")
    rabbitmq_port: str = Field(..., env="RABBITMQ_PORT")

    secret: str = Field(..., env="SECRET")
    hash: str = Field(..., env="HASH")

    partner_url_test: str = Field(..., env="PARTNER_URL_TEST")
    partner_url_prod: str = Field(..., env="PARTNER_URL_PROD")

    sign_key: str = Field(..., env="IAJaZGQgV6RS")
    partner_api_key: str = Field(..., env="PARTNER_API_KEY")

    webhook_url: str = Field(..., env="WEBHOOK_URL")

    class Config:
        env_file = ".env"

    @property
    def partner_url(self):
        if self.prod:
            return self.partner_url_prod
        return self.partner_url_test

    @property
    def rabbitmq_url(self):
        return f"pyamqp://{self.rabbitmq_host}:{self.rabbitmq_port}"

    @property
    def db_url(self):
        return f"postgresql+asyncpg://{self.db_user}:{self.db_pass}@{self.db_host}:{self.db_port}/{self.db_name}"


settings = Settings()
