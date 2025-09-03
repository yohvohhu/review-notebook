from typing import List, Optional
from fastapi import APIRouter, Depends, HTTPException
from sqlmodel import Session, select
from pydantic import BaseModel
from ..database import get_session
from ..auth import get_current_user
from ..models import Card, CardBody, User

router = APIRouter(prefix="/cards", tags=["cards"])


class Hint(BaseModel):
    order: int
    text_md: str


class CardBodyCreate(BaseModel):
    question_md: str
    images: List[str] = []
    source: Optional[str] = None
    expected_time_sec: Optional[int] = None
    hints: List[Hint] = []
    answer_md: str
    steps_md: Optional[str] = None
    error_patterns: List[str] = []
    checklist: List[str] = []
    knowledge: dict = {}
    variants: dict = {}


class CardCreate(BaseModel):
    subject: str
    tags: List[str] = []
    difficulty: int = 1
    body: CardBodyCreate


@router.post("", response_model=Card)
def create_card(data: CardCreate, session: Session = Depends(get_session), user: User = Depends(get_current_user)):
    card = Card(subject=data.subject, tags=data.tags, difficulty=data.difficulty, owner_id=user.id)
    session.add(card)
    session.commit()
    session.refresh(card)
    body = CardBody(card_id=card.id, **data.body.dict())
    session.add(body)
    session.commit()
    session.refresh(card)
    return card


@router.get("/{card_id}", response_model=Card)
def get_card(card_id: int, session: Session = Depends(get_session), user: User = Depends(get_current_user)):
    card = session.get(Card, card_id)
    if not card or card.owner_id != user.id:
        raise HTTPException(status_code=404, detail="Card not found")
    return card


@router.get("", response_model=List[Card])
def list_cards(subject: Optional[str] = None, session: Session = Depends(get_session), user: User = Depends(get_current_user)):
    stmt = select(Card).where(Card.owner_id == user.id)
    if subject:
        stmt = stmt.where(Card.subject == subject)
    return session.exec(stmt).all()
