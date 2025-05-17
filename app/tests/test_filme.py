import os
import sys
import pytest

# so pytest can find filme.py in the project root
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../../')))

from filme import app as flask_app
from app.lib.jojo_cast import characters

@pytest.fixture
def client():
    flask_app.config['TESTING'] = True
    with flask_app.test_client() as client:
        yield client

def test_homepage(client):
    resp = client.get('/')
    assert resp.status_code == 200
    # check for some expected snippet in home.html
    assert b"JoJo's Bizarre Adventure" in resp.data

def test_trailers_page(client):
    resp = client.get('/trailers')
    assert resp.status_code == 200
    # e.g. your jojo.html has an <iframe> or heading “Trailers”
    assert b"Trailer" in resp.data or b"iframe" in resp.data

def test_cast_page(client):
    resp = client.get('/cast')
    assert resp.status_code == 200
    # should list at least one character name
    first = characters[0]['name'].encode('utf-8')
    assert first in resp.data

def test_character_detail(client):
    # pick the first character from your data
    name = characters[0]['name']
    slug = name.lower().replace(' ', '-')
    resp = client.get(f'/character/{slug}')
    assert resp.status_code == 200
    # page should contain that character’s name
    assert name.encode('utf-8') in resp.data

