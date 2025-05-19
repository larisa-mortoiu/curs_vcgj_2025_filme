from app.lib.descriere import descriere_twilight

def test_descriere_not_empty():
    result = descriere_twilight()
    assert result.strip() != ""

def test_descriere_has_keywords():
    result = descriere_twilight().lower()
    assert "bella" in result
    assert "vampire" in result
    assert "twilight" in result
