from flask import Flask, render_template, url_for
from livereload import Server
from app.lib.cars_descriere import get_movie_description
from app.lib.cars_actori import get_actor_names
import os
from app.lib.cars_actori import get_actor_names

app = Flask(__name__)
app.config["TEMPLATES_AUTO_RELOAD"] = True
app.config["TESTING"] = True

@app.route('/')
def index():
    return render_template('home_cars.html')

@app.route('/descriere')
def show_description():
    descriere = get_movie_description()
    return render_template('descriere_cars.html', descriere_text=descriere)

@app.route('/cars2006')
def cars_2006():
    return render_template('cars_2006.html')


@app.route('/cast')
def show_cast():
    image_dir = os.path.join(app.static_folder, 'images')
    actor_images = [
        f for f in os.listdir(image_dir)
        if f.lower().endswith(('.jpg', '.jpeg', '.png')) and 'descriere' not in f.lower()
    ]
    actor_names = get_actor_names().split(", ")
    return render_template("cast_cars.html", actor_images=actor_images, actor_names=actor_names)


if __name__ == "__main__":
    server = Server(app.wsgi_app)
    server.serve(host='0.0.0.0', port=5000, debug=True)
