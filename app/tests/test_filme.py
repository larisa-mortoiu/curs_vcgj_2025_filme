import pytest
from filme import app

@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

# 1. Test homepage
def test_homepage(client):
    response = client.get('/')
    assert response.status_code == 200
    assert b"Bine ai venit" in response.data

# 2. Test pagina filmului Shrek
def test_pagina_shrek(client):
    response = client.get('/shrek')
    assert response.status_code == 200
    assert b"Despre filmul Shrek" in response.data

# 3. Test descriere - status
def test_descriere_status(client):
    response = client.get('/shrek/descriere')
    assert response.status_code == 200

# 4. Test descriere - conținut
def test_descriere_content(client):
    response = client.get('/shrek/descriere')
    html = response.data.decode('utf-8')  # Decodificăm din bytes în string
    assert "căpcăun verde" in html or "Shrek este un" in html

# 5. Test personaje - status
def test_personaje_status(client):
    response = client.get('/shrek/personaje')
    assert response.status_code == 200

# 6. Test personaje - conținut
def test_personaje_content(client):
    response = client.get('/shrek/personaje')
    html = response.data.decode('utf-8')  # Decodificăm din bytes în string
    assert "Donkey" in html
    assert "Fiona" in html

# 7. Test trailer - status
def test_trailer_status(client):
    response = client.get('/shrek/trailer')
    assert response.status_code == 200

# 8. Test trailer - iframe embedded
def test_trailer_iframe(client):
    response = client.get('/shrek/trailer')
    html = response.data.decode('utf-8')  # Decodificăm din bytes în string
    assert "iframe" in html
