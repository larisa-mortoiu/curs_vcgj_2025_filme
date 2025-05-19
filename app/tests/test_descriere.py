"""Unit tests for the get_descriere_dark function."""

from app.lib.descriere import get_descriere_dark

def test_descriere_contine_cuvantul_dark():
    """Checks if the description contains the word 'Dark'."""
    assert "Dark" in get_descriere_dark(), "\nDescrierea nu contine cuvantul 'Dark'."
    print("\nCuvantul 'Dark' se regaseste in descriere.")

def test_descriere_are_cel_putin_10_cuvinte():
    """Ensures the description has at least 10 words."""
    len_cuvinte = len(get_descriere_dark().split())
    assert len_cuvinte >= 10, f"\nDescrierea are doar {len_cuvinte} cuvinte (mai putin de 10)."
    print(f"\nDescrierea are mai mult de 10 cuvinte ({len_cuvinte}).")
