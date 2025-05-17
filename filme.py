from flask import Flask, render_template, send_from_directory

app = Flask(__name__, static_folder='static', template_folder='templates')

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/description')
def description():
    return render_template('description.html')

@app.route('/cast')
def cast():
    return render_template('cast.html')

# Optional: route to serve static files (images, styles)
@app.route('/static/<path:filename>')
def static_files(filename):
    return send_from_directory('static', filename)

if __name__ == '__main__':
    app.run(debug=True)

