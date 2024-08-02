from aiogram.enums import ContentType
from aiogram_dialog import Dialog, DialogManager, Window
from aiogram_dialog.api.entities import MediaAttachment
from aiogram_dialog.widgets.media import DynamicMedia
from aiogram_dialog.widgets.text import Format
from aiogram.types import User

from database import add_card, get_random_card, get_user
from states import MainSG
from utils import rarity_to_data


async def hello_getter(dialog_manager: DialogManager, event_from_user: User, **kwargs):
    user_name = event_from_user.username if event_from_user.username is not None \
        else event_from_user.first_name
    return {"name": user_name}


async def card_getter(dialog_manager: DialogManager, event_from_user: User, **kwargs):
    card = await get_random_card()
    await add_card(telegram_id=event_from_user.id, card=card)
    user = await get_user(event_from_user.id)
    rarity_data = await rarity_to_data(card.rarity)
    image = MediaAttachment(ContentType.PHOTO, url=card.image)
    return {"card_name": card.name, "rarity": rarity_data["rarity"], "points": rarity_data["points"],
            "image":  image, "all_points": user.point_count}


async def profile_getter(dialog_manager: DialogManager, event_from_user: User, **kwargs):
    user = await get_user(event_from_user.id)
    username = event_from_user.username if not None else event_from_user.first_name
    is_banned = "Да" if user.is_banned else "Нет"
    status = "Админ" if user.is_admin else "Пользователь"
    return {"point_count": user.point_count, "user_id": user.id, "status": status,
            "is_banned": is_banned, "username": username, }


main_dialog = Dialog(
    Window(
        Format('Привет, {name}!\nНапишите "Луна" для получения карточки '),
        state=MainSG.start,
        getter=hello_getter
    ),
    Window(
        DynamicMedia("image"),
        Format('Вы нашли {card_name}! \nРедкость: {rarity} \nОчки: {points}\nВсего очков: {all_points}'),
        state=MainSG.get_card,
        getter=card_getter,
    ),
    Window(
        Format("Имя: {username}\nСтатус: {status}\n Забанен: {is_banned}\nКоличество очков: {point_count}"),
        getter=profile_getter,
        state=MainSG.profile,
    )
)

# Короче по-хорошему надо сделать рассылку очередью.
# Мне лень ничего по этому проекту делать наверное не буду.
