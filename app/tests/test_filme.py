from filme import app

def test_home_status_code():
    tester = app.test_client()
    response = tester.get('/')
    assert response.status_code == 200

def test_dexter_page_content():
    tester = app.test_client()
    response = tester.get('/dexter')
    assert b"Dexter" in response.data
