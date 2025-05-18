"""Aplicatia principala"""
from flask import Flask, render_template
from app.lib.actori import get_actori
from app.lib.descriere import get_descriere
from app.lib.trailer import get_trailer_info


app = Flask(__name__)

@app.route('/')
def home():
    """Ruta paginii principale"""
    return render_template('index.html')

@app.route('/descriere')
def descriere():
    """Ruta paginii descriere"""
    text_descriere = get_descriere()
    return render_template('descriere.html', descriere=text_descriere)

@app.route('/actori')
def actori():
    """Ruta paginii actori"""
    lista_actori = get_actori()
    return render_template('actori.html', actori=lista_actori)

@app.route('/trailer')
def trailer():
    """Ruta paginii trailer"""
    trailer_data = get_trailer_info()
    return render_template('trailer.html', trailer=trailer_data)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
