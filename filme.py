from flask import Flask, render_template, url_for
from livereload import Server

app = Flask(__name__)
app.config["TEMPLATES_AUTO_RELOAD"] = True
app.config["TESTING"] = True

@app.route('/')
def index():
    return render_template('homepage.html')
    
@app.route('/prestige', methods=['GET'])
def prestige():
    return render_template('the_prestige.html')
    
if __name__ == "__main__":
    server = Server(app.wsgi_app)
    server.serve(debug=True)
