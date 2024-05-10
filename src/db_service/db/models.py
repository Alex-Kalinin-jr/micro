from typing import Optional
from uuid import UUID, uuid4
from sqlmodel import SQLModel, Field, Relationship
from sqlalchemy import Enum as SqlEnum


class Question(SQLModel, table=True):
    id: Optional[int] = Field(primary_key=True)
    type: str = Field(...)
    text: str = Field(...)

    answers: list["Answer"] = Relationship(back_populates="question")

class Answer(SQLModel, table=True):
    id: Optional[int] = Field(primary_key=True)
    question_id: int = Field(foreign_key = "question.id", index = True)
    data: str = Field(...)
    is_right: bool = Field(...)

    question: Question = Relationship(back_populates="answers")
