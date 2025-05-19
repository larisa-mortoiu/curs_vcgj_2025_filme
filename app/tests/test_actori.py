"""Unit tests for the get_actori_dark function."""

from app.lib.actori import get_actori_dark

def test_actor_principal_in_lista():
    """Checks if Louis Hofmann is in the actor list."""
    actor_names = [actor["nume"] for actor in get_actori_dark()]
    assert "Louis Hofmann" in actor_names, "\nLouis Hofmann nu se afla în lista actorilor."
    print("\nLouis Hofmann este in lista actorilor.") #daca assert returneaza True

def test_numar_minim_actori():
    """Ensures there are at least 3 actors in the list."""
    nr_actori = len(get_actori_dark())
    assert nr_actori >= 3, f"\nLista actorilor are doar {nr_actori} elemente (mai putin de 3)."
    print(f"\nLista actorilor contine {nr_actori} actori.")
