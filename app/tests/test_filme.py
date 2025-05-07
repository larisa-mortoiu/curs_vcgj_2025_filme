import pytest 
import logging
import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../..')))

from filme import app
import app.lib.descriere as descriere_film
import app.lib.cast as cast_film 


@pytest.fixture
def test_client():
    app.config['TESTING'] = True
    return app.test_client()


def clean_whitespace(text):
    return ' '.join(text.split())


def test_descriere_apare_corect(test_client):
    rezultat = test_client.get('/How-to-lose-a-guy-in-10-days-descriere')
    continut_html = rezultat.data.decode('utf-8')

    descriere_din_html = clean_whitespace(continut_html)
    descriere_asteptata = clean_whitespace(descriere_film.get_descriere())

    assert rezultat.status_code == 200, "Eroare la încărcarea paginii de descriere."
    assert descriere_asteptata in descriere_din_html, "Descrierea afișată nu corespunde cu cea definită în backend."

    logging.info("Descrierea a fost verificată cu succes.")


def test_cast_apare_corect(test_client):
    rezultat = test_client.get('/How-to-lose-a-guy-in-10-days-cast')  
    continut_html = rezultat.data.decode('utf-8')

    cast_din_html = clean_whitespace(continut_html)
    cast_asteptat = clean_whitespace(cast_film.get_cast())

    assert rezultat.status_code == 200, "Eroare la încărcarea paginii de cast."
    assert cast_asteptat in cast_din_html, "Castul afișat nu corespunde cu cel definit în backend."

    logging.info("Castul a fost verificat cu succes.")
    