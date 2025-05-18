"""Unit tests for The Blacklist app routes and components."""
# pylint: disable=redefined-outer-name
import sys
import os
import pytest
from filme import app

# Adaugă directorul părinte (unde e filme.py) la sys.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../../')))


@pytest.fixture
def client():
    """Fixtură care oferă un client Flask pentru testare"""
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_home_page(client):
    """Testarea home page-ului"""
    response = client.get('/')
    assert response.status_code == 200
    assert b'The Blacklist' in response.data

def test_descriere_page(client):
    """Testarea pagini descrierii"""
    response = client.get('/descriere')
    assert response.status_code == 200
    assert b'Descriere' in response.data

def test_actori_page(client):
    """Testarea paginii actorilor si verificarea ca exista pozele in ea"""
    response = client.get('/actori')
    assert response.status_code == 200
    assert b'Actori Principali' in response.data

    # Verifică imaginile actorilor
    actor_images = [
        b'/static/images/james_spader.jpeg',
        b'/static/images/harry_lennix.jpeg',
        b'/static/images/megan_boone.jpeg',
        b'/static/images/diego_klattenhoff.jpeg',
        b'/static/images/ryan_eggold.jpeg',
	b'/static/images/mozhan_marno.jpeg'
    ]
    for img in actor_images:
        assert img in response.data

def test_trailer_page(client):
    """Testarea pagina trailerului"""
    response = client.get('/trailer')
    assert response.status_code == 200
    assert b'Trailer' in response.data
