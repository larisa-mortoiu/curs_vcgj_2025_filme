"""This file defines the Flask application for the Dark series."""

from flask import Flask, render_template
from app.lib.descriere import get_descriere_dark
from app.lib.actori import get_actori_dark

app = Flask(__name__)

@app.route('/')
def homepage():
    """Displays the homepage with the movie selection."""
    return render_template("index.html")

@app.route('/dark')
def pagina_dark():
    """Returns the main Dark page."""
    return render_template("dark.html")

@app.route('/dark/descriere')
def descriere():
    """Returns the detailed description of the series."""
    descriere_text = get_descriere_dark()
    return render_template("descriere.html", descriere=descriere_text)

@app.route('/dark/actori')
def actori():
    """Returns the list of main actors with images and roles."""
    lista_actori = get_actori_dark()
    return render_template("actori.html", actori=lista_actori)


if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)
