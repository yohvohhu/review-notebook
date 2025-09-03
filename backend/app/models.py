from __future__ import annotations
from datetime import datetime
from typing import List, Optional
from sqlmodel import SQLModel, Field, Column, JSON, Relationship


class User(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    email: str = Field(index=True, unique=True)
    password_hash: str
    created_at: datetime = Field(default_factory=datetime.utcnow)

    cards: List[Card] = Relationship(back_populates="owner")  # type: ignore


class Card(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    subject: str = Field(index=True)
    tags: List[str] = Field(sa_column=Column(JSON), default_factory=list)
    difficulty: int = 1
    box: int = Field(default=1, index=True)
    due_at: datetime = Field(default_factory=datetime.utcnow, index=True)
    ease: float = 2.5
    interval_days: int = 0
    repetitions: int = 0
    lapse_count: int = 0
    leech_score: int = 0
    created_at: datetime = Field(default_factory=datetime.utcnow)
    updated_at: datetime = Field(default_factory=datetime.utcnow)
    owner_id: int = Field(foreign_key="user.id", index=True)

    body: Optional[CardBody] = Relationship(back_populates="card")
    owner: Optional[User] = Relationship(back_populates="cards")


class CardBody(SQLModel, table=True):
    card_id: int = Field(primary_key=True, foreign_key="card.id")
    question_md: str
    images: List[str] = Field(sa_column=Column(JSON), default_factory=list)
    source: Optional[str] = None
    expected_time_sec: Optional[int] = None
    hints: List[dict] = Field(sa_column=Column(JSON), default_factory=list)
    answer_md: str
    steps_md: Optional[str] = None
    error_patterns: List[str] = Field(sa_column=Column(JSON), default_factory=list)
    checklist: List[str] = Field(sa_column=Column(JSON), default_factory=list)
    knowledge: dict = Field(sa_column=Column(JSON), default_factory=dict)
    variants: dict = Field(sa_column=Column(JSON), default_factory=dict)

    card: Optional[Card] = Relationship(back_populates="body")


class ReviewLog(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    card_id: int = Field(foreign_key="card.id")
    user_id: int = Field(foreign_key="user.id")
    timestamp: datetime = Field(default_factory=datetime.utcnow)
    result: str
    confidence: int
    time_spent_sec: int
    hint_count: int
    peeked: bool
    box_before: int
    box_after: int


class WorkspaceDraft(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    card_id: int = Field(foreign_key="card.id")
    user_id: int = Field(foreign_key="user.id")
    content_md: str = ""
    updated_at: datetime = Field(default_factory=datetime.utcnow)
