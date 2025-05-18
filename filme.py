from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('PaginaPrincipala.html')

@app.route('/cast')
def cast():
    return render_template('Cast.html')

@app.route('/descriere')
def descriere():
    return render_template('Descriere.html')

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000, debug=True)
