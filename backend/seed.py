import os
from sqlmodel import Session
from app.database import engine, init_db
from app.models import User, Card, CardBody
from app.auth import get_password_hash


def main():
    init_db()
    with Session(engine) as session:
        user = User(email="seed@example.com", password_hash=get_password_hash("secret"))
        session.add(user)
        session.commit()
        session.refresh(user)
        samples = [
            ("math", "What is 1+1?", "2"),
            ("english", "Translate 'hello'", "你好"),
            ("politics", "What is democracy?", "Rule by the people"),
        ]
        for subject, q, a in samples:
            card = Card(subject=subject, tags=[], difficulty=1, owner_id=user.id)
            session.add(card)
            session.commit()
            session.refresh(card)
            body = CardBody(card_id=card.id, question_md=q, answer_md=a)
            session.add(body)
            session.commit()
    print("Seed data inserted")


if __name__ == "__main__":
    main()
