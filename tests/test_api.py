from fastapi.testclient import TestClient

from myapp.main import app

client = TestClient(app)


def test_health():
    r = client.get("/health")
    assert r.status_code == 200
    assert r.json() == {"status": "ok"}


def test_create_and_get_item():
    payload = {"id": 1, "name": "Test", "description": "desc"}
    r = client.post("/items", json=payload)
    assert r.status_code == 201
    assert r.json() == payload

    r2 = client.get("/items/1")
    assert r2.status_code == 200
    assert r2.json() == payload


def test_item_not_found():
    r = client.get("/items/9999")
    assert r.status_code == 404
