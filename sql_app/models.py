from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, Date, DateTime, Table
from sqlalchemy.orm import relationship

from database import Base

# These are essentially the make table statements

member_attendance_table = Table(
    "member_attendances",
    Base.metadata,
    Column("username", ForeignKey("users.username"), primary_key=True),
    Column("league_id", ForeignKey("sessions.league_id"), primary_key=True),
    Column("start_time", ForeignKey("sessions.start_time"), primary_key=True)
)

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    first_name = Column(String, nullable = False, index=True)
    last_name = Column(String, nullable=False, index=True)
    email = Column(String, unique=True, nullable=False, index=True)
    birthday = Column(Date, nullable=False, index=True)
    phone_number = Column(Integer, nullable=False, index=True)
    hashed_password = Column(String)

    membership_purchases = relationship("Membership_Purchase", back_populates="members")
    drop_in_purchases = relationship("Drop_In_Purchase", back_populates="drop_ins")
    sessions_attended_as_member = relationship(secondary=member_attendance_table, back_populates="members_attended")

class League(Base):
    __tablename__ = "leagues"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False, index=True)
    description = Column(String, index=True)
    membership_cost = Column(Integer, nullable=False, index=True)
    drop_in_cost = Column(Integer, index=True)

    members = relationship("Membership_Purcahse", back_populates="league_id")
    sessions = relationship("Session", back_populates="league_id")

class Session(Base):
    __tablename__ = "sessions"

    league_id = Column(Integer, ForeignKey("leagues.id"), primary_key=True, index=True)
    start_time = Column(DateTime, primary_key=True, nullable=False, index=True)
    end_time = Column(DateTime, nullable=False, index=True)

    members_attended = Column

class Purchase(Base):
    __tablename__ = "purchases"

    id = Column(Integer, primary_key=True, index=True)
    ammount = Column(Integer, nullable=False, index=True)
    payment_method = Column(String, nullable=False, index=True)
    date = Column(DateTime, nullable=False, index=True)

class Membership_Purchase(Base):
    __tablename__ = "membership_purchases"

    id = Column(Integer, ForeignKey("purchases.id"), primary_key=True, index=True)
    username = Column(String, ForeignKey("users.username"), index=True)
    member_role = Column(String, index=True)
    league_id = Column(Integer, ForeignKey("leagues.id"), index=True)

class Drop_In_Purchase(Base):
    __tablename__ = "drop_in_purchases"

    id = Column(Integer, ForeignKey("purchases.id"), primary_key=True, index=True)
    username = Column(String, ForeignKey("users.username"), index=True)
    league_id = Column(Integer, ForeignKey("sessions.league_id"), index=True)
    session_start_time = Column(DateTime, ForeignKey("sessions.start_time"))


