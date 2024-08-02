from loader import Session
from models import Card
from random import randint
import numpy


async def create_card(rarity: int, name: str, image: str) -> Card:
    with Session() as db:
        card = Card(rarity=rarity, name=name, image=image)
        db.add(card)
        db.commit()


async def get_random_card() -> Card:
    with Session() as db:
        rarities = [0, 1, 2, 3]
        rarity = int(numpy.random.choice(rarities, 1, p=[0.40, 0.30, 0.20, 0.10])[0])
        cards = db.query(Card).filter(Card.rarity == rarity).all()
        cards_len = len(cards)
        random_card = randint(0, cards_len - 1)
        choose_card = cards[random_card]
        return choose_card
