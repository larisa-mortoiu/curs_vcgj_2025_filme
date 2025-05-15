# DUMITRACHE SORANA DENISA

# CUPRINS
1. [Prezentarea generală a aplicației](#prezentarea-generala-a-aplicatiei)  
2. [Versiuni și funcționalități disponibile](#versiuni-si-functionalitati-disponibile)  
3. [Tehnologii utilizate](#tehnologii-utilizate)  
4. [Structura proiectului](#structura-proiectului)  
5. [Instrucțiuni de instalare și configurare](#instructiuni-de-instalare-si-configurare)  
6. [Interfața web - prezentare](#interfata-web---prezentare)  
7. [Testare Pytest](#testare-pytest)  
8. [Analiză statică a codului cu Pylint](#analiza-statica-a-codului-cu-pylint)  
9. [Containerizare cu Docker](#containerizare-cu-docker)  
10. [Pipeline CI/CD cu Jenkins](#pipeline-cicd-cu-jenkins)  
11. [Procedura Pull Request](#procedura-pull-request)  
12. [Bibliografie](#bibliografie)  

# Prezentarea generală a aplicației
 Aplicația web "MovieHub" oferă o platformă simplă pentru filme și seriale, permițând utilizatorilor să exploreze detalii specifice fiecărui titlu, cum ar fi descrierea și distribuția actorilor. Interfața este construită pentru a asigura o experiență clară și ușor de folosit.

Navigarea este facilitată printr-un meniu principal care conduce către paginile de detalii, iar fiecare pagină conține un link de revenire către ecranul principal.

Aplicația suportă containerizarea folosind Docker, iar pentru asigurarea calității codului și automatizarea testelor se folosesc Pytest și Jenkins, care gestionează un pipeline de integrare continuă ce activează mediul virtual, instalează dependențele și rulează testele și verificările statice.

# Versiuni și funcționalități disponibile
Funcționalitățile implementate includ afișarea a două caracteristici principale: descrierea filmelor/serialelor și distribuția actorilor. Navigarea se realizează bidirecțional între pagina principală și paginile de detalii pentru o utilizare facilă.

Versiunea curentă: v0. 
Funcționalitățile implementate:
- Pagina principală cu rută către un film.
- Pagini dedicate pentru: descriere, distribuție.
- Navigare între pagini.
- Separarea logicii în module Python.
- Teste unitare cu Pytest.
- Verificare cod cu Pylint.
- Pipeline Jenkins pentru testare automată.
- Suport pentru rulare în Docker.

# Tehnologii utilizate
- **Flask** – framework web folosit pentru crearea rutelor și gestionarea logicii aplicației;  
- **HTML & CSS** – pentru realizarea structurii și designului paginilor web;  
- **Pytest** – utilizat pentru testarea unitară a componentelor interne;  
- **Pylint** – pentru evaluarea calității și conformității codului Python;  
- **Docker** – containerizarea aplicației pentru medii consistente de rulare;  
- **Jenkins** – pentru automatizarea proceselor de build, testare și integrare continuă.

# Structura proiectului
- `app/` – codul sursă al aplicației:  
  - `lib/` – module Python ce furnizează date despre filme și distribuție;  
  - `tests/` – teste unitare pentru funcțiile din `lib/`;  
- `static/` – resurse statice:  
  - `images/` – imagini utilizate în paginile web;  
  - `styles/` – fișiere CSS pentru aspectul vizual;  
- `templates/` – șabloane HTML pentru toate paginile web: pagina principală, detalii filme, descriere și distribuție;  
- Fișiere de configurare și scripturi:  
  - `filme.py` – scriptul principal al aplicației Flask;  
  - `Dockerfile`, `dockerstart.sh` – fișiere pentru containerizare;  
  - `Jenkinsfile` – definiția pipeline-ului Jenkins;  
  - `pytest.ini` – configurarea testelor Pytest;  
  - `quickrequirements.txt` – lista pachetelor necesare pentru mediul virtual;  
  - Scripturi de configurare și rulare: `ruleaza_app.sh`, `activeaza_venv`, `activeaza_venv_jenkins`.

```text
curs_vcgj_2025_filme/
├── app/
│ ├── lib/
│ │ ├── descriere.py
│ │ └── cast.py
│ └── tests/
│ ├── tests/
│   └── test_filme.py
├── static/
│ ├── images/
│ └── screenshots/
├── templates/
│ ├── home_film.html
│ ├── film.html
│ ├── descriere.html
│ └── cast.html
├── filme.py
├── Dockerfile
├── dockerstart
├── jenkinsfile
├── pytest.ini
├── quickrequirements
├── ruleaza_app.sh
├── activeaza_venv.sh
└── activeaza_venv_jenkins.sh
```

# Instrucțiuni de instalare și configurare

## Configurare și instalare

Instrucțiuni pentru configurarea aplicației pe mașina virtuală locală (user: *denisa*):

```text
# 1. Navigare în Desktop
cd ~/Desktop/

# 2. Clonare repository (dacă nu există deja)
git clone https://github.com/larisa-mortoiu/curs_vcgj_2025_filme.git

# 3. Navigare în folderul proiectului
cd curs_vcgj_2025_filme

# 4. Checkout pe branch-ul propriu
git checkout dev_Dumitrache_Denisa

# ********
# NOTĂ: Instalare dependințe (dacă lipsesc)
sudo apt update
sudo apt install -y net-tools git python3 python3-pip python3.10-venv

# 5. Activare mediu virtual (cu script)
. ./activeaza_venv.sh

# 6. Instalare pachete Python
pip install -r quickrequirements

# 7. Rulare aplicație Flask
. ./ruleaza_app.sh
```

## Configurare `.venv` și instalare pachete

Pentru activarea mediului virtual (`virtual environment`) în folder-ul `curs_vcgj_2025_filme`, trebuie rulate următoarele scripturi bash:

- **`activeaza_venv`**  
  Acest script încearcă să activeze un mediu virtual Python existent în directorul `.venv`.  
  - Dacă activarea reușește, afișează un mesaj de succes.  
  - Dacă nu, rulează un alt script `activeaza_venv_jenkins`, care creează și activează un mediu virtual nou și instalează dependințele necesare.

- **`ruleaza_app`**  
  Acest script trebuie rulat doar după activarea mediului virtual.  
  El pornește aplicația, inițiind server-ul pe IP-ul `127.0.0.1` și portul `5011`.  
  Aplicația poate fi accesată din browser la adresa:  
  `http://127.0.0.1:5011` sau `http://localhost:5011/`.

### Comenzi pentru activare și rulare:

```text
# Activare mediu virtual
. ./activeaza_venv.sh

# Pornire aplicație Flask
. ./ruleaza_app.sh
```
![configurare-venv](https://github.com/larisa-mortoiu/curs_vcgj_2025_filme/blob/dev_Dumitrache_Denisa/static/capturi/configurare-venv.png)

# Interfața web - prezentare
# Prezentare Interfață Web

## Pagina Principală (Homepage)
Această pagină afișează lista de filme disponibile. Fiecare titlu este un link care duce către pagina cu detalii specifice despre film.

![pagina-principala](https://github.com/larisa-mortoiu/curs_vcgj_2025_filme/blob/dev_Dumitrache_Denisa/static/capturi/pagina-principala.png)

## Pagina Film
Pagina dedicată fiecărui film oferă informații sumare și include linkuri către paginile ce conțin descrierea și distribuția.

![film]https://github.com/larisa-mortoiu/curs_vcgj_2025_filme/blob/dev_Dumitrache_Denisa/static/capturi/film.png()

## Pagina Descriere Film
Aici utilizatorii pot citi o descriere detaliată despre filmul  ales.

![descriere-film](https://github.com/larisa-mortoiu/curs_vcgj_2025_filme/blob/dev_Dumitrache_Denisa/static/capturi/descriere-film.png)

## Pagina Distribuție Film
Această pagină oferă informații despre actorii din film și rolurile pe care le interpretează.

![cast-film](https://github.com/larisa-mortoiu/curs_vcgj_2025_filme/blob/dev_Dumitrache_Denisa/static/capturi/cast-film.png)

# Testare Pytest
Pentru a asigura funcționarea corectă a aplicației, au fost dezvoltate teste unitare folosind framework-ul `pytest`. Acestea sunt definite în fișierul `test_filme.py`, aflat în directorul `app/tests/`.

Testele validează funcționalitățile cheie ale aplicației:

- **Afișarea descrierii** filmului, verificată prin testul `test_descriere_apare_corect`
- **Afișarea distribuției actorilor**, verificată prin testul `test_cast_apare_corect`

### Ce face fiecare test:
- Trimite o cerere HTTP `GET` către rutele dedicate (`/How-to-lose-a-guy-in-10-days-descriere` și `How-to-lose-a-guy-in-10-days-cast`)
- Verifică dacă răspunsul are codul de stare `200 OK`
- Compară conținutul HTML returnat cu rezultatul așteptat, generat de funcțiile `descriere_film.get_descriere()` și `cast_film.get_cast()`

Testele nu doar confirmă existența paginilor, ci și faptul că informațiile afișate sunt cele corecte. Ele sunt rulate atât local, cât și automat, prin pipeline-ul configurat în Jenkins.

![testare-locala-pytest](https://github.com/larisa-mortoiu/curs_vcgj_2025_filme/blob/dev_Dumitrache_Denisa/static/capturi/testare-locala-pytest.png)

# Analiză statică a codului cu Pylint 
Pentru analiza statică a codului sursă, este utilizat pylint, aplicat pe modulele cheie ale aplicației: funcțiile definite în app/lib, fișierul principal filme.py, precum și testele din app/tests.

Această analiză ajută la identificarea unor probleme de stil și scriere a codului, precum:

Spațieri necorespunzătoare

Nume de variabile neconforme

Variabile declarate și neutilizate

Alte avertismente privind calitatea codului

Verificările sunt integrate într-un stage dedicat în pipeline-ul Jenkins, sub denumirea pylint - calitate cod. Comenzile rulate automat sunt:

```text
pylint --exit-zero app/lib/*.py
pylint --exit-zero app/tests/*.py
pylint --exit-zero filme.py

```

# Containerizare cu Docker
Pentru a asigura portabilitatea și funcționarea unitară în diverse medii, aplicația a fost containerizată folosind Docker. Această abordare garantează că aplicația rulează cu toate dependențele sale, indiferent de sistemul pe care este implementată.

Dockerfile – configurarea imaginii
Fișierul Dockerfile definește pașii necesari pentru construirea imaginii Docker. Acesta:

Utilizează imaginea de bază python:3.12-alpine

Copiază fișierele aplicației

Creează mediul virtual

Instalează dependențele din quickrequirements.txt

Expune portul 5011

Specifică scriptul de start dockerstart.sh ca punct de intrare

```text
FROM python:3.10-alpine

ENV FLASK_APP filme
#ENV FLASK_CONFIG = docker

#3.12 alpine
RUN adduser -D filme

USER filme

WORKDIR /home/filme/

COPY app app
COPY static static
COPY templates templates
COPY dockerstart.sh dockerstart.sh
COPY pytest.ini pytest.ini
COPY quickrequirements.txt quickrequirements.txt
COPY filme.py filme.py

USER root   
RUN chmod -R 777 static

RUN python3 -m venv .venv
RUN chmod -R g+x .venv
RUN chmod +x dockerstart.sh

RUN .venv/bin/pip install -r quickrequirements.txt


# runtime configuration
EXPOSE 5011
ENTRYPOINT ["./dockerstart.sh"]
#CMD sh 
```
Prin rularea scriptului dockerstart.sh, se inițializează mediul virtual și se lansează serverul Flask în modul de producție, disponibil pe adresa 0.0.0.0:5011 din interiorul containerului.

## Construirea și rularea containerului
Construire imagine: 
```text
docker build -t movieimage:v3 .
```
Vizualizare imagine:

![creare-imagine](https://github.com/larisa-mortoiu/curs_vcgj_2025_filme/blob/dev_Dumitrache_Denisa/static/capturi/creare-imagine.png)

## Creare container:
```text
docker create --name moviecontainer -p 8020:5011 movieimage:v3
```
## Pornire container:
```text
docker start moviecontainer
```
## Listare containere:
```text
docker ps -a
```
Execuția aplicației :
După pornirea containerului, aplicația devine disponibilă pe adresa:
http://localhost:8020
![rulare-container](https://github.com/larisa-mortoiu/curs_vcgj_2025_filme/blob/dev_Dumitrache_Denisa/static/capturi/rulare-container.png)
![aplicatie-din-container](https://github.com/larisa-mortoiu/curs_vcgj_2025_filme/blob/dev_Dumitrache_Denisa/static/capturi/aplicatie-din-container.png)


# Pipeline CI/CD cu Jenkins
## Integrare continuă cu Jenkins
Aplicația este integrată cu Jenkins pentru implementarea unui proces de tip CI (Continuous Integration). Astfel, la fiecare commit sau push în repository-ul remote, se declanșează automat un pipeline care:

Activează mediul virtual

Rulează verificări de stil cu pylint

Execută testele unitare cu pytest

Construiește și pornește aplicația într-un container Docker

## Jenkinsfile
Fișierul Jenkinsfile descrie etapele acestui pipeline și gestionează întregul proces automat:

Build: Pregătirea mediului pentru execuție

Analiză cod: Evaluarea calității codului cu pylint

Testare: Rulare teste unitare

Deploy: Construirea și lansarea containerului Docker
Comanda pentru lansarea Jenkins:
```text
jenkins
```
 Execuție vizuală în Jenkins (Blue Ocean):
 ![Blue-ocean](https://github.com/larisa-mortoiu/curs_vcgj_2025_filme/blob/dev_Dumitrache_Denisa/static/capturi/Blue-ocean.png)

 Pull Request
Modificările realizate în branch-ul de dezvoltare (dev_Dumitrache_Denisa) au fost propuse pentru integrare în ramura principală (main_Dumitrache_Denisa) printr-un Pull Request (PR):

pull-request

# Bibliografie

- [Flask Documentation](https://flask.palletsprojects.com/en/stable/) – Documentația oficială Flask, framework-ul web Python folosit în proiect.
- [Pytest Documentation](https://docs.pytest.org/en/latest/) – Ghidul oficial pentru framework-ul de testare pytest.
- [Docker Documentation](https://docs.docker.com/) – Resurse oficiale pentru containerizarea aplicațiilor cu Docker.
- [Jenkins Documentation](https://www.jenkins.io/doc/) – Documentația oficială a Jenkins, serverul de automatizare pentru CI/CD.
- [Python Documentation](https://docs.python.org/3/) – Documentația oficială Python.
- [Pylint Documentation](https://pylint.pycqa.org/en/latest/) – Documentația pentru instrumentul de analiză statică a codului Python, Pylint.
- [Git Documentation](https://git-scm.com/doc) – Manualul oficial pentru sistemul de control al versiunilor Git.
