import pytest
import logging
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../..')))
from filme import app
import app.lib.gentlemen_description as gentlemen_description
import app.lib.gentlemen_cast as gentlemen_cast

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_gentlemen_description(client):
    description = gentlemen_description.get_description()

    assert isinstance(description, str), "Descrierea nu este un string."
    assert "The Gentlemen este un serial britanic elegant" in description, "Introducerea așteptată nu a fost găsită în descriere."
    assert "Eddie Horniman" in description, "Numele personajului principal lipsește din descriere."
    assert "<p>" in description, "Descrierea nu conține tag-ul HTML <p>; afișarea în browser ar putea fi incorectă."

    logger.info("Testul pentru descriere a trecut cu succes.")


def test_gentlemen_cast(client):
    cast = gentlemen_cast.get_cast()

    assert isinstance(cast, list), "Distribuția nu este o listă."
    assert len(cast) >= 10, f"Distribuția conține mai puțin de 10 membri ({len(cast)})."

    for actor in cast:
        assert "name" in actor and actor["name"], f"Câmpul 'name' lipsește sau este gol pentru un actor: {actor}"
        assert "character" in actor and actor["character"], f"Câmpul 'character' lipsește sau este gol pentru {actor.get('name')}"
        assert "photo" in actor and actor["photo"].endswith(".jpg"), f"Foto invalidă pentru {actor.get('name')}: {actor.get('photo')}"

    assert any(a["name"] == "Theo James" for a in cast), "Theo James nu apare în distribuție."
    assert any(a["character"] == "Eddie Horniman" for a in cast), "Personajul Eddie Horniman lipsește din distribuție."
    
    logger.info("Testul pentru distribuție a trecut cu succes.")