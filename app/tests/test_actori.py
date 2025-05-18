"""Unit tests for the get_actori_dark function."""

from app.lib.actori import get_actori_dark

def test_actor_principal_in_lista():
    """Checks if Louis Hofmann is in the actor list."""
    assert "Louis Hofmann" in get_actori_dark()

def test_numar_minim_actori():
    """Ensures there are at least 3 actors in the list."""
    assert len(get_actori_dark()) >= 3
