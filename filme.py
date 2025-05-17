from flask import Flask, render_template, url_for

import app.lib.biblioteca_filme as biblioteca

app = Flask(__name__)
app.config["TEMPLATES_AUTO_RELOAD"] = True
app.config["TESTING"] = True

@app.route('/')
def index():
    return render_template('homepage.html')

@app.route('/hot_fuzz', methods=['GET'])
def hot_fuzz():
    return render_template('hot_fuzz.html')

@app.route('/hot_fuzz/description', methods=['GET'])
def hot_fuzz_description():
    description = biblioteca.descriere_hotfuzz()
    return render_template('hot_fuzz_description.html', description = description)

@app.route('/hot_fuzz/cast', methods=['GET'])
def hot_fuzz_cast():
    cast = biblioteca.distributie_hotfuzz()
    return render_template('hot_fuzz_cast.html', cast = cast)

if __name__ == '__main__':
    app.run(debug=True)
