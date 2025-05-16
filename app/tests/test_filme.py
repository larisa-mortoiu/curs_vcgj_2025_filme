import sys, os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../..')))
from app.lib.the_prestige_cast import get_actori

import pytest
import logging
from app.lib.the_prestige_cast import get_actori
from app.lib.the_prestige_description import get_descriere

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


def test_descriere_is_string_and_not_empty():
    descriere = get_descriere()
    assert isinstance(descriere, str), "Descrierea trebuie să fie un string."
    assert descriere.strip(), "Descrierea nu trebuie să fie goală."
    assert len(descriere) > 200, "Descrierea este prea scurtă."
    logger.info("Descrierea este validă ca tip și lungime.")

def test_descriere_keywords():
    descriere = get_descriere().lower()
    keywords = ["thriller", "magicieni", "sacrificiu", "iluzie", "rivalitate", "trucuri"]
    for word in keywords:
        assert word in descriere, f"Cuvântul cheie lipsă în descriere: {word}"
    logger.info("Descrierea conține cuvintele cheie importante.")


def test_actor_list_format():
    actori = get_actori()
    assert isinstance(actori, list), "Actori nu este o listă."
    assert len(actori) >= 7, "Lista de actori este prea scurtă."

    for actor in actori:
        assert isinstance(actor, str), f"Actorul nu este un string: {actor}"
        assert actor.strip(), f"Actorul este gol sau conține doar spații: {actor}"
        assert len(actor.split()) >= 2, f"Numele actorului pare incomplet: {actor}"
    
    logger.info("Lista de actori este validă și bine formată.")


def test_actor_presence():
    actori = get_actori()
    required = {"Christian Bale",
        "Hugh Jackman",
        "David Bowie",
        "Piper Perabo",
        "Rebecca Hall",
        "Scarlett Johansson",
        "Michael Caine"}
    assert required.issubset(set(actori)), "Unul sau mai mulți actori esențiali lipsesc."
    logger.info("Actorii principali sunt prezenți în listă.")

