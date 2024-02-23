from fastapi import FastAPI, HTTPException, Depends, status
from pydantic import BaseModel
from typing import Annotated
import models
from database import engine, SessionLocal
from sqlalchemy.orm import Session
from models import StatusEnum,PriorityEnum,TickettypeEnum,ServiceEnum

app = FastAPI()
models.Base.metadata.create_all(bind=engine)

class Task(BaseModel):
    LLM_id : int
    feedback : str
    failed_reason : str
    response : str
    reference : str
    status : StatusEnum
    created_by : str
    updated_by : str

class LLMBase(BaseModel):
    ticket_id : int
    requestor_name : str
    severity : int
    priority : PriorityEnum
    ticket_type : TickettypeEnum
    service : ServiceEnum
    message : str


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close

db_dependency = Annotated[Session, Depends(get_db)]

@app.post("/ticket/", status_code=status.HTTP_201_CREATED)
async def create_ticket(ticket: LLMBase, db: db_dependency):
    db_user = models.LLM(**ticket.dict())
    db.add(db_user)
    db.commit()