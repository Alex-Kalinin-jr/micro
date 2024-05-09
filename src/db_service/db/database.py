from sqlmodel.ext.asyncio.session import AsyncSession
from sqlalchemy.ext.asyncio import create_async_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker


from .conf import DB_URL
from .models import *
from .db_data import question_data

engine = create_async_engine(DB_URL, echo=True, future=True)
async_session = sessionmaker(engine, class_=AsyncSession, expire_on_commit=False)
Base = declarative_base()

async def init_db():
    async with engine.begin() as conn:
        await conn.run_sync(SQLModel.metadata.create_all)
        for data in question_data:
            question = Question.model_validate(data[0])
            answers = [TextAnswer.model_validate(answ for answ in data[1])]
            try:
                await conn.execute(Question.__table__.insert(), question)
                for answer in answers:
                    await conn.execute(TextAnswer.__table__.insert(), answer)
            except Exception as e:
                print(f"error during insertion {e}")
                continue
        await conn.commit()

async def get_session():
    async with async_session() as session:
        yield session

