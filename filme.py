from flask import Flask, render_template

app = Flask(__name__)
app.config["TEMPLATES_AUTO_RELOAD"] = True
app.config["TESTING"] = True

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/actors')
def actors():
    return render_template('actors.html')

@app.route('/description')
def description():
    return render_template('description.html')

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port = 5000)
