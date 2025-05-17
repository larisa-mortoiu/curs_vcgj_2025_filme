from filme import app
import pytest
import logging
import sys
import os
import app.lib.biblioteca_filme as biblioteca
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../..')))

@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_hotfuzz(client):
    response = client.get('/hot_fuzz')

    assert response.status_code == 200, "Eroare la încărcarea paginii de descriere."

    logging.info("Descrierea a fost verificată cu succes.")

def test_descriere_hotfuzz(client):

    description = biblioteca.descriere_hotfuzz()

    assert isinstance(description, str), "Descrierea nu e string."

    response = client.get('/hot_fuzz/descriere')

    assert response.status_code == 200, "Serverul nu răspunde"

    assert "Nicholas Angel este cel mai bun ofițer de poliție din Londra" in description, "descrierea nu conține ce trebuie"
    
    logger.info("Test descriere trecut")
    
    
def test_distributie_hotfuzz(client):

    cast = biblioteca.distributie_hotfuzz()
    
    assert isinstance(cast, list), "Distribuția nu este listă."

    response = client.get('/hot_fuzz/distributie')

    assert response.status_code == 200, "Serverul nu răspunde"
    
    for character in cast:
        assert "actor" in character "Câmpul actor lipsește pentru unul dintre personaje"

    logger.info("Test distribuție trecut")
