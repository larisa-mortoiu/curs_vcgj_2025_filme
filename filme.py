from flask import Flask, render_template, send_from_directory
from app.lib.description import get_description
from app.lib.cast import get_cast

app = Flask(__name__, static_folder='static', template_folder='templates')

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/description')
def description():
    movie = get_description()
    return render_template('description.html', movie=movie)

@app.route('/cast')
def cast():
    cast_list = get_cast()
    return render_template("cast.html", cast=cast_list)

# Optional: route to serve static files (images, styles)
@app.route('/static/<path:filename>')
def static_files(filename):
    return send_from_directory('static', filename)

if __name__ == '__main__':
    app.run(debug=True)

