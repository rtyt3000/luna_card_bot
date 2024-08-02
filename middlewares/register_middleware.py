from typing import Any, Awaitable, Callable, Dict
from aiogram import BaseMiddleware
from aiogram.types import Message

from database.user import create_user, get_user


class RegisterMiddleware(BaseMiddleware):
    def __init__(self) -> None: pass

    async def __call__(self, handler: Callable[[Message, Dict[str, Any]], Awaitable[Any]], event: Message,
                       data: Dict[str, Any]) -> Any:
        if await get_user(event.from_user.id) is None:
            await create_user(event.from_user.id)
        return await handler(event, data)
