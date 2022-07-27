from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from schemas.users import UserCreate, ShowUser
from db.session import get_db
from db.repository.users import create_new_user, retrieve_user_by_id

router = APIRouter()


@router.post("/", response_model=ShowUser)
def create_user(user: UserCreate, db: Session = Depends(get_db)):
    user = create_new_user(user, db)
    return user


@router.get("/get/{id}", response_model=ShowUser)
def get_by_id(id:int, db: Session = Depends(get_db)):
    user = retrieve_user_by_id(id=id, db=db)
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"User with the following {id} does not exist")
    return user