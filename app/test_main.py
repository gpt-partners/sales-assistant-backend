from fastapi.testclient import TestClient

from .main import app

client = TestClient(app)


def test_get_main():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"status": "OK"}


def test_post_vito():
    response = client.post(
        "/vito",
        json={
            "linkedInUrl": "http://example.com",
            "companyUrl": "http://example.com",
        },
    )
    assert response.status_code == 200