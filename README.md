# curs_vcgj_2025_filme
# 🎬 Cars Movie App — Flask + Docker + Jenkins

Aplicație web scrisă în Flask care afișează detalii despre filmul **Cars (2006)**: descriere, distribuție și un trailer integrat. Proiectul include infrastructură de testare, containerizare Docker și CI cu Jenkins.

---

## 🧠 Funcționalități

- 📝 Afișare descriere film
- 👨‍🎤 Afișare cast (poze + listă)
- ▶️ Trailer YouTube integrat
- ✅ Testare automată cu `pytest`
- 🐳 Docker-ready
- ⚙️ CI automatizat cu Jenkins

---

## 🚀 Cum rulezi local

### 1. Clonează proiectul

```bash
git clone https://github.com/username/cars-flask-app.git
cd cars-flask-app

### 2. Rulează în Docker
docker build -t flask-cars .
docker run -p 5000:5000 flask-cars
Accesează în browser:
📍 http://localhost:5000

### 3. Testarea aplicatiei

pytest app/tests/test_filme.py


Testele validează:

-calitatea descrierii

-formatul listei de actori

-existența rutelor Flask

###4.CI cu Jenkins
Rulează Jenkins local

Creează un job de tip Pipeline

Asigură-te că ai Jenkinsfile în repo

###5.Structura

├── filme.py                # Aplicația principală Flask
├── Dockerfile              # Containerizare
├── Jenkinsfile             # CI pipeline
├── requirements.txt        # Dependențe
├── templates/              # Pagini HTML
├── static/                 # CSS, imagini
├── app/
│   ├── lib/
│   │   ├── cars_actori.py
│   │   └── cars_descriere.py
│   └── tests/
│       └── test_filme.py

Autor
Adil Mologani
@github.com/username


---

## ✅ Personalizare:

- înlocuiește `https://github.com/username/...` cu linkul tău
- adaugă eventual imagini relevante (ex: capturi UI)
- poți adăuga și secțiune _"Future features"_ dacă ai planuri de extindere

Vrei să includem și instrucțiuni pentru rulare cu `docker-compose`? Sau să îți creez un badge CI pentru GitHub?

