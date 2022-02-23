from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from core.database.db import get_db

from core.controllers.schedules import (
    get_schdule_by_body_type,
    get_meal_types,
    get_body_types
)

router = APIRouter()

@router.get("/body/{id}/schedule", tags=["schedule"])
async def get_schedule(id: int, db: Session = Depends(get_db)):
    return await get_schdule_by_body_type(id, db)

@router.get("/body/{id}/meal", tags=["schedule"])
async def get_schedule(id: int, db: Session = Depends(get_db)):
    return await get_meal_types(id, db)


@router.get("/body-types", tags=["schedule"])
async def get_schedule(db: Session = Depends(get_db)):
    return await get_body_types(db)

