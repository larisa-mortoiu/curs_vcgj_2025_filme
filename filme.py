"""Main Flask app for the Breaking Bad web project."""
from flask import Flask, render_template
from app.lib.description import get_description_html
from app.lib.actors import get_actors_html
from app.lib.trailers import get_trailers

app = Flask(__name__)

@app.route('/')
def homepage():
    """Render the homepage with a banner and navigation to other sections."""
    return render_template('index.html')

@app.route('/breaking-bad')
def description():
    """Render the description page with a short summary of the series."""
    desc = get_description_html()
    return render_template('description.html', desc=desc)

@app.route('/breaking-bad/characters')
def characters():
    """Render the characters page showing the list of actors and their roles."""
    actors = get_actors_html()
    return render_template('characters.html', actors=actors)

@app.route('/breaking-bad/trailers')
def trailers():
    """Render the trailers page with embedded official videos."""
    trailer_list = get_trailers()
    return render_template('trailers.html', trailers=trailer_list)

if __name__ == '__main__':
    app.run(debug=True)
