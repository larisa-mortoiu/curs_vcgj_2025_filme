from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("pagina_principala.html")

@app.route("/actori")
def actori():
    return render_template("pagina_actori_utf8.html")

@app.route("/descriere")
def descriere():
    return render_template("pagina_descriere_film.html")

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=5000)

