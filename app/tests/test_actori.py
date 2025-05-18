from app.lib.actori import actori_twilight

def test_actori_not_empty():
    result = actori_twilight()
    assert result.strip() != ""

def test_main_actors_present():
    result = actori_twilight().lower()
    assert "kristen stewart" in result
    assert "robert pattinson" in result
    assert "taylor lautner" in result
