
import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
import pytest
from app import create_app
from app.config import TestConfig
from unittest.mock import patch
from app.db.db_utils import db

@pytest.fixture
def client(app):
    return app.test_client()
 
@patch('app.main.routes.Article.query')
def test_index_page(mock_query, client):
    mock_query.order_by.return_value.limit.return_value.all.return_value = []
    response = client.get('/')
    assert response.status_code == 200
    assert b'Charles Ugwute Ogbonna' in response.data or b'Articles' in response.data

def test_about_page(client):
    response = client.get('/about')
    assert response.status_code == 200
    assert b'About' in response.data or b'Team' in response.data
