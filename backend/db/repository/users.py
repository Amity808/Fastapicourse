from sqlalchemy.orm import Session

from schemas.users import UserCreate

from db.models.users import User
from core.hashing import Hash


def create_new_user(user: UserCreate, db: Session):
    user = User(username=user.username,
                email=user.email,
                hashed_password=Hash.bcrypt(user.password),
                is_active=True,
                is_superuser=False
                )
    db.add(user)
    db.commit()
    db.refresh(user)
    return user


def retrieve_user_by_id(id: int, db: Session):
    user = db.query(User).filter(User.id == id).first()
    return user
