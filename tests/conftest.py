import pytest
import requests
import random

from app.models import grades, Gender, Department
from urllib.parse import urljoin

from src.config import config


def pytest_addoption(parser):
    parser.addoption(
        "--app_host",
        action="store",
        default=f"http://{config['app']['host']}:{config['app']['port']}",
    )


@pytest.fixture(scope="session")
def app_host(request):
    return request.config.getoption("--app_host")


@pytest.fixture(scope="session")
def session(app_host):
    class AppClient(requests.Session):
        def __init__(self, base):
            super().__init__()
            self.base = base

        def get(self, path, **kwargs):
            return super().get(url=urljoin(self.base, path))

        def post(self, path, data=None, json=None, **kwargs):
            return super().post(
                url=urljoin(self.base, path), data=data, json=json, **kwargs
            )

        def delete(self, path, **kwargs):
            return super().delete(url=urljoin(self.base, path), **kwargs)

        def patch(self, url, data=None, **kwargs):
            return super().patch(url=urljoin(self.base, url), data=data, **kwargs)

    return AppClient(base=app_host)


@pytest.fixture
def create_worker(session):
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

    yield response.json()["worker_id"]

    session.delete(f"/workers/delete", json={"worker_id": response.json()["worker_id"]})
