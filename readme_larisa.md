# Cuprins
1. [Prezentare generală](#prezentare-generală)
2. [Funcționalități disponibile](#funcționalități-disponibile)
3. [Stack tehnologic](#stack-tehnologic)
4. [Structura proiectului](#structura-proiectului)
5. [Instrucțiuni de instalare](#instrucțiuni-de-instalare)
6. [Pagini disponibile](#pagini-disponibile)
7. [Testare Pytest](#testare-pytest)
8. [Analiză cu Pylint](#analiză-cu-pylint)
9. [Utilizare Docker](#utilizare-docker)
10. [Integrare Jenkins](#integrare-jenkins)
11. [Pull Request](#pull-request)
12. [Surse](#surse)

# Prezentare generală
Această aplicație web oferă utilizatorilor o experiență completă în jurul serialului Suits (2011). Pagina principală permite navigarea către informații esențiale: prezentare generală, poveste, personaje principale, trailer, precum și o secțiune de recenzii scrise de vizitatori.

Aplicația este dezvoltată folosind Flask, este containerizată cu Docker și include testare automată și verificare statică a codului. Interacțiunea cu utilizatorul este simplă și intuitivă.

# Funcționalități disponibile
- Pagină principală cu meniu de navigare
- Pagini statice: descriere, trailer, prezentare serial, distribuție
- Pagină dinamică: recenzii (afișare + adăugare)
- Testare cu Pytest pentru rute și funcționalități
- Analiză cod cu Pylint
- Suport pentru rulare locală și în container Docker
- Pipeline de CI cu Jenkins

# Stack tehnologic
- *Flask* – framework web
- *HTML & CSS* – structură și stilizare
- *Pytest* – testare automată
- *Pylint* – verificare statică
- *Docker* – containerizare
- *Jenkins* – CI/CD

# Structura proiectului

.
├── app
│   ├── __init__.py
│   ├── lib
│   │   ├── actori.py
│   │   ├── descriere.py
│   │   ├── __init__.py
│   │   └── __pycache__
│   │       ├── actori.cpython-310.pyc
│   │       ├── descriere.cpython-310.pyc
│   │       └── __init__.cpython-310.pyc
│   ├── __pycache__
│   │   ├── __init__.cpython-310.pyc
│   │   └── test_filme.cpython-310-pytest-8.3.5.pyc
│   └── tests
│       ├── __init__.py
│       ├── __pycache__
│       │   ├── __init__.cpython-310.pyc
│       │   └── test_filme.cpython-310-pytest-8.3.5.pyc
│       └── test_filme.py
├── Dockerfile
├── filme.py
├── Jenkinsfile
├── LICENSE
├── __pycache__
│   └── filme.cpython-310.pyc
├── quickrequirements.txt
├── readme_larisa.md
├── README.md
├── recenzii.txt
└── static
    └── screenshots
        ├── descriere.png
        ├── despre.png
        ├── home.png
        ├── personaje.png
        ├── recenzii.png
        └── trailer.png



# Instrucțiuni de instalare
bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r quickrequirements.txt
python3 filme.py

Accesează aplicația la: [http://127.0.0.1:5050](http://127.0.0.1:5050)

# Pagini disponibile
- / – Pagina de start
- /despre – Despre serial
- /descriere – Prezentare detaliată
- /personaje – Actori principali
- /trailer – Trailer oficial YouTube
- /recenzii – Afișare și trimitere recenzii

### Capturi interfață
- ![home](https://github.com/larisa-mortoiu/curs_vcgj_2025_filme/blob/main_Mihalcea_Larisa/static/screenshots/static/screenshots/home.png?raw=true)
- ![descriere](https://github.com/larisa-mortoiu/curs_vcgj_2025_filme/blob/main_Mihalcea_Larisa/static/screenshots/static/screenshots/descriere.png?raw=true)
- ![personaje](https://github.com/larisa-mortoiu/curs_vcgj_2025_filme/blob/main_Mihalcea_Larisa/static/screenshots/static/screenshots/personaje.png?raw=true)
- ![trailer](https://github.com/larisa-mortoiu/curs_vcgj_2025_filme/blob/main_Mihalcea_Larisa/static/screenshots/static/screenshots/trailer.png?raw=true)
- ![recenzii](https://github.com/larisa-mortoiu/curs_vcgj_2025_filme/blob/main_Mihalcea_Larisa/static/screenshots/static/screenshots/recenzii.png?raw=true)

# Testare Pytest
bash
pytest app/tests/

- verificare status 200 pentru rute
- testare adăugare recenzie

![pytest](https://github.com/larisa-mortoiu/curs_vcgj_2025_filme/blob/main_Mihalcea_Larisa/static/screenshots/static/screenshots/testare-pytest.png?raw=true)

# Analiză cu Pylint
bash
pylint filme.py app/lib/*.py app/tests/*.py --exit-zero

![pylint](https://github.com/larisa-mortoiu/curs_vcgj_2025_filme/blob/main_Mihalcea_Larisa/static/screenshots/static/screenshots/verificare-pylint.png?raw=true)

# Utilizare Docker
bash
docker build -t suits-app .
docker run -p 5050:5050 suits-app

![docker](https://github.com/larisa-mortoiu/curs_vcgj_2025_filme/blob/main_Mihalcea_Larisa/static/screenshots/static/screenshots/docker-run.png?raw=true)
![docker](https://github.com/larisa-mortoiu/curs_vcgj_2025_filme/blob/main_Mihalcea_Larisa/static/screenshots/static/screenshots/docker.png?raw=true)
# Integrare Jenkins
Pipeline-ul rulează automat:
- instalare dependințe
- pylint
- pytest
- build container Docker
![jenkins](https://github.com/larisa-mortoiu/curs_vcgj_2025_filme/blob/main_Mihalcea_Larisa/static/screenshots/static/screenshots/jenkins-blueocean.png?raw=true)

# Pull Request
PR din dev_nume_student către main, aprobat și testat automat.
![pull-request](https://github.com/larisa-mortoiu/curs_vcgj_2025_filme/blob/main_Mihalcea_Larisa/static/screenshots/static/screenshots/pull-request.png?raw=true)

# Surse
- [Flask Docs](https://flask.palletsprojects.com)
- [Pytest](https://docs.pytest.org)
- [Docker](https://docs.docker.com)
- [Jenkins](https://www.jenkins.io)
- [Pylint](https://pylint.pycqa.org)
