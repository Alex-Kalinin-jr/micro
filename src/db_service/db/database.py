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
            print(f"#######this is the data[0]: {data[0]}##########")
            db_question = Question.model_validate(data[0])
            print(f"#########{db_question}########")
                #here to be improved to handle partial valid data
            db_answ = [Answer.model_validate(answ) for answ in data[1]]
                #here to be validated for presence of true answ
            if db_answ != []:
                session.add(db_question)
                await session.commit()
                session.refresh(db_answ) #here
            for answ in db_answ:
                answ.question_id  = db_question.id
                session.add(db_answ)
            await session.commit()

     
     
     
     
            # try:
            #     db_question = Question.model_validate(data[0])
            #     print("#################")
            #     print("#################")
            #     print("#################")
            #     print("#################")
            #     print("#################")
            #     print("#################")
            #     print("#################")
            #     print("#################")
            #     print(f"#########{db_question}########")
            #     #here to be improved to handle partial valid data
            #     db_answ = [Answer.model_validate(answ) for answ in data[1]]
            #     #here to be validated for presence of true answ
            #     if db_answ != []:
            #         session.add(db_question)
            #         await session.commit()
            #         session.refresh(db_answ) #here
            #     for answ in db_answ:
            #         answ.question_id  = db_question.id
            #         session.add(db_answ)
            #     await session.commit()
            # except Exception as e:
            #     print(f"error during insertion {e}")
            #     continue

