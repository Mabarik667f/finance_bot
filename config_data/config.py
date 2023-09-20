from dataclasses import dataclass
from environs import Env

@dataclass
class TgBot:
    token: str
    admin_ids: list[int]


@dataclass
class DataBaseConfig:
    db_name: str
    db_user: str
    db_host: str
    db_password: str


@dataclass
class Config:
    tg_bot: TgBot
    db: DataBaseConfig


def load_config(path: str = None) -> Config:
    env: Env = Env()
    env.read_env(path)

    cfg = Config(
        tg_bot=TgBot(
            token=env('BOT_TOKEN'),
            admin_ids=list(map(int, env.list('ADMIN_IDS')))
        ),
        db=DataBaseConfig(
            db_name=env('DB_NAME'),
            db_host=env('DB_HOST'),
            db_user=env('DB_USER'),
            db_password=env('DB_PASSWORD')
        )
    )

    return cfg
