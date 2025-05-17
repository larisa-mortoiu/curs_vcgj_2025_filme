from filme import app
from app.lib.trailers import get_trailers

def test_homepage():
    client = app.test_client()
    response = client.get('/')
    assert response.status_code == 200
    assert b'<title>Breaking Bad</title>' in response.data

def test_description_page():
    client = app.test_client()
    response = client.get('/breaking-bad')
    assert response.status_code == 200

def test_characters_page():
    client = app.test_client()
    response = client.get('/breaking-bad/characters')
    assert response.status_code == 200

def test_trailers_structure():
    trailers = get_trailers()
    assert isinstance(trailers, list), "Expected a list of trailers"

    for trailer in trailers:
        assert "title" in trailer, "Trailer must have a 'title'"
        assert "src" in trailer, "Trailer must have a 'src'"
        assert trailer["src"].startswith("https://www.imdb.com/video/embed/"), "Invalid trailer source URL"


