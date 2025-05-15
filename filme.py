from flask import Flask, render_template, url_for 
from livereload import Server
import app.lib.curious_case_description as curious_case_description
import app.lib.curious_case_cast as curious_case_cast

app = Flask(__name__)
app.config["TEMPLATES_AUTO_RELOAD"] = True
app.config["TESTING"] = True

@app.route('/')
def index():
    return render_template('homepage.html')

@app.route('/curious_case', methods=['GET'])
def curious_case():
    return render_template('curious_case.html')

@app.route('/curious_case/description', methods=['GET'])
def show_curious_case_description():
    description = curious_case_description.get_description()
    return render_template('curious_case_description.html', description = description)

@app.route('/curious_case/cast', methods=['GET'])
def show_curious_case_cast():
    cast = curious_case_cast.get_cast()
    return render_template('curious_case_cast.html', cast = cast)

if __name__ == '__main__':
    server = Server(app.wsgi_app)
    server.serve(host='0.0.0.0', port=5011, debug=True)