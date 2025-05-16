from app.lib import descriere

def test_descriere_este_string():
    rezultat = descriere.get_descriere()
    assert isinstance(rezultat, str)

def test_descriere_contine_turing():
    rezultat = descriere.get_descriere().lower()
    assert "turing" in rezultat or "enigma" in rezultat
