from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession, async_sessionmaker
from sqlalchemy.orm import DeclarativeBase
from app.config import DATABASE_URL

# how to connect to DB (just tube to DB)
engine = create_async_engine(DATABASE_URL, echo=True)

#fabric for session which do new certian action (insert, del, commit)
SessionLocal = async_sessionmaker(engine, expire_on_commit=False)

class Base(DeclarativeBase):
    pass

async def get_db():
    #with - if happen error "with" close session without problem
    async with SessionLocal() as session:
        yield session