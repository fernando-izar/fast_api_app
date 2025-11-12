from typing import Annotated
from sqlalchemy.orm import Session
from fastapi import APIRouter, Depends, HTTPException, status, Path
from pydantic import BaseModel, Field
from models import Users
from database import SessionLocal
from .auth import get_current_user


router = APIRouter(prefix="/user", tags=["user"])


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


db_dependency = Annotated[Session, Depends(get_db)]
user_dependency = Annotated[dict, Depends(get_current_user)]


@router.put("/phone_number/{phone_number}", status_code=status.HTTP_204_NO_CONTENT)
def update_phone_number(
    phone_number: str,
    user: user_dependency,
    db: db_dependency,
):

    if not user:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="User not found"
        )

    user_to_update = db.query(Users).filter(Users.id == user.get("id")).first()
    user_to_update.phone_number = phone_number
    db.commit()
