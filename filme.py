from flask import Flask, render_template
from livereload import Server
import app.lib.descriere as descriere_st
import app.lib.distributie as distributie_st


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
    descriere=descriere_st.get_descriere()
    return render_template('descriere.html', descriere=descriere)

@app.route('/distributie')
def distributie():
    distributie=distributie_st.get_distributie()
    return render_template('distributie.html', distributie=distributie)















if __name__ == '__main__':
    server = Server(app.wsgi_app)
    server.serve(port=5011, debug=True)