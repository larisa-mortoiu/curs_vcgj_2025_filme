import pytest
import logging
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../..')))
from filme import app
import app.lib.dynasty_description as description_dy
import app.lib.dynasty_cast as cast_dy


@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client
    

def test_dynasty_description(client):
    response = client.get('/dynasty/description')
    html_description = response.data.decode()

    def normalize(text):
        return ' '.join(text.split())

    description_from_html = normalize(html_description)
    description_expected = normalize(description_dy.get_description())

    if response.status_code == 200:
        logging.info("Descrierea serialului a fost găsită cu succes.")
        assert True
    else:
        logging.error(f"Descrierea serialului nu a fost găsită. Status code: {response.status_code}")
        assert False

    if description_expected in description_from_html:
        logging.info("Descrierea serialului este corectă.")
        assert True
    else:
        logging.error("Descrierea serialului nu este corectă.")
        assert False

def test_dynasty_cast(client):
    response = client.get('/dynasty/cast')
    html_cast = response.data.decode()

    def normalize(text):
        return ' '.join(text.split())

    cast_from_html = normalize(html_cast)
    cast_expected = normalize(cast_dy.get_cast())

    if response.status_code == 200:
        logging.info("Distribuția serialului a fost găsită cu succes.")
        assert True
    else:
        logging.error(f"Distribuția serialului nu a fost găsită. Status code: {response.status_code}")
        assert False

    if cast_expected in cast_from_html:
        logging.info("Distribuția serialului este corectă.")
        assert True
    else:
        logging.error("Distribuția serialului nu este corectă.")
        assert False