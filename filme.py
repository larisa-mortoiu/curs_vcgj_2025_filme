from flask import Flask, render_template, url_for


app = Flask(__name__)
@app.route('/')


def dynasty():
    return "<h1>Dynasty</h1>"

if __name__ == '__main__':
   app.run(debug=True)