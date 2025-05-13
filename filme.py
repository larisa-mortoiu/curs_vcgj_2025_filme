from flask import Flask, render_template, url_for
from livereload import Server
from app.lib.the_prestige_description import get_descriere
from app.lib.the_prestige_cast import get_actori

app = Flask(__name__)
app.config["TEMPLATES_AUTO_RELOAD"] = True
app.config["TESTING"] = True

@app.route('/')
def index():
    return render_template('homepage.html')

@app.route('/prestige', methods=['GET'])
def prestige():
    return render_template('the_prestige.html')

@app.route('/prestige/cast', methods=['GET'])
def the_prestige_cast():
    return render_template("the_prestige_cast.html", lista=get_actori())

@app.route('/prestige/description')
def the_prestige_description():
    return render_template("the_prestige_description.html", text=get_descriere())

if __name__ == "__main__":
    server = Server(app.wsgi_app)
    server.serve(debug=True)
