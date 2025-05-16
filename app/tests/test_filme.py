import pytest
import logging
import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../..')))

from filme import app
import app.lib.bridgerton_description as bridgerton_description
import app.lib.bridgerton_cast as bridgerton_cast

logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger("bridgerton_tests")

@pytest.fixture
def test_client():
    app.config.update({"TESTING": True})
    with app.test_client() as client:
        yield client

def test_description_paragraph_structure():
    text = bridgerton_description.get_description()
    
    paragrafe = [p.strip() for p in text.split("<p>") if p.strip()]
    assert len(paragrafe) >= 2, "Descrierea trebuie să conțină cel puțin două paragrafe valide."
    
    for p in paragrafe:
        assert len(p) > 30, f"Paragraful este prea scurt: {p[:30]}..."

    logger.info(f" Descrierea are {len(paragrafe)} paragrafe structurate.")

def test_description_open_tags():
    descriere = bridgerton_description.get_description()
    
    assert descriere.count("<p>") == descriere.count("</p>"), "Numărul de <p> și </p> nu este egal – descrierea are taguri HTML neînchise."
    
    logger.info(" Tagurile HTML <p> sunt echilibrate.")

def test_cast_image_extension_name():
    cast = bridgerton_cast.get_cast()
    extensii_permise = (".jpg", ".jpeg", ".png")

    for actor in cast:
        foto = actor["photo"]
        assert foto.endswith(extensii_permise), f"Imaginea are o extensie invalidă: {foto}"
        assert " " not in foto, f"Numele fișierului conține spații: {foto}"
        assert foto.lower() == foto, f"Numele fișierului ar trebui să fie lowercase: {foto}"

    logger.info(" Toate fișierele de imagine au nume și extensii valide.")

def test_cast_duplicates():
    cast = bridgerton_cast.get_cast()
    nume = [actor["name"] for actor in cast]
    duplicate = set(n for n in nume if nume.count(n) > 1)

    assert not duplicate, f"Nume duplicate în distribuție: {', '.join(duplicate)}"
    
    logger.info(" Distribuția nu conține nume duplicate.")
