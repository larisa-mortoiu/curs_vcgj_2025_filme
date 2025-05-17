import pytest
import filme  # aplicația ta Flask

@pytest.fixture
def client():
    return filme.app.test_client()

# --------------------------------
# Pagina Acasă (/)
# --------------------------------
def test_acasa_status(client):
    response = client.get('/')
    assert response.status_code == 200

def test_acasa_text(client):
    response = client.get('/')
    assert b"Bine ai venit" in response.data

# --------------------------------
# Pagina Despre (/suits)
# --------------------------------
def test_suits_status(client):
    response = client.get('/suits')
    assert response.status_code == 200

def test_suits_text(client):
    response = client.get('/suits')
    assert b"<h1>Suits</h1>" in response.data

# --------------------------------
# Pagina Descriere (/suits/descriere)
# --------------------------------
def test_descriere_status(client):
    response = client.get('/suits/descriere')
    assert response.status_code == 200

def test_descriere_text(client):
    response = client.get('/suits/descriere')
    assert b"Mike Ross" in response.data

# --------------------------------
# Pagina Personaje (/suits/personaje)
# --------------------------------
def test_personaje_status(client):
    response = client.get('/suits/personaje')
    assert response.status_code == 200

def test_personaje_text(client):
    response = client.get('/suits/personaje')
    assert b"Harvey Specter" in response.data
    assert b"Mike Ross" in response.data
# --------------------------------
# Pagina Trailer (/suits/trailer)
# --------------------------------
def test_trailer_status(client):
    response = client.get('/suits/trailer')
    assert response.status_code == 200

def test_trailer_embed(client):
    response = client.get('/suits/trailer')
    assert b"youtube.com" in response.data

# --------------------------------
# Pagina Recenzii (/suits/recenzii)
# --------------------------------
def test_recenzii_status(client):
    response = client.get('/suits/recenzii')
    assert response.status_code == 200

def test_recenzii_text(client):
    response = client.get('/suits/recenzii')
    assert b"Recenzii ale fanilor" in response.data

