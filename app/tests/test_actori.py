from app.lib import actori

def test_actori_este_string():
    rezultat = actori.get_actori()
    assert isinstance(rezultat, str)

def test_actori_contine_cumberbatch():
    rezultat = actori.get_actori().lower()
    assert "cumberbatch" in rezultat or "keira" in rezultat
