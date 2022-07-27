import json


def test_create_job(client):
    data = {
        "title": "SDE super",
        "company": "doogle",
        "company_url": "www.doogle.com",
        "location": "USA,NY",
        "description": "python",
        "date_posted": "2022-03-20"
    }
    response = client.post("/job/create-job", json.dumps(data))
    assert response.status_code == 200
    assert response.json()["company"] == "doogle"
    assert response.json()["description"] == "python"


'''def test_retreive_job_by_id(client):
    data = {
        "title": "SDE 1 Yahoo",
        "company": "testhoo",
        "company_url": "https://www.fhh.com",
        "location": "USA,NY",
        "description": "Testing",
        "date_posted": "2022-07-20"
    }

    response = client.post("/job/", json.dumps(data))
    assert response.status_code == 200'''
