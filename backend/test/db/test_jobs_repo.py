from sqlalchemy.orm import Session

from db.repository.jobs import crete_new_job, retrieve_job
from schemas.jobs import Jobcreate

from test.utils.users import create_random_owner


def test_retreive_job_by_id(db_session: Session):
    title = "test title"
    company = "test comp"
    company_url = "testcomp.com"
    location = "USA,Ny"
    description = "Foo bar"
    owner = create_random_owner(db=db_session)
    job_schema = Jobcreate(title=title, company=company, company_url=company_url, location=location,
                           description=description)
    job = crete_new_job(job=job_schema, db=db_session, owner_id=owner.id)
    retrieved_job = retrieve_job(id=job.id, db=db_session)
    assert retrieved_job.id == job.id
    assert retrieved_job.title == "test title"
