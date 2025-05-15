import pytest
import logging
import sys
import os

logging.basicConfig(level=logging.INFO, format="%(asctime)s [%(levelname)s]  %(message)s")

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../..')))

from filme import app
import app.lib.curious_case_description as description_c
import app.lib.curious_case_cast as cast_c

@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_curious_case_description(client):
    response = client.get('/curious_case/description')
    html_description = response.data.decode()

    def normalize(text):
        return ' '.join(text.split())

    description_from_html = normalize(html_description)
    description_expected = normalize(description_c.get_description())

    if response.status_code == 200:
        logging.info("Pagina de descriere a fost încărcată cu succes.")
    else:
        logging.error(f"Eroare la încărcarea paginii de descriere. Status: {response.status_code}")
    assert response.status_code == 200

    keywords = [
        "The Curious Case of Benjamin Button",
        "Brad Pitt",
        "Cate Blanchett",
        "David Fincher"
    ]

    for keyword in keywords:
        if keyword.lower() in description_from_html.lower():
            logging.info(f"Keyword găsit în descriere: {keyword}")
        else:
            logging.error(f"Lipsește keyword în descriere: {keyword}")
        assert keyword.lower() in description_from_html.lower()

    if description_expected in description_from_html:
        logging.info("Descrierea completă a fost regăsită în HTML.")
    else:
        logging.error("Descrierea generată nu apare corect în pagină.")
    assert description_expected in description_from_html


def test_curious_case_cast(client):
    response = client.get('/curious_case/cast')
    html_cast = response.data.decode()

    if response.status_code == 200:
        logging.info("Pagina de distribuție a fost încărcată cu succes.")
    else:
        logging.error(f"Eroare la încărcarea paginii de distribuție. Status: {response.status_code}")
    assert response.status_code == 200

    cast = cast_c.get_cast()

    for actor in cast:
        if actor['name'] in html_cast:
            logging.info(f"Actor găsit în HTML: {actor['name']}")
        else:
            logging.error(f"Lipsește actor în HTML: {actor['name']}")
        assert actor['name'] in html_cast

        if actor['character'] in html_cast:
            logging.info(f"Personaj găsit în HTML: {actor['character']}")
        else:
            logging.error(f"Lipsește personaj în HTML: {actor['character']}")
        assert actor['character'] in html_cast
