from loader import engine
from models import Base


async def setup_db():
    Base.metadata.create_all(bind=engine)
