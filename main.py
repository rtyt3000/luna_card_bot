import asyncio
import logging

from aiogram_dialog import setup_dialogs

from database import setup_db
from dialogs import ban_router, main_dialog
from loader import bot, dp
from middlewares import BannedMiddleware, RegisterMiddleware

logging.basicConfig(level=logging.INFO)


async def start():
    dp.message.middleware.register(RegisterMiddleware())
    dp.message.outer_middleware.register(BannedMiddleware())
    dp.include_routers(main_dialog, ban_router, dialog_starter)
    setup_dialogs(dp)
    await setup_db()
    await dp.start_polling(bot)


if __name__ == '__main__':
    asyncio.run(start())
