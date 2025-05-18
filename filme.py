"""This file defines the Flask application for the Dark series."""

from flask import Flask
from app.lib.descriere import get_descriere_dark
from app.lib.actori import get_actori_dark

app = Flask(__name__)

@app.route('/')
def homepage():
    """Returns the main menu of the application."""
    return '''
        <h1>Filme/Seriale</h1>
        <p>Proiect realizat pentru cursul de Sisteme Cloud și Containerizare</p>
        <a href="/dark">Dark</a>
    '''

@app.route('/dark')
def pagina_dark():
    """Returns the description app page of the series."""
    return '''
        <h1>Dark</h1>
        <p>Un serial misterios despre călătoria în timp.</p>
        <a href="/dark/descriere">Descriere</a> | <a href="/dark/actori">Actori</a>
    '''

@app.route('/dark/descriere')
def descriere():
    """Returns the description of the series."""
    return f"<p>{get_descriere_dark()}</p>"

@app.route('/dark/actori')
def actori():
    """Returns the list of main actors of the series."""
    lista_actori = get_actori_dark()
    return "<ul>" + "".join(f"<li>{actor}</li>" for actor in lista_actori) + "</ul>"


if __name__ == "__main__":
    app.run(debug=True)
