from aiogram import Router
from aiogram.filters import Command, CommandObject
from aiogram.types import Message
from aiogram_dialog import DialogManager

from database.user import ban_user, unban_user
from filters import IsAdminFilter

ban_router = Router()


@ban_router.message(IsAdminFilter(), Command("ban"))
async def ban_command(message: Message, dialog_manager: DialogManager, command: CommandObject):
    if message.reply_to_message.from_user.id is not None and not message.reply_to_message.from_user.is_bot:
        user_to_ban = message.reply_to_message.from_user.id
    elif command.args[0] is not None:
        user_to_ban = int(command.args[0])
    else:
        await message.answer("А кого банить то?")
        return
    try:
        await ban_user(user_to_ban)
        await message.answer(f"{user_to_ban} забанен!")
    except ValueError:
        await message.answer("Это не айди, надо айди")
    except Exception:
        await message.answer("Не удалось забанить пользователя")


@ban_router.message(IsAdminFilter(), Command("unban"))
async def ban_command(message: Message, dialog_manager: DialogManager, command: CommandObject):
    if message.reply_to_message.from_user.id is not None and not message.reply_to_message.from_user.is_bot:
        user_to_ban = message.reply_to_message.from_user.id
    elif command.args[0] is not None:
        user_to_ban = int(command.args[0])
    else:
        await message.answer("А кого банить то?")
        return
    try:
        await unban_user(user_to_ban)
        await message.answer(f"{user_to_ban} разбанен!")
    except ValueError:
        await message.answer("Это не айди, надо айди")
    except Exception:
        await message.answer("Не удалось разбанить пользователя")
