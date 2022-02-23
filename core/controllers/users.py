import datetime
from os import stat
import re
from shutil import ExecError
from typing import List
from fastapi import HTTPException, status
from sqlmodel import Session
from sqlalchemy.orm import Session
from core.database.models import users
from core.schemas import user
from core.utils.password_utils import get_password_hash, verify_password, create_access_token
from core.utils.weight_utils import get_bmi

async def list_users(db: Session) -> List[user.User]:
    return db.query(users.User).all()


async def create_user(db: Session, user: user.UserBase) -> user.User:
    try:
        create_data = user.dict()
        create_data.pop("password")
        db_obj = users.User(**create_data)
        db_obj.password = get_password_hash(user.password)
        db_obj.BMI = get_bmi(user.height, user.weight)
        db_obj.created_at = datetime.datetime.utcnow()
        db.add(db_obj)
        db.commit()
        db.refresh(db_obj)
        return db_obj
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(e))


async def read_single_user(id: int, db: Session) -> user.User:
    try:
        db_user = db.query(users.User).filter(users.User.id==id).first()
        if not db_user:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="User Unavailable")
        return db_user
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(e))



async def login_user(db: Session, user: user.UserLogin) -> dict:
    try:
        db_user = db.query(users.User).filter(users.User.email==user.email).first()
        if not db_user:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Invalid credentials")
        if not verify_password(user.password, db_user.password):
            raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid credentials")
        
        payload = {
            "email": db_user.email,
            "id": db_user.id
        }
        
        return create_access_token(payload)
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(e))


async def update_user(id: int, user: user.UserUpdate, db: Session) -> user.User:
    try:
        db_user = db.query(users.User).filter(users.User.id==id).first()
        if not db_user:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="User Unavailable")
        db_user.first_name = user.first_name
        db_user.last_name = user.last_name
        db_user.age = user.age
        db_user.weight = user.weight
        db_user.height = user.height
        db_user.BMI = get_bmi(user.height, user.weight)
        db_user.updated_at = datetime.datetime.utcnow()
        db.commit()
        db.refresh(db_user)
        return db_user
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(e))