from sqlmodel.ext.asyncio.session import AsyncSession
from sqlalchemy.ext.asyncio import create_async_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker


from conf import DB_URL
from .models import *
from .db_data import question_data


engine = create_async_engine(DB_URL, echo=True, future=True)
async_session = sessionmaker(engine, class_=AsyncSession, expire_on_commit=False)


async def get_session():
    async with async_session() as session:
        yield session


async def init_db():
    async with engine.begin() as conn:
        await conn.run_sync(SQLModel.metadata.create_all)

    async with async_session() as session:
        for data in question_data:
            try:
                db_question = Question(**(data[0]))
                answers = [Answer(**answ) for answ in data[1]]
                db_question.answers = answers

                session.add(db_question)
                await session.commit()
            except Exception as e:
                print(f"EXCEPTION: {e}")
                session.rollback()
                continue

