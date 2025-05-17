from filme import app

# =====================
# Teste pentru homepage
# =====================
def test_homepage_status():
    tester = app.test_client()
    response = tester.get('/')
    assert response.status_code == 200

# ============================
# Teste pentru /imitation-game
# ============================
def test_film_page_status():
    tester = app.test_client()
    response = tester.get('/imitation-game')
    assert response.status_code == 200

def test_film_page_content():
    tester = app.test_client()
    response = tester.get('/imitation-game')
    assert b"The Imitation Game" in response.data

# =============================
# Teste pentru atribut: descriere
# =============================
def test_descriere_status():
    tester = app.test_client()
    response = tester.get('/imitation-game/descriere')
    assert response.status_code == 200

def test_descriere_content():
    tester = app.test_client()
    response = tester.get('/imitation-game/descriere')
    assert b"Turing" in response.data or b"Enigma" in response.data

# ============================
# Teste pentru atribut: actori
# ============================
def test_actori_status():
    tester = app.test_client()
    response = tester.get('/imitation-game/actori')
    assert response.status_code == 200

def test_actori_content():
    tester = app.test_client()
    response = tester.get('/imitation-game/actori')
    assert b"Benedict Cumberbatch" in response.data or b"Keira Knightley" in response.data

# =========================
# Test pentru pagina trailer
# =========================
def test_trailer_status():
    tester = app.test_client()
    response = tester.get('/imitation-game/trailer')
    assert response.status_code == 200

def test_trailer_embed_code():
    tester = app.test_client()
    response = tester.get('/imitation-game/trailer')
    assert b"youtube.com" in response.data
