import pytest
from app import app

@pytest.fixture
def client():
    with app.test_client() as c:
        yield c

def test_health(client):
    resp = client.get('/api/health')
    assert resp.status_code == 200
    data = resp.get_json()
    assert data['status'] == 'healthy'

def test_data(client):
    resp = client.get('/api/data')
    assert resp.status_code == 200
    json = resp.get_json()
    assert 'banner' in json and 'volume' in json
