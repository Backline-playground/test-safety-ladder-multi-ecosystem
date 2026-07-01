from app import app


def test_index():
    client = app.test_client()
    resp = client.get("/")
    assert resp.status_code == 200
    assert resp.data == b"ok"


def test_upload_missing_file():
    client = app.test_client()
    resp = client.post("/upload")
    assert resp.status_code == 400
