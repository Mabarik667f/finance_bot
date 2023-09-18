from pydantic import BaseSettings, SecretStr


class Settings(BaseSettings):
    bot_token: SecretStr
    host: str
    user: SecretStr
    password: SecretStr
    db_name: SecretStr

    class Config:
        env_file = '.env'
        env_file_encode = 'utf-8'


cfg = Settings()