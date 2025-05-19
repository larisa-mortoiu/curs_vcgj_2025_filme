# Eftimie Albert
Cuprins
Descriere aplicație

Funcționalități

Tehnologii

Structură

Rulare locală

Testare & Analiză

Docker & Jenkins

Descriere aplicație
Aplicație web Flask despre serialul Dexter, cu pagini pentru descriere și actori. Interfață responsive, cod organizat, testat și containerizat.

Funcționalități
Homepage cu tematică Dexter

Pagină „Descriere” cu imagine și text

Pagină „Actori” cu carduri pentru fiecare personaj

Navigare ușoară între pagini

Tehnologii
Flask, Python

HTML + CSS

Pytest, Pylint

Docker, Jenkins

Structură
text
Copiază
Editează
curs_vcgj_2025_filme/
├── app/lib/            # logica pentru descriere + actori
├── app/tests/          # teste unitare
├── templates/          # pagini HTML
├── static/             # CSS + imagini
├── filme.py            # aplicația Flask
Rulare locală
bash
Copiază
Editează
git clone https://github.com/larisa-mortoiu/curs_vcgj_2025_filme.git
cd curs_vcgj_2025_filme
git checkout dev_Eftimie_Albert
pip install flask
python3 filme.py
Acces: http://127.0.0.1:5000

Testare & Analiză
bash
Copiază
Editează
pytest app/tests/
pylint app/lib/*.py
Docker & Jenkins
bash
Copiază
Editează
docker build -t dexter:v1 .
docker run -d -p 8020:5000 dexter:v1
Pipeline configurat în Jenkinsfile pentru CI/CD automat.

