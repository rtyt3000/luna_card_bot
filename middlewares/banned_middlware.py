from typing import Any, Awaitable, Callable, Dict
from aiogram import BaseMiddleware
from aiogram.types import Message
from database import get_user


class BannedMiddleware(BaseMiddleware):
    def __init__(self) -> None:
        pass

    async def __call__(self, handler: Callable[[Message, Dict[str, Any]], Awaitable[Any]], event: Message,
                       data: Dict[str, Any]) -> Any:
        user = await get_user(event.from_user.id)
        if user is not None:
            if not user.is_banned:
                return await handler(event, data)
