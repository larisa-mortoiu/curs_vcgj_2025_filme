# curs_vcgj_2025_filme
# 🎬 Cars Movie App 

Aplicație web scrisă în Flask care afișează detalii despre filmul **Cars (2006)**: descriere, distribuție și un trailer integrat. Proiectul include infrastructură de testare, containerizare Docker și CI cu Jenkins.

---

# 🧠 Funcționalități

- 📝 Afișare descriere film
- 👨‍🎤 Afișare cast (poze + listă)
- ▶️ Trailer YouTube integrat
- ✅ Testare automată cu `pytest`
- 🐳 Docker-ready
- ⚙️ CI automatizat cu Jenkins

---


# 1. Clonează proiectul

```bash
git clone https://github.com/larisa-mortoiu/curs_vcgj_2025_filme.git
cd curs_vcgj_2025_filme
```

# 2. Rulează în Docker
```
docker build -t flask-cars .
docker run -p 5000:5000 flask-cars

```

Accesează în browser:
📍 http://localhost:5000

# 3. Testarea aplicatiei

pytest app/tests/test_filme.py


Testele validează:

-calitatea descrierii

-formatul listei de actori

-existența rutelor Flask

# 4.CI cu Jenkins

Rulează Jenkins local

```
sudo systemctl start jenkins

```

Creează un job de tip Pipeline

Jenkinsfile execută:

- setup venv

- rulare lint (pylint)

- rulare pytest

- build Docker image

# 5.Structura
```
.
├── filme.py                # Aplicația principală Flask
├── Dockerfile              # Docker build file
├── Jenkinsfile             # CI logic pentru Jenkins
├── requirements.txt        # Dependențe Python
├── static/
│   ├── images/             # Imagini actori + elemente vizuale
│   └── styles/             # CSS pentru pagini
├── templates/
│   ├── home_cars.html
│   ├── cast_cars.html
│   ├── descriere_cars.html
│   └── cars_2006.html
├── app/
│   ├── lib/
│   │   ├── cars_actori.py         # Returnează lista actorilor
│   │   └── cars_descriere.py      # Returnează descrierea filmului
│   └── tests/
│       └── test_filme.py          # Teste unificate pentru aplicație

```

# Interfata Web

## Pagina principală (Homepage)
Reprezintă punctul de plecare al aplicației, oferind utilizatorului o primă interacțiune vizuală și acces rapid către informațiile esențiale despre filmul Cars (2006). De aici, utilizatorul poate naviga către secțiunea de descriere sau către distribuția filmului, în funcție de interes.

![Movie](https://github.com/larisa-mortoiu/curs_vcgj_2025_filme/blob/dev_Mologani_Adil/static/images/captures/Home_page.png)

## 🎬 Pagina film (Movie)
Această pagină oferă o prezentare succintă a filmului, incluzând titlul, anul lansării, genul și durata, alături de trailerul integrat. De asemenea, conține două butoane de navigare care permit utilizatorului să acceseze fie secțiunea de descriere detaliată, fie distribuția completă.


![Home_page](https://github.com/larisa-mortoiu/curs_vcgj_2025_filme/blob/dev_Mologani_Adil/static/images/captures/movie_page.png)

## 📝 Secțiunea de descriere (Description)
Prezintă în mod detaliat subiectul filmului, personajul principal, conflictul narativ și temele abordate. Textul este extras dintr-un modul Python și afișat împreună cu o imagine ilustrativă specifică, într-un layout optimizat pentru lizibilitate și impact vizual.

![Description](https://github.com/larisa-mortoiu/curs_vcgj_2025_filme/blob/dev_Mologani_Adil/static/images/captures/description.png)

## 👥 Secțiunea de distribuție (Cast)
Afișează actorii principali ai filmului împreună cu imaginile acestora, organizate într-o grilă responsive. Sub grilă, este afișată și o listă completă cu numele actorilor, generată automat dintr-un script Python. Această secțiune oferă utilizatorului o imagine completă asupra distribuției filmului.

![Cast](https://github.com/larisa-mortoiu/curs_vcgj_2025_filme/blob/dev_Mologani_Adil/static/images/captures/cast.png)
