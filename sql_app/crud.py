from sqlalchemy.orm import Session

import models, schemas

# This is where the queries go

def get_user(db: Session, username: str):
    return db.query(models.User).filter(models.User.username == username).first()

def get_user_by_email(db: Session, email: str):
    return db.query(models.User).filter(models.User.email == email).first()

def get_users(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.User).offset(skip).limit(limit).all()

def update_user(db: Session, username: str, user: schemas.UserCreate):
    db_user = db.query(models.User).filter(models.User.username == username).first()
    if user.password not in [None, ""]:
        db_user.password = user.password + "notreallyhashed"
    if user.username not in [None, ""]:
        db_user.username = user.username
    if user.first_name not in [None, ""]:
        db_user.first_name = user.first_name
    if user.last_name not in [None, ""]:
        db_user.last_name = user.last_name
    if user.phone_number != None:
        db_user.username = user.username
    if user.email not in [None, ""]:
        db_user.email = user.email
    if user.birthday not in [None, ""]:
        db_user.birthday = user.birthday
    db.commit()
    db.refresh(db_user)
    return db_user


def create_user(db: Session, user: schemas.UserCreate):
    fake_hashed_password = user.password + "notreallyhashed"
    db_user = models.User(username=user.username, first_name=user.first_name, last_name=user.last_name, email=user.email, phone_number=user.phone_number, birthday=user.birthday, hashed_password=fake_hashed_password)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user