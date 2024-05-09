from typing import Optional
from uuid import UUID, uuid4
from sqlmodel import SQLModel, Field, Relationship, BackPopulates
from sqlalchemy import Enum as SqlEnum 


class QuestionType(SqlEnum):
    TEXT = 'text'
    IMG = 'image'


class Question(SQLModel, table=True):
    id: Optional[UUID] = Field(default_factory=uuid4, primary_key=True)
    type = Field(QuestionType)
    text = Field(str)
    answer: list["Answer"] = Relationship(back_populates="answer")


class Answer(SQLModel):
    id: Optional[UUID] = Field(default_factory=uuid4, primary_key=True)
    is_right = Field(bool)
    question_id = Field(UUID, foreign_key = Question.id, index = True)
    question: Question = Relationship(back_populates="question")


class TextAnswer(Answer, table=True):
    text = Field(str)


class ImgAnswer(Answer, table=True):
    link = Field(str)


# #interaction - future
# def CreateQuestion(the_text: str, the_type: QuestionType, engine: AsyncEngine) -> None:
#     with Session(engine) as session:
#         question = Question(type = the_type, text = the_text)
#         session.add(question)
#         session.commit()


# def CreateQuestions(the_data: list[tuple], engine: AsyncEngine) -> None:
#     with Session(engine) as session:
#         for the_type, the_text in the_data:
#             question = Question(type = the_type, text = the_text)
#             session.add(question)
#         session.commit()


# def CreateTextAnswer(the_question: UUID, the_type: QuestionType, the_text: [str], engine: AsyncEngine):
#     with Session(engine) as session:
#         if the_type is TextAnswer:
#             for variant in the_text:
#                 answ = TextAnswer(the_question, variant)
#                 session.add(answ)
#         elif the_type is ImgAnswer:
#             for variant in the_text:
#                 answ = ImgAnswer(the_question, variant)
#                 session.add(answ)
#         session.commit()


# session.refresh(object)

    # with Session(engine) as session:
    #     statement = select(Hero)
    #     results = session.exec(statement)
    

# IMPORTANT!
# hero = session.get(Hero, 1)


# IMPORTANT! JOIN
# statement = select(Hero, Team).where(Hero.team_id == Team.id)
# statement = select(Hero, Team).join(Team)
# statement = select(Hero, Team).join(Team, isouter=True)


#IMPORTANT! HOW TO AVOID CIRCULAR LINKS
# if TYPE_CHECKING:
#     from .hero_model import Hero


#IMPORTANT! HOW TO GET OBJECT BY FIELD
# @app.get("/heroes/{hero_id}", response_model=HeroPublic)
# def read_hero(hero_id: int):
#     with Session(engine) as session:
#         hero = session.get(Hero, hero_id)
#         if not hero:
#             raise HTTPException(status_code=404, detail="Hero not found")
#         return hero


#FLAGS OF SERIALIZATION
# exclude_unset
# round_trip
# exclude_defaults
# exclude_none
# serialization_alias= -> by_alias


# IMPORTANT! UPDATING WITH EXTRA DATA. If there's a field in both hero and the extra_data, the value from the extra_data passed to update will take precedence.
# db_hero = Hero.model_validate(hero, update=extra_data)