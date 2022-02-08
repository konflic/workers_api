import random
from app.models import grades, Gender, Department


def test_workers(session):
    response = session.get("/workers")
    assert response.status_code == 200


def test_add_worker(session):
    random_user = {
        "name": "Test User",
        "department": random.choice([dept.value for dept in Department]),
        "position": "Tester",
        "grade": random.choice(grades),
        "gender": random.choice([gender.value for gender in Gender]),
        "birthday": "1987-02-10",
    }

    response = session.post("/workers/add", json=random_user)
    assert response.status_code == 200
    assert response.json()["success"] == True


def test_delete_worker(session, create_worker):
    response = session.delete(f"/workers/delete", json={"worker_id": create_worker})
    assert response.status_code == 200
    assert response.json()["success"] == True


def test_get_worker_by_id(session, create_worker):
    response = session.get(f"/workers/{create_worker}")
    assert response.status_code == 200, response.text
    assert str(response.json()["id"]) == create_worker


def test_worker_update(session, create_worker):
    new_name = "New Updated"
    response = session.patch(
        f"/workers/update", json={"worker_id": create_worker, "name": new_name}
    )
    assert response.status_code == 200, response.text
    response = session.get(f"/workers/{create_worker}")
    assert response.status_code == 200, response.text
    assert str(response.json()["name"]) == new_name


def test_worker_update_negative(session, create_worker):
    new_name = "New Updated"
    response = session.patch(
        f"/workers/update", json={"worker_id": -1, "name": new_name}
    )
    assert response.status_code == 400
    assert response.json().get("error") == "worker_id is required as numeric value"
