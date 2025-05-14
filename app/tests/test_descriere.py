from app.lib.descriere import get_descriere_dark

def test_descriere_contine_cuvantul_dark():
    assert "Dark" in get_descriere_dark()

def test_descriere_are_cel_putin_10_cuvinte():
    assert len(get_descriere_dark().split()) >= 10
