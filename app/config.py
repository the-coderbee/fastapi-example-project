from pydantic import BaseSettings
from dotenv import load_dotenv

load_dotenv()


class Settings(BaseSettings):
    database_hostname: str
    database_port: str
    database_name: str
    database_user: str
    database_password: str
    secret_key: str
    algorithm: str
    access_token_expire_minutes: int

    class Config:
        env_file = '../.env'


settings = Settings()
