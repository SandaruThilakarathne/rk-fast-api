from typing import List
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from core.database.db import get_db

from core.schemas import user

from core.controllers.users import (
    list_users,
    create_user,
    login_user,
    update_user,
    read_single_user
)

router = APIRouter()


@router.get("/all/", tags=["users"], response_model=List[user.User], response_model_exclude_unset=True)
async def list(db: Session = Depends(get_db)):
    return await list_users(db)


@router.post("/add/", tags=["users"], response_model=user.User, response_model_exclude_unset=True)
async def create(user: user.UserBase, db: Session = Depends(get_db)):
    return await create_user(db, user)


@router.put("/{id}/", tags=["users"], response_model=user.User, response_model_exclude_unset=True)
async def update_users(id: int, user: user.UserUpdate, db: Session = Depends(get_db)):
    return await update_user(id, user, db)


@router.get("/{id}/", tags=["users"], response_model=user.User, response_model_exclude_unset=True)
async def read_user(id: int, db: Session = Depends(get_db)):
    return await read_single_user(id, db)


@router.post("/login", tags=["users"])
async def login(user: user.UserLogin, db: Session = Depends(get_db)):
    return await login_user(db, user)