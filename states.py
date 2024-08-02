from aiogram.fsm.state import StatesGroup, State


class MainSG(StatesGroup):
    start = State()
    profile = State()
    get_card = State()


class GetCardSG(StatesGroup):
    start = State()
