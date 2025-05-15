from flask import Flask, render_template
import app.lib.descriere as descriere_film
import app.lib.cast as cast_film 

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
    descriere=descriere_film.get_descriere()
    return render_template("descriere.html", descriere=descriere)

@app.route('/How-to-lose-a-guy-in-10-days-cast')
def film_cast():
    cast=cast_film.get_cast()
    return render_template("cast.html",cast=cast)

if __name__ == '__main__':
    app.run(debug=True)






























