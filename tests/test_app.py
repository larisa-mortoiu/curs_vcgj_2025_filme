def test_home_route():
    from filme import app
    with app.test_client() as client:
        response = client.get('/')
        assert response.status_code == 200

def test_actori_route():
    from filme import app
    with app.test_client() as client:
        response = client.get('/actori')
        assert response.status_code == 200
