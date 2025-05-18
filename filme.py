from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/descriere")
def descriere():
    return render_template("descriere.html")

@app.route("/actori")
def actori():
    return render_template("actori.html")

@app.route("/trailer")
def trailer():
    return render_template("trailer.html")

if __name__ == "__main__":
    app.run(debug=True)

