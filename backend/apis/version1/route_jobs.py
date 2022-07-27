from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from typing import List
from db.session import get_db
from schemas.jobs import Jobcreate, ShowJob
from db.repository.jobs import crete_new_job, retrieve_job, list_job, update_job_by_id, delete_job_by_id
from db.models.jobs import Job

router = APIRouter()


@router.post("/create-job", response_model=ShowJob)
def create_job(job: Jobcreate, db: Session = Depends(get_db)):
    owner_id = 1
    job = crete_new_job(job=job, db=db, owner_id=owner_id)
    return job


@router.get("/get/{id}", response_model=ShowJob)
def retrieve_job_by_id(id: int, db: Session = Depends(get_db)):
    job = retrieve_job(id=id, db=db)
    print(job)
    if not job:
        HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Job with the id {id} not found")
    return job


@router.get("/all", response_model=List[ShowJob])
def retrieve_all_jobs(db: Session = Depends(get_db)):
    jobs = list_job(db=db)
    return jobs


@router.put("/update/{id}")
def update_job(id: int, job: Jobcreate, db: Session = Depends(get_db)):
    owner_id = 1
    message = update_job_by_id(id=id, job=job, db=db, owner_id=owner_id)
    if not message:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Job with the id {id} does not exist")
    return {"details": "Successfully update data"}


@router.delete("/delete/{id}")
def delete_job(id: int, db: Session = Depends(get_db)):
    owner_id = 1
    message = delete_job_by_id(id=id, db=db, owner_id=owner_id)
    if not message:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Job with the id{id} does not exist")
    return {"detail": "deleted successfully"}
