from flask import Flask, render_template
from livereload import Server

app = Flask(__name__)
app.config["TEMPLATES_AUTO_RELOAD"] = True
app.config["TESTING"] = True

@app.route('/')
def index():
    return render_template("home_film.html")


@app.route('/How-to-lose-a-guy-in-10-days')
def film():
    return render_template("film.html")

@app.route('/How-to-lose-a-guy-in-10-days-descriere')
def film_descriere():
    return render_template("descriere.html")

@app.route('/How-to-lose-a-guy-in-10-days-cast')
def film_cast():
    return render_template("cast.html")

if __name__ == '__main__':
    server = Server(app.wsgi_app)
    server.serve(port=5011, debug=True)






























