from app.lib.actori import get_actori_dark

def test_actor_principal_in_lista():
    assert "Louis Hofmann" in get_actori_dark()

def test_numar_minim_actori():
    assert len(get_actori_dark()) >= 3
