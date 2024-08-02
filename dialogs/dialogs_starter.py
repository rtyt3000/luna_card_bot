from aiogram import F, Router
from aiogram.filters import Command
from aiogram.types import Message
from aiogram_dialog import DialogManager, StartMode

from states import MainSG


dialog_starter = Router()


@dialog_starter.message(F.text.lower() == "луна")
async def get_card(message: Message, dialog_manager: DialogManager):
    await dialog_manager.start(MainSG.get_card, mode=StartMode.RESET_STACK)


@dialog_starter.message(Command("start"))
async def command_start(message: Message, dialog_manager: DialogManager):
    await dialog_manager.start(MainSG.start, mode=StartMode.RESET_STACK)


@dialog_starter.message(F.text.lower() == "профиль")
async def get_card(message: Message, dialog_manager: DialogManager):
    await dialog_manager.start(MainSG.profile, mode=StartMode.RESET_STACK)
