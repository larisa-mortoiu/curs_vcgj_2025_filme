from filme import app

def test_homepage():
    client = app.test_client()
    response = client.get('/')
    assert response.status_code == 200
    assert b'Movies' in response.data

def test_description_page():
    client = app.test_client()
    response = client.get('/breaking-bad')
    assert response.status_code == 200

def test_characters_page():
    client = app.test_client()
    response = client.get('/breaking-bad/characters')
    assert response.status_code == 200

