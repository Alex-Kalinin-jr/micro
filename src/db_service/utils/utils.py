from db.database import async_session
from db.db_data import question_data, links_data
from db.models import *

async def init_db_by_questions():
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


async def init_db_by_links():
    async with async_session() as session:
        for data in links_data:
            try:
                db_link = UrlData(**data)
                session.add(db_link)
                await session.commit()
            except Exception as e:
                print(f"EXCEPTION: {e}")
                session.rollback()
                continue
