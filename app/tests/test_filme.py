import sys
import os
import pytest
import logging

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../..')))


from app.lib.actors import get_actors
from app.lib.description import get_description
from filme import app


logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def test_descriere_is_valid():
    descriere = get_description()
    assert isinstance(descriere, str), "Descrierea trebuie să fie un string."
    assert descriere.strip(), "Descrierea nu trebuie să fie goală."
    logger.info("Descrierea este validă.")

def test_get_actors():
    actors = get_actors()
    assert isinstance(actors, list), "Actorii trebuie să fie o listă."
    assert all(isinstance(a, str) and a.strip() for a in actors), "Toți actorii trebuie să fie stringuri non-goale."
    logger.info("Lista de actori este validă.")

@pytest.fixture
def client():
    app.config["TESTING"] = True
    with app.test_client() as client:
        yield client

def test_home_route(client):
    response = client.get("/")
    assert response.status_code == 200
    logger.info("Ruta / este funcțională.")

def test_descriere_route(client):
    response = client.get("/descriere")  # <-- corectat
    assert response.status_code == 200
    logger.info("Ruta /descriere este funcțională.")

def test_cast_route(client):
    response = client.get("/cast")  # <-- corectat
    assert response.status_code == 200
    logger.info("Ruta /cast este funcțională.")
