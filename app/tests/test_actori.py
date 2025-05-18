from app.lib.actori import get_actori

def test_primul_actor():
    actori = get_actori()
    assert actori[0]["nume"] == "Michael C. Hall"

