from fastapi.testclient import TestClient
from app import app

client = TestClient(app)


def test_health():
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json() == {"status": "ok"}


def test_add():
    response = client.get("/add?a=2&b=3")
    assert response.status_code == 200
    assert response.json() == {"result": 5}


def test_add_negative():
    response = client.get("/add?a=-1&b=5")
    assert response.status_code == 200
    assert response.json() == {"result": 4}

def test_multiply():
    response = client.get("/multiply?a=3&b=4")
    assert response.status_code == 200
    assert response.json() == {"result": 12}


def test_version_on_312():
    import sys
    response = client.get("/version")
    assert response.status_code == 200
    if sys.version_info.minor == 12:
        assert response.json() == {"python": "3.12", "support": "full"}
    else:
        assert response.json()["support"] == "full"  # this will FAIL on 3.10, 3.11