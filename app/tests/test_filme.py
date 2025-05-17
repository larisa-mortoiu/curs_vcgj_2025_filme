import sys
import os
import pytest

# Add the project root to sys.path so Python can find filme.py
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../../')))

from filme import app as flask_app  # Now this should work

@pytest.fixture
def client():
    flask_app.config['TESTING'] = True
    with flask_app.test_client() as client:
        yield client

def test_homepage(client):
    response = client.get('/')
    assert response.status_code == 200
    assert b'Ali G Indahouse' in response.data

def test_description_page(client):
    response = client.get('/description')
    assert response.status_code == 200

def test_cast_page(client):
    response = client.get('/cast')
    assert response.status_code == 200

