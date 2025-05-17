from flask import Flask, render_template, url_for
from app.lib.jojo_cast import characters
from app.lib.jojo_description import descriptions

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/trailers')
def trailers():
    return render_template('jojo.html')

@app.route('/cast')
def cast():
    return render_template('jojo_cast.html', characters=characters)

@app.route('/character/<name>')
def character_details(name):
    # Find the character data
    character_data = None
    for character in characters:
        if character['name'].lower().replace(' ', '-') == name.lower():
            character_data = character
            break
    
    # Find the description data
    description_data = None
    if character_data:
        for description in descriptions:
            if description['name'] == character_data['name']:
                description_data = description
                break
    
    return render_template('jojo_description.html', 
                           character=character_data, 
                           description=description_data)

if __name__ == '__main__':
    app.run(debug=True)

