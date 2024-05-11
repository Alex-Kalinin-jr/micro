import json
from fastapi import APIRouter, status, HTTPException, Depends, Query, Body
from typing import Annotated, Optional, List
from sqlmodel import select

from db.database import get_session, AsyncSession
from db.models import Question, Answer

router = APIRouter(prefix="/data")


@router.get("", status_code=200)
async def get_all_questions(*, session: AsyncSession = Depends(get_session)):
    answers = await session.exec(select(Question))
    return [answ.model_dump() for answ in answers]


@router.get("/{id}", status_code=200)
async def get_question_by_id(*, 
                             id: int,
                             session: AsyncSession = Depends(get_session)):
    answers = await session.exec(select(Answer).where(Answer.question_id == id))

    if not answers:
        raise HTTPException(status_code=404, detail="Question not found")
    
    return [answ.model_dump(round_trip=True) for answ in answers]


@router.post("", response_model=Question)
async def post_question(*,
                        question: Question,
                        session: AsyncSession = Depends(get_session)):
    session.add(question)
    await session.commit()
    session.refresh(question)
    return question
