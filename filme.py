from flask import Flask, render_template
from app.lib.description import get_description_html
from app.lib.actors import get_actors_html
from app.lib.trailers import get_trailers

app = Flask(__name__)

@app.route('/')
def homepage():
    return render_template('index.html')

@app.route('/breaking-bad')
def description():
    description = get_description_html()
    return render_template('description.html', description=description)

@app.route('/breaking-bad/characters')
def characters():
    actors = get_actors_html()
    return render_template('characters.html', actors=actors)

@app.route('/breaking-bad/trailers')
def trailers():
    trailer_list = get_trailers()
    return render_template('trailers.html', trailers=trailer_list)

if __name__ == '__main__':
    app.run(debug=True)
