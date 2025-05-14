from flask import Flask
from app.lib.descriere import get_descriere_dark
from app.lib.actori import get_actori_dark

app = Flask(__name__)

@app.route('/')
def homepage():
    return '''
        <h1>Filme/Seriale</h1>
        <p>Proiect realizat pentru cursul de Sisteme Cloud și Containerizare</p>
        <a href="/dark">Dark</a>
    '''

@app.route('/dark')
def pagina_dark():
    return '''
        <h1>Dark</h1>
        <p>Un serial misterios despre călătoria în timp.</p>
        <a href="/dark/descriere">Descriere</a> | <a href="/dark/actori">Actori</a>
    '''

@app.route('/dark/descriere')
def descriere():
    return f"<p>{get_descriere_dark()}</p>"

@app.route('/dark/actori')
def actori():
    actori = get_actori_dark()
    return "<ul>" + "".join(f"<li>{actor}</li>" for actor in actori) + "</ul>"


if __name__ == "__main__":
    app.run(debug=True)
