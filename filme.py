from flask import Flask
from app.lib.biblioteca_shrek import descriere_personaj, replici_memorabile

app = Flask(__name__)

html_template = """
<!DOCTYPE html>
<html lang="ro">
<head>
    <meta charset="UTF-8">
    <title>{titlu}</title>
    <style>
        body {{
            font-family: 'Segoe UI', sans-serif;
            background-color: #2e4d35;
            margin: 0;
            padding: 0;
            color: #fffaf0;
        }}
        header {{
            background-color: #3a5f0b;
            padding: 20px;
            text-align: center;
        }}
        header h1 {{
            font-size: 44px;
            margin: 0;
            color: #ffffff;
        }}
        nav {{
            background-color: #4a633c;
            display: flex;
            justify-content: center;
            flex-wrap: wrap;
            gap: 15px;
            padding: 15px;
        }}
        nav form {{
            display: inline;
        }}
        button {{
            background-color: #8B4513;
            color: #fff;
            padding: 10px 18px;
            border: none;
            border-radius: 6px;
            cursor: pointer;
            font-size: 16px;
            font-weight: bold;
        }}
        button:hover {{
            background-color: #5c3317;
        }}
        .container {{
            background-color: #ffffff;
            color: #2c3e50;
            margin: 40px auto;
            padding: 30px;
            width: 85%;
            max-width: 850px;
            border-radius: 12px;
            box-shadow: 0 0 20px rgba(0,0,0,0.2);
            text-align: center;
        }}
        img {{
            max-width: 100%;
            height: auto;
            border-radius: 10px;
            margin: 20px 0;
        }}
        iframe {{
            width: 100%;
            max-width: 560px;
            height: 315px;
            border-radius: 10px;
        }}
        ul {{
            text-align: left;
            display: inline-block;
            font-size: 18px;
            margin-top: 20px;
        }}
        a {{
            display: inline-block;
            margin-top: 20px;
            text-decoration: none;
            color: #2980b9;
            font-weight: bold;
        }}
    </style>
</head>
<body>
    <header>
        <h1>Shrek</h1>
    </header>
    <nav>
        <form action="/"><button>Acasă</button></form>
        <form action="/shrek"><button>Despre</button></form>
        <form action="/shrek/descriere"><button>Descriere</button></form>
        <form action="/shrek/personaje"><button>Personaje</button></form>
        <form action="/shrek/trailer"><button>Trailer</button></form>
        <form action="/shrek/poveste"><button>Poveste</button></form>
        <form action="/shrek/replici"><button>Replici</button></form>
    </nav>
    <div class="container">
        {continut}
        <br><br>
        <form action="/"><button>Înapoi</button></form>
    </div>
</body>
</html>
"""

@app.route("/", methods=['GET'])
def pagina_principala():
    continut = """
    <h2>Bine ai venit în regatul lui Shrek!</h2>
    <p>
        Descoperă lumea amuzantă și emoționantă a celebrului căpcăun verde. 
        Shrek nu este un erou tipic, dar te va cuceri prin curaj, loialitate și umor inconfundabil.
        Explorează fiecare secțiune a site-ului pentru a afla mai multe despre povestea sa, personajele haioase și replicile care au rămas în istorie.
    </p>
    <img src="https://external-content.duckduckgo.com/iu/?u=https%3A%2F%2Fhappymag.tv%2Fwp-content%2Fuploads%2F2021%2F05%2Fshrek4_disneyscreencaps.com_675.0.jpg" alt="Shrek în mlaștină">
    """
    return html_template.format(titlu="Shrek - Acasă", continut=continut)

@app.route("/shrek", methods=['GET'])
def pagina_shrek():
    continut = """
    <h2>Despre filmul Shrek</h2>
    <p>
        Lansat în 2001, "Shrek" a fost primul film animat care a câștigat premiul Oscar pentru Cel mai bun film de animație.
        Cu un amestec unic de umor, emoție și satiră, filmul a redefinit genul animației.
        Seria a avut un impact cultural major, generând mai multe continuări și un număr imens de fani.
    </p>
    <img src="https://external-content.duckduckgo.com/iu/?u=https%3A%2F%2Feskipaper.com%2Fimages%2Fshrek-and-donkey-2.jpg" alt="Shrek și Donkey">
    """
    return html_template.format(titlu="Shrek", continut=continut)

@app.route("/shrek/descriere", methods=['GET'])
def descriere_shrek():
    continut = """
    <h2>Descriere generală</h2>
    <p>
        Shrek este o creație originală – un căpcăun cu suflet mare care își dorește doar liniște.
        Filmul ne arată cum aparențele înșală și cum fiecare are o poveste complexă în spate.
        Este un personaj memorabil, plin de sarcasm dar și de sensibilitate autentică.
    </p>
    <img src="https://external-content.duckduckgo.com/iu/?u=https%3A%2F%2Fi.etsystatic.com%2F27475238%2Fr%2Fil%2F46b262%2F3758939537%2Fil_fullxfull.3758939537_cop1.jpg" alt="Poster film Shrek">
    """
    return html_template.format(titlu="Descriere", continut=continut)

@app.route("/shrek/personaje", methods=['GET'])
def personaje_shrek():
    continut = """
    <h2>Personaje principale</h2>
    <ul>
        <li><strong>Shrek</strong> – căpcăunul verde cu o inimă mare</li>
        <li><strong>Donkey</strong> – tovarășul vesel și loial, plin de vorbe</li>
        <li><strong>Fiona</strong> – prințesa care ascunde un secret incredibil</li>
        <li><strong>Lord Farquaad</strong> – tiranul comic obsedat de perfecțiune</li>
    </ul>
    <img src="https://external-content.duckduckgo.com/iu/?u=https%3A%2F%2Ffacts.net%2Fwp-content%2Fuploads%2F2022%2F06%2FShrek-characters-730x411.jpg" alt="Echipa Shrek">
    """
    return html_template.format(titlu="Personaje", continut=continut)

@app.route("/shrek/trailer", methods=['GET'])
def trailer_shrek():
    continut = """
    <h2>Trailer oficial</h2>
    <p>Urmărește trailerul care a lansat o legendă!</p>
    <iframe src="https://www.youtube.com/embed/CwXOrWvPBPk" title="Trailer Shrek" frameborder="0" allowfullscreen></iframe>
    """
    return html_template.format(titlu="Trailer Shrek", continut=continut)

@app.route("/shrek/poveste", methods=['GET'])
def poveste_shrek():
    continut = f"<h2>Povestea lui Shrek</h2><p>{descriere_personaj()}</p>"
    return html_template.format(titlu="Poveste", continut=continut)

@app.route("/shrek/replici", methods=['GET'])
def replici_shrek():
    continut = f"<h2>Replici memorabile</h2>{replici_memorabile()}"
    return html_template.format(titlu="Replici", continut=continut)

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=5050, debug=True)
