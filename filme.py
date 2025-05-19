from flask import Flask, render_template
from app.lib.descriere import get_description
from app.lib.actori import get_cast

app = Flask(__name__)

@app.route('/')
def home():
    return render_template("home.html")

@app.route('/film')
def film():
    return render_template("film.html")

@app.route('/descriere')
def descriere():
    return render_template("descriere.html", descriere=get_description())

@app.route('/actori')
def actori():
    return render_template("actori.html", actori_html=get_cast())

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)

