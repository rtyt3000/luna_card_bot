async def rarity_to_data(rarity) -> {str, int}:
    match rarity:
        case 0:
            card_rarity = "Обычная"
            points = 100
        case 1:
            card_rarity = "Редкая"
            points = 200
        case 2:
            card_rarity = "Эпическая"
            points = 300
        case 3:
            card_rarity = "Легендарная"
            points = 400
        case _:
            card_rarity = "Ошибка"
            points = 0
    return {"rarity": card_rarity, "points": points}
