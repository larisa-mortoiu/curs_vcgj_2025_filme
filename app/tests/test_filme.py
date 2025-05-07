import pytest
import sys
import os
import logging

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../..')))

from filme import app
import app.lib.descriere as descriere_st
import app.lib.distributie as distributie_st

@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as c:
        yield c


def test_descriere_st(client):
    response = client.get('/descriere')
    assert response.status_code == 200

    content = ' '.join(response.data.decode().split())
    expected = ' '.join(descriere_st.get_descriere().split())

    if expected in content:
        logging.info("Testul pentru descriere a trecut cu succes!")
        assert True
    else:
        logging.error("Conținutul descrierii nu se regăsește în răspuns!")
        assert False

def test_distributie_st(client):
    response = client.get('/distributie')
    assert response.status_code == 200

    content = ' '.join(response.data.decode().split())
    expected = ' '.join(distributie_st.get_distributie().split())

    if expected in content:
        logging.info("Testul pentru distributie a trecut cu succes!")
        assert True
    else:
        logging.error("Conținutul distributiei nu se regăsește în răspuns!")
        assert False