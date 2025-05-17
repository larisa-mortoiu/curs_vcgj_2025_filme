from flask import Flask, request, redirect
from app.lib.descriere import descriere_suits as continut_descriere
from app.lib.actori import personaje_suits as continut_personaje

app = Flask(__name__)
RECENZII_FILE = "recenzii.txt"

html_template = """
<!DOCTYPE html>
<html lang="ro">
<head>
    <meta charset="UTF-8">
    <title>{titlu}</title>
    <link href="https://fonts.googleapis.com/css2?family=Poppins:wght@300;600&display=swap" rel="stylesheet">
    <style>
        * {{
            box-sizing: border-box;
        }}
        body {{
            font-family: 'Poppins', sans-serif;
            background-image: url('https://wallpaperaccess.com/full/1265956.jpg');
            background-size: cover;
            background-attachment: fixed;
            background-position: center;
            margin: 0;
            padding-top: 70px;
            text-align: center;
            color: #ffffff;
        }}
        body::before {{
            content: "";
            position: fixed;
            top: 0;
            left: 0;
            width: 100%;
            height: 100%;
            background: rgba(0, 0, 0, 0.6);
            backdrop-filter: blur(3px);
            z-index: -1;
        }}
        nav {{
            position: fixed;
            top: 0;
            width: 100%;
            background-color: #151520;
            padding: 15px 0;
            text-align: center;
            box-shadow: 0 4px 10px rgba(0, 0, 0, 0.5);
            z-index: 999;
        }}
        nav a {{
            color: #f9d342;
            margin: 0 20px;
            text-decoration: none;
            font-weight: bold;
            font-size: 1.1em;
        }}
        nav a:hover {{
            color: #ffffff;
        }}
        .container {{
            background-color: rgba(0, 0, 0, 0.5);
            padding: 40px;
            margin: 20px auto;
            width: 90%;
            max-width: 800px;
            border-radius: 20px;
            box-shadow: 0 8px 30px rgba(0, 0, 0, 0.4);
        }}
        h1 {{
            font-size: 2.5em;
            margin-bottom: 20px;
            color: #f9d342;
        }}
        h2 {{
            font-size: 1.8em;
            margin-bottom: 15px;
            color: #f9d342;
        }}
        p {{
            font-size: 1.1em;
            line-height: 1.6;
        }}
        button {{
            background: #f9d342;
            color: #1e1e2f;
            padding: 14px 28px;
            margin: 12px;
            border: none;
            border-radius: 30px;
            font-weight: 600;
            font-size: 1em;
            cursor: pointer;
            box-shadow: 0 4px 15px rgba(249, 211, 66, 0.5);
            transition: transform 0.2s, box-shadow 0.2s;
        }}
        button:hover {{
            transform: translateY(-2px);
            box-shadow: 0 6px 20px rgba(249, 211, 66, 0.7);
        }}
        a {{
            display: inline-block;
            margin-top: 20px;
            color: #a2d5f2;
            text-decoration: none;
            font-weight: bold;
        }}
        ul {{
            list-style: none;
            padding: 0;
            margin: 0 auto;
            display: inline-block;
            text-align: left;
        }}
        li {{
            padding: 8px 0;
        }}
        img {{
            margin-top: 20px;
            max-width: 100%;
            border-radius: 12px;
            box-shadow: 0 6px 20px rgba(0, 0, 0, 0.4);
        }}
        iframe {{
            margin-top: 20px;
            border-radius: 12px;
            width: 100%;
            max-width: 640px;
        }}
        .review {{
            background-color: rgba(255,255,255,0.05);
            padding: 20px;
            margin: 20px auto;
            border-radius: 10px;
            width: 90%;
            max-width: 600px;
            box-shadow: 0 4px 20px rgba(0,0,0,0.3);
        }}
        .review p {{
            font-style: italic;
        }}
        .btn-group {{
            display: flex;
            flex-wrap: wrap;
            justify-content: center;
            gap: 15px;
            margin-top: 20px;
        }}
        form input, form textarea {{
            margin: 10px auto;
            display: block;
            width: 60%;
            padding: 10px;
            border-radius: 8px;
            border: none;
            font-family: 'Poppins', sans-serif;
        }}
    </style>
</head>
<body>
    <nav>
        <a href="/">Acasă</a>
        <a href="/suits">Despre</a>
        <a href="/suits/descriere">Descriere</a>
        <a href="/suits/personaje">Personaje</a>
        <a href="/suits/trailer">Trailer</a>
        <a href="/suits/recenzii">Recenzii</a>
    </nav>
    <div class="container">
        {continut}
    </div>
</body>
</html>
"""

@app.route("/")
def pagina_principala():
    continut = """
    <h1>Bine ai venit în lumea avocaților din Suits!</h1>
    <p>
        Explorează universul serialului Suits – află detalii despre personaje, poveste și urmărește trailerul.
    </p>
    <form action="/suits">
         <button type="submit">Intră în universul Suits</button>
    </form>
    """
    return html_template.format(titlu="Suits - Pagina Principală", continut=continut)

@app.route("/suits")
def pagina_suits():
    continut = """
    <h1>Suits</h1>
    <img src="https://wallpaperaccess.com/full/1265956.jpg" alt="Suits cast"><br>
    <div class="btn-group">
        <form action="/suits/descriere"><button type="submit">Descriere</button></form>
        <form action="/suits/personaje"><button type="submit">Personaje</button></form>
        <form action="/suits/trailer"><button type="submit">Vezi trailer</button></form>
        <form action="/suits/recenzii"><button type="submit">Recenzii</button></form>
    </div>
    """
    return html_template.format(titlu="Suits", continut=continut)

@app.route("/suits/descriere")
def descriere_suits():
    continut = continut_descriere() + '<a href="/suits">← Înapoi la pagina principală</a>'
    return html_template.format(titlu="Descriere", continut=continut)

@app.route("/suits/personaje")
def personaje_suits():
    continut = continut_personaje() + '<a href="/suits">← Înapoi la pagina principală</a>'
    return html_template.format(titlu="Personaje", continut=continut)

@app.route("/suits/trailer")
def trailer_suits():
    continut = """
    <h2>Trailer oficial Suits</h2>
    <iframe height="315" src="https://www.youtube.com/embed/85z53bAebsI" 
    title="Suits Trailer" frameborder="0" allowfullscreen></iframe>
    <a href="/suits">← Înapoi la pagina principală</a>
    """
    return html_template.format(titlu="Trailer Suits", continut=continut)

@app.route("/suits/recenzii")
def recenzii_suits():
    recenzii_html = ""
    try:
        with open(RECENZII_FILE, "r", encoding="utf-8") as f:
            for linie in f:
                parts = linie.strip().split("||")
                if len(parts) == 2:
                    recenzii_html += f"""
                    <div class="review">
                        <p>"{parts[1]}"</p>
                        <strong>— {parts[0]}</strong>
                    </div>
                    """
    except FileNotFoundError:
        recenzii_html = "<p>Nu există încă recenzii.</p>"

    continut = f"""
    <h2>Recenzii ale fanilor</h2>
    {recenzii_html}
    <br><a href="/suits/adauga-recenzie">✍️ Adaugă o recenzie</a><br>
    <a href="/suits">← Înapoi la pagina principală</a>
    """
    return html_template.format(titlu="Recenzii Suits", continut=continut)

@app.route("/suits/adauga-recenzie", methods=["GET", "POST"])
def adauga_recenzie():
    if request.method == "POST":
        nume = request.form.get("nume", "").strip()
        mesaj = request.form.get("mesaj", "").strip()
        if nume and mesaj:
            with open(RECENZII_FILE, "a", encoding="utf-8") as f:
                f.write(f"{nume}||{mesaj}\n")
        return redirect("/suits/recenzii")

    continut = """
    <h2>Adaugă o recenzie</h2>
    <form method="POST">
        <input type="text" name="nume" placeholder="Numele tău" required>
        <textarea name="mesaj" placeholder="Scrie recenzia ta..." rows="4" required></textarea>
        <button type="submit">Trimite recenzia</button>
    </form>
    <a href="/suits/recenzii">← Înapoi la recenzii</a>
    """
    return html_template.format(titlu="Adaugă Recenzie", continut=continut)

if __name__ == "__main__":
    app.run(host="127.0.0.1", port=5050, debug=True)

