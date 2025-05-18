# Proiect SCC – Breaking Bad Web App

**Autor:** Zarafin Radu-Adrian (Grupa 442D)

---

## Cuprins

1. [Descriere aplicație](#descriere-aplicație)
2. [Funcționalități & Versiuni](#funcționalități--versiuni)
3. [Tehnologii folosite](#tehnologii-folosite)
4. [Structura proiectului](#structura-proiectului)
5. [Configurare & Instalare](#configurare--instalare)
6. [Prezentare interfață web](#prezentare-interfață-web)
7. [Testare cu Pytest](#testare-cu-pytest)
8. [Analiză statică cu Pylint](#analiză-statică-cu-pylint)
9. [Containerizare cu Docker](#containerizare-cu-docker)
10. [Pipeline CI/CD cu Jenkins](#pipeline-cicd-cu-jenkins)
11. [Pull Request & Mentenanță](#pull-request--mentenanță)

---

## Descriere aplicație

Această aplicație web este dedicată serialului „Breaking Bad” și oferă utilizatorilor o interfață simplă pentru a vizualiza:
- o descriere generală a serialului,
- personaje principale,
- trailere oficiale.

Aplicația este construită cu Flask și este modularizată astfel încât fiecare atribut (descriere, actori, trailere) este gestionat într-un fișier separat.

---

## Funcționalități & Versiuni

* **v1.0** – versiune funcțională cu:
  * pagină principală `/`
  * pagină cu descriere `/breaking-bad`
  * pagină cu personaje `/breaking-bad/characters`
  * pagină cu trailere `/breaking-bad/trailers`
  * integrare Jenkins + Docker + Pytest + Pylint

---

## Tehnologii folosite

* **Python 3.10** & **Flask** – backend web
* **HTML/CSS** – afișare interfețe
* **Jinja2** – motor de template-uri
* **Pytest** – testare automată
* **Pylint** – analiză statică
* **Docker** – containerizare
* **Jenkins** – CI/CD pipeline

---

## Structura proiectului

```text
curs_vcgj_2025_filme
    ├── activeaza_venv
    ├── activeaza_venv_jenkins
    ├── app
    │   ├── lib
    │   │   ├── actors.py
    │   │   ├── description.py
    │   │   ├── __pycache__
    │   │   │   ├── actors.cpython-310.pyc
    │   │   │   ├── description.cpython-310.pyc
    │   │   │   └── trailers.cpython-310.pyc
    │   │   └── trailers.py
    │   └── tests
    │       ├── __pycache__
    │       │   └── test_filme.cpython-310-pytest-7.4.0.pyc
    │       └── test_filme.py
    ├── breaking_bad
    ├── Dockerfile
    ├── dockerstart_jenkins.sh
    ├── dockerstart.sh
    ├── filme.py
    ├── Jenkinsfile
    ├── LICENSE
    ├── __pycache__
    │   └── filme.cpython-310.pyc
    ├── pytest.ini
    ├── quickrequirements.txt
    ├── README.md
    ├── static
    │   ├── images
    │   │   ├── breaking_bad.jpg
    │   │   ├── gus_fring.jpg
    │   │   ├── hank_schrader.jpg
    │   │   ├── hector_salamanca.jpg
    │   │   ├── imdb-logo.png
    │   │   ├── jesse_pinkman.jpg
    │   │   ├── marie_schrader.jpg
    │   │   ├── mike_ehrmantraut.jpg
    │   │   ├── saul_goodman.jpg
    │   │   ├── skyler_white.jpg
    │   │   ├── smoke.gif
    │   │   ├── tuco_salamanca.jpg
    │   │   └── walter_white.avif
    │   ├── screenshots
    │   │   ├── activare_venv_start_app.png
    │   │   ├── actori.png
    │   │   ├── descriere.png
    │   │   ├── homepage.png
    │   │   ├── pipeline.png
    │   │   └── trailers.png
    │   └── styles
    │       └── style.css
    └── templates
        ├── characters.html
        ├── description.html
        ├── index.html
        └── trailers.html

```

---

## Configurare & Instalare

1. **Clone repo & branch**:

```bash
git clone https://github.com/larisa-mortoiu/curs_vcgj_2025_filme.git
cd curs_vcgj_2025_filme
git checkout dev_Zarafin_Radu
```
2. **Rulare directă** (fără venv):
 ```bash
 python3 filme.py
 ```
3. **Rulare cu venv**:
```bash
source activeaza_venv
source breaking_bad
```

Acces aplicație: [http://localhost:5011](http://localhost:5011)

---
![image](https://github.com/larisa-mortoiu/curs_vcgj_2025_filme/blob/dev_Zarafin_Radu/static/screenshots/activare_venv_start_app.png)


## Prezentare interfață web

### 1. Homepage
![Homepage](https://github.com/larisa-mortoiu/curs_vcgj_2025_filme/blob/dev_Zarafin_Radu/static/screenshots/homepage.png)

### 2. Characters
![Characters](https://github.com/larisa-mortoiu/curs_vcgj_2025_filme/blob/dev_Zarafin_Radu/static/screenshots/actori.png)

### 3. Trailers
![Trailers](https://github.com/larisa-mortoiu/curs_vcgj_2025_filme/blob/dev_Zarafin_Radu/static/screenshots/trailers.png)

---

## Testare cu Pytest

Testele validează:
- codul 200 pentru fiecare rută
- structura obiectului `trailers`

```bash
python3 -m pytest app/tests/ -q
```
![image](https://github.com/larisa-mortoiu/curs_vcgj_2025_filme/blob/dev_Zarafin_Radu/static/screenshots/testare_manuala.png)
---

## Analiză statică cu Pylint

```bash
pylint app/lib/*.py app/tests/*.py filme.py
```

Se folosește `--exit-zero` în Jenkins pentru a nu întrerupe pipeline-ul la warning-uri.

---

## Containerizare cu Docker

```bash
docker build -t breakingbad-app .
docker run -p 5011:5011 breakingbad-app
```

Aplicația devine accesibilă la: [http://localhost:5011](http://localhost:5011)

---

## Pipeline CI/CD cu Jenkins

Pipeline-ul include pașii:

1. Build
2. Analiză statică cu Pylint
3. Testare unitară cu Pytest
4. Deploy: Pornire container local (`breakingbad-container`)


Exemplu rulare cu succes:
![Pipeline](https://github.com/larisa-mortoiu/curs_vcgj_2025_filme/blob/dev_Zarafin_Radu/static/screenshots/pipeline.png)

---

## Pull Request & Mentenanță

* Dezvoltarea se face pe branch `dev_Zarafin_Radu`
* Se deschide PR către `main_Zarafin_Radu`
* După review și succes pipeline, se face merge și build automat pe `main`

---
