from flask import Flask, render_template, url_for
from livereload import Server
import app.lib.gentlemen_description as gentlemen_description
import app.lib.gentlemen_cast as gentlemen_cast

app = Flask(__name__)
app.config["TEMPLATES_AUTO_RELOAD"] = True
app.config["TESTING"] = True

@app.route('/')
def index():
    return render_template('homepage.html')

@app.route('/gentlemen', methods=['GET'])
def gentlemen():
    return render_template('the_gentlemen.html')

@app.route('/gentlemen/description', methods=['GET'])
def show_gentlemen_description():
    description = gentlemen_description.get_description()
    return render_template('description.html', description = description)

@app.route('/gentlemen/cast', methods=['GET'])
def show_gentlemen_cast():
    cast = gentlemen_cast.get_cast()
    return render_template('cast.html', cast = cast)


if __name__ == '__main__':
    server = Server(app.wsgi_app)
    server.serve(port=5011, debug=True)