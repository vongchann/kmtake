from fastapi.testclient import TestClient

from myapp.main import app

client = TestClient(app)


def test_root_serves_index():
    r = client.get("/")
    assert r.status_code == 200
    assert "text/html" in r.headers.get("content-type", "")
    assert "kmtake — Demo UI" in r.text
