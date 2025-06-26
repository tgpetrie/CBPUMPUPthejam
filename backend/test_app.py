import pytest
from app import create_app
from unittest.mock import patch

@pytest.fixture
def client():
    app = create_app()
    app.config["TESTING"] = True
    return app.test_client()

def test_health(client):
    resp = client.get("/api/health")
    data = resp.get_json()
    assert resp.status_code == 200
    assert data["status"] == "ok"

@patch('app.fetch_top_movers_1h')
@patch('app.fetch_top_by_volume_24h')
@patch('app.get_mock_gainers_losers')
def test_data(mock_get_gainers_losers, mock_fetch_volume, mock_fetch_banner, client):
    # Setup mock return values
    mock_fetch_banner.return_value = [
        {'symbol': 'BTC-USD', 'current_price': 65000, 'price_change_1h': 1.5}
    ]
    mock_fetch_volume.return_value = [
        {'symbol': 'ETH-USD', 'current_price': 3500, 'volume_24h': 5000000000}
    ]
    mock_get_gainers_losers.return_value = {
        'gainers': [{'id': 'SOL-USD', 'change_3m': '5.00', 'url': '...'}],
        'losers': [{'id': 'XRP-USD', 'change_3m': '-3.00', 'url': '...'}]
    }

    resp = client.get("/api/data")
    js = resp.get_json()

    assert resp.status_code == 200
    assert "banner" in js
    assert "volume" in js
    assert "gainers" in js
    assert "losers" in js

    assert len(js['banner']) == 1
    assert js['banner'][0]['id'] == 'BTC-USD'
    assert js['banner'][0]['change_1h'] == '1.50'

    assert len(js['volume']) == 1
    assert js['volume'][0]['id'] == 'ETH-USD'
    assert js['volume'][0]['volume_24h'] == 5000000000

    assert len(js['gainers']) == 1
    assert js['gainers'][0]['id'] == 'SOL-USD'

    assert len(js['losers']) == 1
    assert js['losers'][0]['id'] == 'XRP-USD'