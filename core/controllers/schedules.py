from fastapi import HTTPException, status
from sqlmodel import Session
from sqlalchemy.orm import Session
from core.database.models import schedules

from core.utils.json_utils import read_json


async def get_schdule_by_body_type(id: int, db: Session):
    
    week_ = db.query(schedules.WeekBodyType).filter(schedules.WeekBodyType.body == id).all()
    array_weeks = {}
    array_days = {}
    schedule__ = {}
    for week in week_:
        week_day_rel_ = db.query(
            schedules.WeeksDayRelation
        ).filter(
            schedules.WeeksDayRelation.week_id == week.id
        ).all()

        for week_day in week_day_rel_:
            sche = db.query(
                schedules.Schedule
            ).filter(
                schedules.Schedule.week_day_id == week_day.id
            ).first()
            shedule = {}
            if sche:
                shedule = {
                    "id": sche.id,
                    "exerices": read_json(sche.json_link)
                }
            else:
                shedule = {
                    "id": None,
                    "exerices": None
                }
            day = db.query(
                schedules.Days
            ).filter(
                schedules.Days.id == week_day.day_id
            ).first()
            array_days[day.name] = shedule
        array_weeks[week.id] = array_days
    schedule__["data"] = array_weeks
    return schedule__


async def get_meal_types(id: int, db: Session):
    meal_ = db.query(schedules.MealPlan).filter(schedules.MealPlan.body == id).first()
    if meal_:
        meal_.meal_plan_link = read_json(meal_.meal_plan_link)
        return meal_
    else:
        raise HTTPException(status.HTTP_404_NOT_FOUND, "No meal plan for body type")


async def get_body_types(db: Session):
    body_ = db.query(schedules.BodyTypes).all()

    return body_