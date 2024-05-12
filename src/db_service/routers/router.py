import json
from fastapi import APIRouter, status, HTTPException, Depends, Query, Body
from typing import Annotated, Optional, List
from sqlmodel import select

from db.database import get_session, AsyncSession
from db.models import Question, Answer

router = APIRouter(prefix="/data")


@router.get("/questions", status_code=200)
async def get_all_questions(*, session: AsyncSession = Depends(get_session)):
    print("###########################")
    print("###########################")
    print("###########################")
    print("###########################")
    print("###########################")
    print("i was here")
    questions = await session.exec(select(Question))
    return [question.model_dump() for question in questions]

@router.get("/answers", status_code=200)
async def get_all_answers(*, session: AsyncSession = Depends(get_session)):
    answers = await session.exec(select(Question))
    return [answer.model_dump() for answer in answers]


@router.get("/answers/{id}", status_code=200)
async def get_answers_by_question_id(*, 
                             id: int,
                             session: AsyncSession = Depends(get_session)):
    answers = await session.exec(select(Answer).where(Answer.question_id == id))

    if not answers:
        raise HTTPException(status_code=404, detail="Question not found")
    
    return [answ.model_dump(round_trip=True) for answ in answers]


@router.post("/questions", status_code=201, response_model=Question)
async def post_question(*,
                        question: Question,
                        session: AsyncSession = Depends(get_session)):
    session.add(question)
    await session.commit()
    session.refresh(question)
    return question

#there the validation must be prepared. Answers must have at least one right answer and their count must be more than one
@router.post("/answers/{id}", response_model=Question)
async def post_answers_for_question(*,
                       id: int,
                       answers: List[Answer],
                       session: AsyncSession = Depends(get_session)):
    question = await session.get(Question, id)
    for answ in answers:
        answ.question_id = question.id
        session.add(answ)
    await session.commit()
    session.refresh(question)
    return question
