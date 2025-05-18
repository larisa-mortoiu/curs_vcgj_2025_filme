"""Unit tests for the get_descriere_dark function."""

from app.lib.descriere import get_descriere_dark

def test_descriere_contine_cuvantul_dark():
    """Checks if the description contains the word 'Dark'."""
    assert "Dark" in get_descriere_dark()

def test_descriere_are_cel_putin_10_cuvinte():
    """Ensures the description has at least 10 words."""
    assert len(get_descriere_dark().split()) >= 10
