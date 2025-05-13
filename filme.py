from flask import Flask, render_template, url_for
import app.lib.dynasty_description as description_dy
import app.lib.dynasty_cast as cast_dy

app = Flask(__name__)
app.config["TEMPLATES_AUTO_RELOAD"] = True
app.config["TESTING"] = True

@app.route('/')
def index():
    return render_template('homepage.html')

@app.route('/dynasty', methods=['GET'])
def dynasty():
    return render_template('dynasty.html')

@app.route('/dynasty/description', methods=['GET'])
def dynasty_description():
    description = description_dy.get_description()
    return render_template('dynasty_description.html', description = description)

@app.route('/dynasty/cast', methods=['GET'])
def dynasty_cast():
    cast = cast_dy.get_cast()
    return render_template('dynasty_cast.html', cast = cast)


if __name__ == '__main__':
    app.run(debug=True)