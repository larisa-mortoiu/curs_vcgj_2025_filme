import pytest
import logging
import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../..')))

from filme import app
import app.lib.descriere as bm_description
import app.lib.actori as bm_cast

@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_bob_marley_description(client):
    response = client.get('/descriere')
    html_description = response.data.decode()

    def normalize(text):
        return ' '.join(text.split())

    description_from_html = normalize(html_description)
    description_expected = normalize(bm_description.get_description())

    if response.status_code == 200:
        logging.info("Descrierea filmului a fost găsită cu succes.")
        assert True
    else:
        logging.error(f"Descrierea filmului nu a fost găsită. Status code: {response.status_code}")
        assert False

    if description_expected in description_from_html:
        logging.info("Descrierea filmului este corectă.")
        assert True
    else:
        logging.error("Descrierea filmului nu este corectă.")
        assert False

def test_bob_marley_cast(client):
    response = client.get('/actori')
    html_cast = response.data.decode()

    def normalize(text):
        return ' '.join(text.split())

    cast_from_html = normalize(html_cast)
    cast_expected = normalize(bm_cast.get_cast())

    if response.status_code == 200:
        logging.info("Distribuția filmului a fost găsită cu succes.")
        assert True
    else:
        logging.error(f"Distribuția filmului nu a fost găsită. Status code: {response.status_code}")
        assert False

    if cast_expected in cast_from_html:
        logging.info("Distribuția filmului este corectă.")
        assert True
    else:
        logging.error("Distribuția filmului nu este corectă.")
        assert False

