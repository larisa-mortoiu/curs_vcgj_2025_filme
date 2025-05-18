from flask import Flask, render_template, url_for
from app.lib.descriere import get_descriere
from app.lib.actori import get_actori

app = Flask(__name__, static_url_path='/static')

@app.route('/')
def home():
    return render_template("home.html")

@app.route('/dexter')
def dexter():
    return render_template("dexter.html")

@app.route('/dexter/descriere')
def descriere():
    return render_template("descriere.html", descriere=get_descriere())

@app.route('/dexter/actori')
def actori():
    return render_template("actori.html", actori=get_actori())

if __name__ == '__main__':
    app.run(debug=True)

