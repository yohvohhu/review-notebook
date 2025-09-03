import os
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.append(str(ROOT))
os.environ["DATABASE_URL"] = "sqlite:///./test.db"

from fastapi.testclient import TestClient
from sqlmodel import SQLModel
from app.main import app
from app.database import engine

client = TestClient(app)


def setup_module():
    SQLModel.metadata.create_all(engine)


def teardown_module():
    SQLModel.metadata.drop_all(engine)


def get_token():
    client.post("/auth/register", data={"username": "a@example.com", "password": "secret"})
    res = client.post("/auth/login", data={"username": "a@example.com", "password": "secret"})
    return res.json()["access_token"]


def test_register_login_me():
    token = get_token()
    res = client.get("/me", headers={"Authorization": f"Bearer {token}"})
    assert res.status_code == 200
    assert res.json()["email"] == "a@example.com"


def test_create_get_card():
    token = get_token()
    card_data = {
        "subject": "math",
        "tags": ["algebra"],
        "difficulty": 3,
        "body": {
            "question_md": "What is 2+2?",
            "answer_md": "4"
        }
    }
    res = client.post("/cards", json=card_data, headers={"Authorization": f"Bearer {token}"})
    assert res.status_code == 200
    card_id = res.json()["id"]
    res = client.get(f"/cards/{card_id}", headers={"Authorization": f"Bearer {token}"})
    assert res.status_code == 200
    assert res.json()["subject"] == "math"
