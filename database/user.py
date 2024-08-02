from loader import Session
from models import User, Card


async def create_user(telegram_id: str) -> User:
    with Session() as db:
        user: User = User(telegram_id=telegram_id)
        db.add(user)
        db.commit()
        return user


async def get_user(telegram_id: str) -> User:
    with Session() as db:
        user: User = db.query(User).filter(User.telegram_id == telegram_id).first()
        return user


async def add_card(telegram_id: int, card: Card) -> User:
    with Session() as db:
        user: User = db.query(User).filter(User.telegram_id == telegram_id).first()
        if card.id not in user.cards:
            user.cards += [card.id]  # Ебаная дока SQLAlchemy, не работает без добавления массива в любом случае,
            db.commit()  # а в доке ни хуя нету
    await add_points(telegram_id, card)
    return user


async def ban_user(telegram_id: int) -> User:
    with Session() as db:
        user: User = db.query(User).filter(User.telegram_id == telegram_id).first()
        user.is_banned = True
        db.commit()
        return user


async def unban_user(telegram_id: int) -> User:
    with Session() as db:
        user: User = db.query(User).filter(User.telegram_id == telegram_id).first()
        user.is_banned = False
        db.commit()
        return user


async def add_points(telegram_id: int, card: Card) -> User:
    with Session() as db:
        user: User = db.query(User).filter(User.telegram_id == telegram_id).first()
        match card.rarity:
            case 0:
                user.point_count += 100
            case 1:
                user.point_count += 200
            case 2:
                user.point_count += 300
            case 3:
                user.point_count += 400
        db.commit()
        return user
