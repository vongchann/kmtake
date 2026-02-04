from fastapi.testclient import TestClient

from myapp.main import app

client = TestClient(app)


def test_static_index():
    r = client.get("/static/index.html")
    assert r.status_code == 200
    assert "text/html" in r.headers.get("content-type", "")
    assert "kmtake — Demo UI" in r.text


def test_favicon_not_found():
    r = client.get("/favicon.ico")
    assert r.status_code in (404, 200)
