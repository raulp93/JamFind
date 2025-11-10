# from sqlalchemy import Column, Integer, String, ForeignKey, Text, Boolean, JSON, BLOB, Date, DateTime
# from sqlalchemy.orm import relationship
# from .database import Base


# class Vendor(Base):
#     __tablename__ = 'vendors'
#     id = Column(Integer, primary_key=True)
#     companyName = Column(String)
#     contactPerson = Column(String)
#     contactPersonPosition = Column(String)
#     email = Column(String)
#     phone = Column(String)


from pydantic import BaseModel
from typing import Optional

class User(BaseModel):
    email: Optional[str] = None
    first_name: Optional[str] = None
    last_name: Optional[str] = None
    disabled: Optional[bool] = None

class UserInDB(User):
    hashed_password: str

class UserCreate(BaseModel):
    email: str
    first_name: str
    last_name: str
    password: str
