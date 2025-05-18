# Proiect SCC – Breaking Bad Web App

**Autor:** Tofan IOnut Lucian (Grupa 442D)

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

Această aplicație web este dedicată filmului "Interstellar” și oferă utilizatorilor o interfață simplă pentru a vizualiza:
- o descriere generală a serialului,
- personaje principale,
- trailer oficial.

Aplicația este construită cu Flask și este modularizată astfel încât fiecare atribut (descriere, actori, trailere) este gestionat într-un fișier separat.

---

## Funcționalități & Versiuni

* **v1.0** – versiune funcțională cu:
  * pagină principală 
  * pagină cu descriere 
  * pagină cu personaje 
  * pagină cu trailere
  * integrare Jenkins + Docker + Pytest + Pylint

---

## Tehnologii folosite

* **Python 3.10** & **Flask** – backend web
* **HTML/CSS** – afișare interfețe
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
    │   └── tests
    │       └── test_filme.py
    ├── Dockerfile
    ├── dockerstart_jenkins.sh
    ├── dockerstart.sh
    ├── filme.py
    ├── Jenkinsfile
    ├── LICENSE
    ├── pytest.ini
    ├── README.md
    ├── requirements.txt
    ├── static
    │   ├── images
    │   │   ├── Anne Hathaway.jpeg
    │   │   ├── cover.jpeg
    │   │   ├── Jessica Chastain.jpeg
    │   │   ├── Mackenzie Foy.jpeg
    │   │   ├── Matt Damon.jpeg
    │   │   ├── Matthew McConaughey.jpeg
    │   │   ├── Michael Caine.jpeg
    │   │   └── Timothée Chalamet.jpeg
    │   └── styles
    │       └── styles.css
    ├── templates
    │   ├── actori.html
    │   ├── descriere.html
    │   ├── index.html
    │   └── trailer.html
    └── venv
        ├── bin
        │   ├── activate
        │   ├── activate.csh
        │   ├── activate.fish
        │   ├── Activate.ps1
        │   ├── flask
        │   ├── pip
        │   ├── pip3
        │   ├── pip3.10
        │   ├── python -> python3
        │   ├── python3 -> /usr/bin/python3
        │   └── python3.10 -> python3
        ├── include
        ├── lib
        │   └── python3.10
        ├── lib64 -> lib
        └── pyvenv.cfg



```

---

## Configurare & Instalare

1. **Clone repo & branch**:

```bash
git clone https://github.com/larisa-mortoiu/curs_vcgj_2025_filme.git
cd curs_vcgj_2025_filme
git checkout dev_Tofan_Lucian
```

2. **Rulare cu venv**:
```bash
source activeaza_venv
python filme.py
```

Acces aplicație: [http://localhost:5000](http://localhost:5000)

---
![image](https://github.com/user-attachments/assets/33267851-7989-48d6-bbba-ee10d596eeac)



## Prezentare interfață web

### 1. Homepage
![Home](https://github.com/user-attachments/assets/14d04971-b7c9-4ace-9632-f881791a8756)


### 2. Characters
![Characters](https://github.com/user-attachments/assets/fa65d1cf-094e-4d2d-99fb-14c8f452919a)


### 3. Trailer
![Trailer](https://github.com/user-attachments/assets/538d544f-0017-4e2e-a44a-6d0bb7c3561c)


---

## Testare cu Pytest

Testele validează:
- codul 200 pentru fiecare rută


```bash
pytest app/tests/

```
![test](https://github.com/user-attachments/assets/a50502f8-b3dd-4215-8ed7-fc09d0f83197)

---

## Analiză statică cu Pylint

```bash
PYTHONPATH=. pylint --exit-zero app/tests/test_filme.py
PYTHONPATH=. pylint --exit-zero filme.py
```
![pylint](https://github.com/user-attachments/assets/3b753f26-3d3b-403b-99c4-492164d0dfdc)

---

## Containerizare cu Docker

```bash
sudo docker build -t interstellar-app .

sudo docker run -it --rm interstellar-app:latest

```

Aplicația devine accesibilă la: [http://localhost:5011](http://localhost:5011)

---

## Pipeline CI/CD cu Jenkins

Pipeline-ul include pașii:

1. Build
2. Analiză statică cu Pylint
3. Testare unitară cu Pytest
4. Deploy: Pornire container local (`flask-filme-container`)


Exemplu rulare cu succes:

![Jenkins](https://github.com/user-attachments/assets/8d94eb34-279d-4511-88f8-6556ee7bd9f0)

---

## Pull Request & Mentenanță

* Dezvoltarea se face pe branch `dev_Tofan_Lucian`
* Se deschide PR către `main_Tofan_Lucian`
* După review și succes pipeline, se face merge și build automat pe `main`
