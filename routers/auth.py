from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from sqlalchemy import select
from typing import Annotated

from database import get_db
from models import User
from schemas import UserCreate, UserResponse
from core import hash_password, create_token, verify_password

router = APIRouter(prefix="/auth", tags=["auth"])

@router.post("/login")
def login(user: UserCreate, db: Annotated[Session, Depends(get_db)]):
    res = db.execute(select(User).where(User.username == user.username))
    existing = res.scalars().first()
    if existing is None or not verify_password(user.password, existing.password):
        raise HTTPException(status_code=401, detail="Invalid username or password")
    token = create_token({"sub": str(existing.id)})  
    # ↑str() because JWT only accepts string values, but our user ID is an int. We can convert it back to int when decoding the token in core.py
    return {"access_token": token, "token_type": "bearer"}