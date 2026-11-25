from fastapi.testclient import TestClient

from app.main import app

client = TestClient(app)


def test_root():
    res = client.get("/")
    assert res.status_code == 200
    assert res.json() == {"message": "hello hackathon"}


def test_health():
    res = client.get("/health")
    assert res.status_code == 200
    assert res.json() == {"status": "ok"}


def test_version():
    assert client.get("/version").json() == {"version": "0.1.0"}
