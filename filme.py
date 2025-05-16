from flask import Flask

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
            background-color: #eef5ec;
            margin: 0;
            padding: 0;
        }}
        .logo {{
            font-size: 48px;
            font-weight: bold;
            color: forestgreen;
            text-align: center;
            padding: 30px 0 10px 0;
            text-shadow: 2px 2px 0 #8B4513;
            letter-spacing: 3px;
        }}
        .navbar {{
            background-color: #228B22;
            padding: 15px 20px;
            display: flex;
            justify-content: center;
            gap: 20px;
            box-shadow: 0 2px 6px rgba(0,0,0,0.1);
        }}
        .navbar a {{
            color: white;
            text-decoration: none;
            font-weight: bold;
            font-size: 16px;
            transition: color 0.3s ease;
        }}
        .navbar a:hover {{
            color: #d4e7d4;
        }}
        .container {{
            background-color: #ffffff;
            margin: 40px auto;
            padding: 40px 50px;
            width: 90%;
            max-width: 900px;
            border-radius: 12px;
            box-shadow: 0 0 20px rgba(0,0,0,0.1);
            text-align: center;
        }}
        h1, h2 {{
            color: #2c3e50;
            margin-bottom: 20px;
        }}
        p {{
            font-size: 18px;
            line-height: 1.6;
            margin-bottom: 30px;
            color: #3e3e3e;
        }}
        .btn-container {{
            display: flex;
            flex-wrap: wrap;
            justify-content: center;
            gap: 15px;
            margin-top: 30px;
        }}
        form {{
            display: inline-block;
        }}
        button {{
            background-color: #228B22;
            color: white;
            padding: 12px 24px;
            border: none;
            border-radius: 8px;
            font-weight: bold;
            font-size: 16px;
            cursor: pointer;
            transition: background-color 0.3s ease;
        }}
        button:hover {{
            background-color: #1e7a1e;
        }}
        .back-btn {{
            display: inline-block;
            margin-top: 30px;
            background-color: #8B4513;
            color: white;
            padding: 10px 20px;
            border: none;
            border-radius: 8px;
            font-weight: bold;
            text-decoration: none;
            transition: background-color 0.3s ease;
        }}
        .back-btn:hover {{
            background-color: #6e3610;
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
            font-size: 17px;
            margin-top: 20px;
        }}
    </style>
</head>
<body>
    <div class="logo">SHREK</div>
    <div class="navbar">
        <a href="/">Acasă</a>
        <a href="/shrek">Despre</a>
        <a href="/shrek/descriere">Descriere</a>
        <a href="/shrek/personaje">Personaje</a>
        <a href="/shrek/trailer">Trailer</a>
    </div>
    <div class="container">
        {continut}
    </div>
</body>
</html>
"""

@app.route("/", methods=['GET'])
def pagina_principala():
    continut = """
    <h1>Bine ai venit în regatul lui Shrek!</h1>
    <p>
        Un site dedicat filmului animat Shrek – o aventură plină de umor, personaje memorabile și magie inversă.
    </p>
    <div class="btn-container">
        <form action="/shrek">
            <button type="submit">Explorează filmul</button>
        </form>
    </div>
    """
    return html_template.format(titlu="Shrek - Acasă", continut=continut)

@app.route("/shrek", methods=['GET'])
def pagina_shrek():
    continut = """
    <h1>Despre filmul Shrek</h1>
    <p>
        Shrek este o comedie animată produsă de DreamWorks care sparge toate clișeele poveștilor cu prinți și prințese.
        Lansat în 2001, filmul a câștigat inimile publicului de toate vârstele.
    </p>
    <div class="btn-container">
        <form action="/shrek/descriere"><button type="submit">Descriere</button></form>
        <form action="/shrek/personaje"><button type="submit">Personaje</button></form>
        <form action="/shrek/trailer"><button type="submit">Trailer</button></form>
    </div>
    """
    return html_template.format(titlu="Shrek", continut=continut)

@app.route("/shrek/descriere", methods=['GET'])
def descriere_shrek():
    continut = """
    <h2>Un basm inversat și plin de umor</h2>
    <p>
        Shrek este un căpcăun verde care trăiește liniștit într-o mlaștină. Viața lui ia o turnură neașteptată
        când pornește într-o călătorie cu un măgar enervant pentru a salva o prințesă. 
        Dar nimic nu este ce pare...
    </p>
    <a class="back-btn" href='/shrek'>← Înapoi la meniu</a>
    """
    return html_template.format(titlu="Descriere", continut=continut)

@app.route("/shrek/personaje", methods=['GET'])
def personaje_shrek():
    continut = """
    <h2>Personaje principale</h2>
    <ul>
        <li><strong>Shrek</strong> – căpcăunul verde, protagonistul curajos și sarcastic</li>
        <li><strong>Donkey</strong> – prietenul vorbăreț și loial al lui Shrek</li>
        <li><strong>Fiona</strong> – prințesa independentă cu un secret magic</li>
        <li><strong>Lord Farquaad</strong> – conducătorul scund și tiranic</li>
    </ul>
    <a class="back-btn" href='/shrek'>← Înapoi la meniu</a>
    """
    return html_template.format(titlu="Personaje", continut=continut)

@app.route("/shrek/trailer", methods=['GET'])
def trailer_shrek():
    continut = """
    <h2>Trailer oficial</h2>
    <iframe src="https://www.youtube.com/embed/CwXOrWvPBPk" 
    title="Trailer Shrek" frameborder="0" allowfullscreen></iframe>
    <br>
    <a class="back-btn" href='/shrek'>← Înapoi la meniu</a>
    """
    return html_template.format(titlu="Trailer Shrek", continut=continut)

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=5050, debug=True)
