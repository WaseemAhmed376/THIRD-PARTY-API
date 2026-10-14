from fastapi.testclient import TestClient

from main import app

client = TestClient(app)


def test_get_all_posts():

    response = client.get("/posts")

    assert response.status_code == 200

    data = response.json()

    assert isinstance(data, list)

    assert len(data) > 0