from flask import Flask, render_template, url_for
from livereload import Server
import app.lib.bridgerton_description as bridgerton_description
import app.lib.bridgerton_cast as bridgerton_cast

app = Flask(__name__)
app.config["TEMPLATES_AUTO_RELOAD"] = True
app.config["TESTING"] = True

@app.route('/')
def index():
    return render_template('homepage.html')

@app.route('/bridgerton', methods=['GET'])
def bridgerton():
    return render_template('bridgerton.html')

@app.route('/bridgerton/description', methods=['GET'])
def show_bridgerton_description():
    description = bridgerton_description.get_description()
    return render_template('bridgerton_description.html', description = description)

@app.route('/bridgerton/cast', methods=['GET'])
def show_bridgerton_cast():
    cast = bridgerton_cast.get_cast()
    return render_template('bridgerton_cast.html', cast = cast)


if __name__ == '__main__':
    server = Server(app.wsgi_app)
    server.serve(host='0.0.0.0', port=5011, debug=True)