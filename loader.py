from aiogram import Bot, Dispatcher
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine, Engine
from aiogram.fsm.storage.redis import RedisStorage, DefaultKeyBuilder
from sqlalchemy.engine import URL
import redis

url = URL.create(
    drivername="postgresql",
    username="postgres",
    host="127.0.0.1",
    database="LunaCardsDB",
    password="QwerTY",
)
engine: Engine = create_engine(url)
Session = sessionmaker(autoflush=False, bind=engine, expire_on_commit=False)


storage = RedisStorage(redis.asyncio.Redis(),
                       DefaultKeyBuilder(with_destiny=True))

dp = Dispatcher(storage=storage)
bot = Bot(token="7006035031:AAGk0uBvIJsKoMUuU_hTKlqJ8gbyK7Sxkns",
          default=DefaultBotProperties(
              parse_mode=ParseMode.HTML
            )
          )
