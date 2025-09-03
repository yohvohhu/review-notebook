from fastapi import FastAPI, Depends
from fastapi.middleware.cors import CORSMiddleware
from .database import init_db
from .auth import router as auth_router, get_current_user
from .routers import cards

app = FastAPI(title="Smart Mistake Notebook")

origins = ["*"]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(auth_router)
app.include_router(cards.router)


@app.on_event("startup")
def on_startup():
    init_db()


@app.get("/me")
def read_me(user=Depends(get_current_user)):
    return {"id": user.id, "email": user.email}
