
import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
import pytest
from app import create_app
from app.config import TestConfig

app = create_app(config_class=TestConfig)


@pytest.fixture
def client():
    app = create_app()
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_index_page(client):
    response = client.get('/')
    assert response.status_code == 200
    assert b'Charles Ugwute Ogbonna' in response.data or b'Articles' in response.data
 
def test_about_page(client):
    response = client.get('/about')
    assert response.status_code == 200
    assert b'About' in response.data or b'Team' in response.data
