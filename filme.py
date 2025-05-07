from flask import Flask, render_template
from livereload import Server


app = Flask(__name__)
app.config["TEMPLATES_AUTO_RELOAD"] = True
app.config["TESTING"] = True

@app.route('/')
def index():
    return render_template('home.html')

@app.route('/serial_home') 
def serial_home():
    return render_template('serial_home.html')
@app.route('/descriere')
def descriere():
    return render_template('descriere.html')

@app.route('/distributie')
def distributie():
    return render_template('distributie.html')















if __name__ == '__main__':
    server = Server(app.wsgi_app)
    server.serve(port=5011, debug=True)