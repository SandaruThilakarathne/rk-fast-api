from sqlalchemy import Column, ForeignKey, Integer, String, Float, Date
from sqlalchemy.orm import relationship

from core.database.db import Base


class User(Base):
    __tablename__="my-profile-user"
    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    email = Column(String(80), nullable=False, index=True, unique=True)
    first_name = Column(String(250), nullable=True)
    last_name = Column(String(80), nullable=True)
    password = Column(String(250), nullable=False)
    age = Column(Integer, nullable=True)
    weight = Column(Float, nullable=True)
    height = Column(Float, nullable=True)
    BMI = Column(Float, nullable=True)
    created_at = Column(Date, nullable=True)
    updated_at = Column(Date, nullable=True)

    class Config:
        orm_mode = True