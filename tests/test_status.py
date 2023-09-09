from fastapi.testclient import TestClient
from crypto_data_provider.main import app
from crypto_data_provider.settings import settings


def test_answer():
    client = TestClient(app)
    result = client.get(settings.main_url)
    assert result.status_code == 200
    assert result.json() == {"status": "ok"}