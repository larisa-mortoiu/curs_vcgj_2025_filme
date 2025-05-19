from app.lib.actori import actori_twilight

def test_actori_not_empty():
    result = actori_twilight()
    assert len(result) > 0

def test_main_actors_present():
    actors = actori_twilight()
    actor_names = [actor["name"].lower() for actor in actors]
    assert "kristen stewart" in actor_names
    assert "robert pattinson" in actor_names
    assert "taylor lautner" in actor_names
