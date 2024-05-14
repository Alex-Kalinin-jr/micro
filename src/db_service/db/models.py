from typing import Optional, List
from uuid import UUID, uuid4
from sqlmodel import SQLModel, Field, Relationship
from sqlalchemy import Enum as SqlEnum
from pydantic import field_validator


class Question(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    type: str = Field(...)
    text: str = Field(...)

    answers: list["Answer"] = Relationship(back_populates="question")


class Answer(SQLModel, table=True):
    id: Optional[int] = Field(primary_key=True)
    question_id: int = Field(foreign_key = "question.id", index = True)
    data: str = Field(...)
    is_right: bool = Field(...)

    question: Question = Relationship(back_populates="answers")


class UrlData(SQLModel, table=True):
    id: Optional[int] = Field(primary_key=True)
    data: str = Field(...)
    explanation: str = Field(...)
