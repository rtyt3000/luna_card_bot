from aiogram.filters import BaseFilter
from aiogram.types import Message
from database import get_user


class IsAdminFilter(BaseFilter):
    def __init__(self): pass

    async def __call__(self, message: Message) -> bool:  # [3]
        user = await get_user(message.from_user.id)
        if user.is_admin:
            return True
        else:
            return False
