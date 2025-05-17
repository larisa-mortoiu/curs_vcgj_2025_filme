import pytest
from filme import app

@pytest.fixture
def client():
    app.config['TESTING'] = True
    return app.test_client()

def test_homepage(client):
    response = client.get('/')
    assert response.status_code == 200
    assert b"Suits" in response.data

def test_suits_page(client):
    response = client.get('/suits')
    assert response.status_code == 200
    assert b"Suits" in response.data

def test_descriere_page(client):
    response = client.get('/suits/descriere')
    assert response.status_code == 200
    assert b"Mike Ross" in response.data

def test_personaje_page(client):
    response = client.get('/suits/personaje')
    assert response.status_code == 200
    assert b"Harvey Specter" in response.data

def test_trailer_page(client):
    response = client.get('/suits/trailer')
    assert response.status_code == 200
    assert b"iframe" in response.data

