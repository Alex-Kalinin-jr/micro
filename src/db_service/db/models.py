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


#to be relocated
def validate_answers(self, answers: List["Answer"]) -> List["Answer"]:
    if len(answers) < 2:
        raise ValueError("There should be more than one answer.")

    right_answers = [answer for answer in answers if answer.is_right]
    if len(right_answers) != 1:
        raise ValueError("There should be exactly one answer with is_right = True.")

    return answers