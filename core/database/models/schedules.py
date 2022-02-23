from email.mime import base
from tkinter.tix import Tree
from sqlalchemy import Column, ForeignKey, Integer, String, Float, Date, ForeignKey
from sqlalchemy.orm import relationship

from core.database.db import Base

class BodyTypes(Base):
    __tablename__="body-type"
    __table_args__ = {'extend_existing': True}
    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    name = Column(String(250), nullable=True)
    image_url = Column(String, nullable=True)
    weeks_body = relationship("WeekBodyType")
    meal_plan = relationship("MealPlan")


class Weeks(Base):
    __tablename__="week"
    __table_args__ = {'extend_existing': True}
    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    name = Column(String(250), nullable=True)
    week_day_relation = relationship("WeeksDayRelation")


class WeekBodyType(Base):
    __tablename__="week-body"
    __table_args__ = {'extend_existing': True}
    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    week_id =  Column(Integer, ForeignKey("week.id", ondelete="CASCADE"), nullable=True,)
    body =  Column(Integer, ForeignKey("body-type.id", ondelete="CASCADE"), nullable=True,)

class Days(Base):
    __tablename__="day"
    __table_args__ = {'extend_existing': True}
    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    name = Column(String(250), nullable=True)
    week_day_relation = relationship("WeeksDayRelation")


class WeeksDayRelation(Base):
    __tablename__='week_day_relation'
    __table_args__ = {'extend_existing': True}
    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    week_id =  Column(Integer, ForeignKey("week.id", ondelete="CASCADE"), nullable=True,)
    day_id = Column(Integer, ForeignKey("day.id", ondelete="CASCADE"), nullable=True)
    schedule = relationship("Schedule")


class Schedule(Base):
    __tablename__='schedule'
    __table_args__ = {'extend_existing': True}
    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    json_link = Column(String(500), nullable=True)
    week_day_id = Column(Integer, ForeignKey("week_day_relation.id", ondelete="CASCADE"), nullable=True)



class MealPlan(Base):
    __tablename__="meal-plan"
    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    name = Column(String(250), nullable=True)
    meal_plan_link = Column(String(250), nullable=True)
    body =  Column(Integer, ForeignKey("body-type.id", ondelete="CASCADE"), nullable=True,)
 