from flask import Flask, render_template
from app.lib.descriere import descriere_twilight
from app.lib.actori import actori_twilight

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/twilight')
def twilight():
    return render_template('twilight.html')

@app.route('/twilight/despre')
def despre():
    descriere = descriere_twilight()
    return render_template('despre.html', descriere=descriere)

@app.route('/twilight/actori')
def actori():
    actori = actori_twilight()
    return render_template('actori.html', actori=actori)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
