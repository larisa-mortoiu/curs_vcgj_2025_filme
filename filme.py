from flask import Flask
from app.lib.descriere import get_descriere
from app.lib.actori import get_actori

app = Flask(__name__)

html_template = """
<!DOCTYPE html>
<html lang="ro">
<head>
    <meta charset="UTF-8">
    <title>{titlu}</title>
    <style>
        body {{
            margin: 0;
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
            position: relative;
            min-height: 100vh;
            overflow-x: hidden;
        }}

        body::before {{
            content: "";
            position: fixed;
            top: 0; left: 0;
            width: 100%; height: 100%;
            background: url('https://i0.wp.com/www.lstylegstyle.com/wp-content/uploads/2014/12/The-Imitation-Game-Quad-poster-Benedict-Cumberbatch11.jpg?fit=985%2C565&ssl=1') no-repeat center center fixed;
            background-size: cover;
            filter: blur(8px) brightness(0.6);
            z-index: -1;
        }}

        header, footer {{
            background-color: rgba(75, 30, 30, 0.95);
            color: #e0a949;
            text-align: center;
            padding: 20px;
            font-size: 24px;
            font-weight: bold;
            backdrop-filter: blur(4px);
	    -webkit-backdrop-filter: blur(4px);

        }}

        .nav-buttons {{
            margin-top: 10px;
        }}

        .nav-buttons a {{
            background-color: #7b1f1f;
            color: white;
            padding: 10px 20px;
            margin: 5px;
            border-radius: 8px;
            text-decoration: none;
            font-weight: bold;
            display: inline-block;
            font-size: 16px;
            transition: background-color 0.2s ease-in-out;
        }}

        .nav-buttons a:hover {{
            background-color: #5e1515;
        }}

        .container {{
            display: flex;
            justify-content: center;
            align-items: center;
            padding: 40px 20px;
            min-height: 80vh;
            z-index: 1;
        }}

        .card {{
            background-color: rgba(255, 255, 255, 0.85);
            border-radius: 16px;
            padding: 30px;
            box-shadow: 0 10px 25px rgba(0,0,0,0.2);
            text-align: center;
            max-width: 700px;
            width: 100%;
            position: relative;
            z-index: 2;
        }}

        .card img {{
            width: 100%;
            border-radius: 12px;
            margin-bottom: 20px;
        }}

        .card h2 {{
            color: #7b1f1f;
            margin-bottom: 10px;
        }}

        .card p {{
            font-size: 17px;
            line-height: 1.5;
        }}

        .card button {{
            background-color: #7b1f1f;
            color: white;
            border: none;
            padding: 10px 20px;
            border-radius: 8px;
            margin: 10px 0;
            cursor: pointer;
            font-size: 16px;
            font-weight: bold;
            width: 200px;
            transition: background-color 0.2s ease-in-out;
        }}

        .card button:hover {{
            background-color: #5e1515;
        }}

        a {{
            display: block;
            margin-top: 20px;
            color: #7b1f1f;
            text-decoration: none;
            font-weight: bold;
        }}

        .img-home {{
            width: 70%;
            max-width: 300px;
            margin-bottom: 20px;
            border-radius: 12px;
        }}
    </style>
</head>
<body>
    <header>
        Movie Portal
        <div class="nav-buttons">
            <a href="/">Acasă</a>
            <a href="/imitation-game">The Imitation Game</a>
            <a href="/imitation-game/descriere">Descriere</a>
            <a href="/imitation-game/actori">Actori</a>
            <a href="/imitation-game/trailer">Trailer</a>
        </div>
    </header>
    <div class="container">
        {continut}
    </div>
    <footer style="font-size: 14px; color: #555;">
        © 2025 Movie Portal. Toate drepturile rezervate.
    </footer>
</body>
</html>
"""

@app.route("/")
def homepage():
    continut = """
    <div class='card'>
        <img src="https://encrypted-tbn1.gstatic.com/images?q=tbn:ANd9GcR2U4mxZY4YdluCriYhHs1iXSvB2-hZkHATfNTAiTZ-IfHk6E6s9uPYlDfTOvkCOkATd_XLzw" alt="Welcome image" class="img-home">
        <h2>Bine ai venit!</h2>
        <p>Alege un titlul pentru a vedea detalii.</p>
        <form action="/imitation-game">
            <button type="submit">The Imitation Game</button>
        </form>
    </div>
    """
    return html_template.format(titlu="Acasă", continut=continut)

@app.route("/imitation-game")
def pagina_film():
    continut = """
    <div class='card'>
        <h2>The Imitation Game (2014)</h2>
        <img src="https://www.hollywoodreporter.com/wp-content/uploads/2014/09/the_imitation_game_a_p.jpg" alt="Poster" style="width: 25%; border-radius: 12px;">
        <p>Un film captivant despre criptanalistul britanic Alan Turing și spargerea codului Enigma în timpul celui de-al Doilea Război Mondial.</p>
        <form action="/imitation-game/descriere">
            <button type="submit">Vezi descriere</button>
        </form>
        <form action="/imitation-game/actori">
            <button type="submit">Vezi actori</button>
        </form>
        <form action="/imitation-game/trailer">
            <button type="submit">Vezi trailer</button>
        </form>
        <a href="/">← Înapoi la homepage</a>
    </div>
    """
    return html_template.format(titlu="The Imitation Game", continut=continut)

@app.route("/imitation-game/descriere")
def pagina_descriere():
    continut = f"""
    <div class='card'>
        <h2>Descriere</h2>
        <p>{get_descriere()}</p>
        <a href="/imitation-game">← Înapoi</a>
    </div>
    """
    return html_template.format(titlu="Descriere Film", continut=continut)

@app.route("/imitation-game/actori")
def pagina_actori():
    continut = f"""
    <div class='card'>
        <h2>Actori principali</h2>
        <div style='display: grid; grid-template-columns: repeat(auto-fill, minmax(120px, 1fr)); gap: 15px; margin: 20px 0;'>
            <div><img src='https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQpFn1Tun9DSlGXggeItJcqKlP6r1EsPQlZz7NEc33s45yumjhegG2Go9R5QtA4t7Fjs87m8KKp1Dy7rKetkHFmig' alt='Benedict Cumberbatch' style='width:120px; height:160px; object-fit: cover; border-radius:8px;'><p>Benedict Cumberbatch</p></div>
            <div><img src='https://encrypted-tbn2.gstatic.com/images?q=tbn:ANd9GcQLZFqnSqfucVETztDq7cYSf2XGppNDAK6BksZSPzagOQluE3Hq8vEaLMmgPx24edeCcnzcF6v5-JOd92j-7wV81Q' alt='Keira Knightley' style='width:120px; height:160px; object-fit: cover; border-radius:8px;'><p>Keira Knightley</p></div>
            <div><img src='https://encrypted-tbn1.gstatic.com/images?q=tbn:ANd9GcRI8b_RR0eaPcxUEwoJb9ERmves0iH-bPlpM23jshamzcmk8VNyeo3PHlYxrYS4J6sjwgAKc08OALSSSIWD67vFjw' alt='Matthew Goode' style='width:120px; height:160px; object-fit: cover; border-radius:8px;'><p>Matthew Goode</p></div>
            <div><img src='https://encrypted-tbn1.gstatic.com/images?q=tbn:ANd9GcQI-BN0QH0ewSpJ3dPrSiIupAo2wQ2fyXgZCNV9t_cwp2pilQ7qCTm4rIuE3p5TsdZFX96G3HqglRJj3z0gfmbS5w' alt='Allen Leech' style='width:120px; height:160px; object-fit: cover; border-radius:8px;'><p>Allen Leech</p></div>
            <div><img src='https://encrypted-tbn1.gstatic.com/licensed-image?q=tbn:ANd9GcSWTw_BfAdpHk2k5OVlb6RX2CSIqGGkmDKc3LHxfw5_7POdjoiMUms1V9UwwHAIX9Jxd4HJALTtGylc_Ys' alt='Mark Strong' style='width:120px; height:160px; object-fit: cover; border-radius:8px;'><p>Mark Strong</p></div>
            <div><img src='https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSwLFJDH_-Zsu_guEKQepu9QKk42cxxhkT1ZQdsBNAmzXG1U_y8mjYum5JDBjbICkFTtMnfp18eQskMLhp3aP1IkQ' alt='Charles Dance' style='width:120px; height:160px; object-fit: cover; border-radius:8px;'><p>Charles Dance</p></div>
            
        </div>
        <a href="/imitation-game">← Înapoi</a>
    </div>
    """
    return html_template.format(titlu="Actori Film", continut=continut)

@app.route("/imitation-game/trailer")
def pagina_trailer():
    continut = """
    <div class='card'>
        <h2>Trailer</h2>
        <iframe width="100%" height="315" src="https://www.youtube.com/embed/nuPZUUED5uk"
                title="YouTube video player" frameborder="0"
                allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen>
        </iframe>
        <a href="/imitation-game">← Înapoi</a>
    </div>
    """
    return html_template.format(titlu="Trailer Film", continut=continut)

if __name__ == "__main__":
    app.run(host="127.0.0.1", port=5050)

