from datetime import date, datetime

from pydantic import BaseModel

# This is our object oriented models
class LeagueBase(BaseModel):
    name: str
    description: str | None = None
    membership_cost: int | None = 0
    drop_in_cost: int | None = 0

class League(LeagueBase):
    id: int

class UserBase(BaseModel):
    first_name: str
    last_name: str
    email: str
    birthdate: date
    phone_number: int

class UserCreate(UserBase):
    password: str


class User(UserBase):
    id: int

    memberships: list[League] = []

    class Config:
        from_attributes = True