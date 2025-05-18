import pytest
from filme import app
from app.lib.trailers import get_trailers

@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_homepage(client):
    """Verifică statusul și titlul paginii de start."""
    response = client.get('/')
    assert response.status_code == 200
    assert b'<title>Interstellar</title>' in response.data

def test_404_page(client):
    """Verifică răspunsul pentru o pagină inexistentă."""
    response = client.get('/pagina-inexistenta')
    assert response.status_code == 404

def test_trailers_structure():
    """Verifică structura și validitatea datelor din get_trailers()."""
    trailers = get_trailers()
    assert isinstance(trailers, list), "Expected a list of trailers"
    assert len(trailers) > 0, "Lista de trailere e goală"
    for trailer in trailers:
        assert "title" in trailer, "Trailer must have a 'title'"
        assert "src" in trailer, "Trailer must have a 'src'"
        assert trailer["src"].startswith("https://www.imdb.com/video/embed/"), "Invalid embed URL"

