from fastapi.testclient import (
    TestClient,
)

from apps.api.main import app


client = TestClient(app)