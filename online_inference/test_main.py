from fastapi.testclient import TestClient
import pytest

from main import app, load_model
from get_test_data import gen_valid_data, gen_invalid_data


client = TestClient(app)


@pytest.fixture(scope='session', autouse=True)
def initialize_model():
    load_model()


def test_predict_valid():
    data = gen_valid_data()
    response = client.post('/predict', json=data)
    assert response.status_code == 200
    assert (response.json() == {"condition": [0.0]} or response.json() == {"condition": [1.0]})


def test_predict_invalid():
    data = gen_invalid_data()
    response = client.post("/predict", json=data)
    assert response.status_code == 422


def test_predict_missing():
    data = gen_valid_data()
    data.pop("age")
    response = client.post("/predict", json=data)
    assert response.status_code == 422
    assert response.json()['detail'][0]['msg'] == 'field required'


def test_health_endpoint():
    response = client.get('/health')
    assert response.status_code == 200
    assert response.json() == 'Model is ready to work'
