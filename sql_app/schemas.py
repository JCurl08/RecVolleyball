from datetime import date, datetime

from pydantic import BaseModel

# This is our object oriented models
# class LeagueBase(BaseModel):
#     name: str
#     description: str | None = None
#     membership_cost: int | None = 0
#     drop_in_cost: int | None = 0

# class League(LeagueBase):
#     id: int

class UserBase(BaseModel):
    username: str | None = None
    first_name: str | None = None
    last_name: str | None = None
    email: str | None = None
    birthday: date | None = None
    phone_number: int | None = None

class UserCreate(UserBase):
    password: str | None = None


class User(UserBase):

    # memberships: list[League] = []

    class Config:
        from_attributes = True