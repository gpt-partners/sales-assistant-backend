from fastapi.testclient import TestClient
from llm.create_vito import VitoRequest

from .main import app

client = TestClient(app)

vr = VitoRequest(linked_in_url="", company_url="")


class MockOpenAI:
    def invoke(_text):
        return vr


def test_get_main(mocker):
    mocker.patch("llm.create_vito.llm", MockOpenAI)
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"status": "OK"}


def test_post_vito(mocker):
    mocker.patch("llm.create_vito.llm", MockOpenAI)
    response = client.post(
        "/vito",
        json={
            "linked_in_url": "http://example.com",
            "company_url": "http://example.com",
        },
    )
    assert response.status_code == 200
