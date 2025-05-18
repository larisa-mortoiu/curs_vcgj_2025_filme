import pytest
from filme import app


@pytest.fixture

def test_index():
    client = app.test_client()
    response = client.get('/')
    assert response.status_code == 200
    assert b"Interstellar" in response.data  # pune aici ceva sigur în index.html

def test_descriere():
    client = app.test_client()
    response = client.get('/descriere')
    assert response.status_code == 200
    assert b"Descriere" in response.data  # adaptează după conținutul paginii

def test_actori():
    client = app.test_client()
    response = client.get('/actori')
    assert response.status_code == 200
    assert b"Actori" in response.data  # adaptează după conținut

def test_trailer():
    client = app.test_client()
    response = client.get('/trailer')
    assert response.status_code == 200
    assert b"Trailer" in response.data  # adaptează după conținut

