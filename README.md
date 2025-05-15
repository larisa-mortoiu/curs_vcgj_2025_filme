# Curs_vcgj_2025_filme

[# Achitei Mihai Alexandru](#achitei-mihai-alexandru)

[# Al Hajjih Kais](#al-hajjih-kais)

[# Anghel Alexandru Dan](#anghel-alexandru-dan)

[# Anghelina Mara](#anghelina-mara)

[# Baican Antonia Alexandra](#baican-antonia-alexandra)

[# Bancila Vlad Valentin](#bancila-vlad-valentin)

[# Camburu Mihail Whilliam](#camburu-mihail-whilliam)

[# Constantinescu Adelina Maria](#constantinescu-adelina-maria)

[# Corlan Victor Alexandru](#corlan-victor-alexandru)

[# Dina Nitoi Maria Alexandra](#dina-nitoi-maria-alexandra)

[# Dumitrache Sorana Denisa](#dumitrache-sorana-denisa)

[# Eftimie Albert Gabriele](#eftimie-albert-gabriele)

[# Gorcea Cristina](#gorcea-cristina)

[# Ichim Alexandru Ionut](#ichim-alexandru-ionut)

[# Mihalcea Larisa Maria](#mihalcea-larisa-maria)

[# Mirica Elena Ernestina](#mirica-elena-ernestina)

[# Mitrea Bogdan Gabriel](#mitrea-bogdan-gabriel)

[# Mologani Adil](#mologani-adil)

[# Mortoiu Larisa Maria](#mortoiu-larisa-maria)

[# Pham Nhat Hoang](#pham-nhat-hoang)

[# Popa Andreea Elena](#popa-andreea-elena)

[# Sandu Victor Codrin](#sandu-victor-codrin)

[# Simion Razvan Marian](#simion-razvan-marian)

[# Tofan Ionut Lucian](#tofan-ionut-lucian)

[# Zarafin Radu Adrian](#zarafin-radu-adrian)


--------------------------------------------------------------------

# Achitei Mihai Alexandru
(insereaza readme)
--------------------------------------------------------------------
# Al Hajjih Kais
(insereaza readme)
--------------------------------------------------------------------
# Anghel Alexandru Dan
(insereaza readme)
--------------------------------------------------------------------

# Anghelina Mara
-------------------------

# Cuprins
1. [Descriere aplicatie](#descriere-aplicatie)
1. [Versiune si functionalitati](#versiune-si-functionalitati)
1. [Tehnologii folosite](#tehnologii-folosite)
1. [Structura proiectului](#structura-proiectului)
1. [Configurare si instalare](#configurare-si-instalare)
1. [Prezentare interfata web](#prezentare-interfata-web)
1. [Testare cu pytest](#testare-cu-pytest)
1. [Verificare statica cu pylint](#verificare-statica-cu-pylint)
1. [Utilizare Docker si containerizare aplicatie](#utilizare-docker-si-containerizare-aplicatie)
1. [Pipeline Jenkins](#pipeline-jenkins)
1. [Pull Request](#pull-request)


# Descriere aplicatie

Proiectul „filme” reprezintă o aplicație web destinată afișării unei colecții de filme și seriale. Utilizatorii pot explora titlurile disponibile și pot accesa informații detaliate despre fiecare dintre ele precum sinopsisul și actorii principali. Platforma pune accent pe simplitate și ușurință în utilizare, oferind o interfață accesibilă pentru consultarea rapidă a conținutului. Navigarea este organizată logic: pagina de start oferă acces direct către celelalte secțiuni, iar acestea, la rândul lor, includ opțiuni de revenire către început.

Din punct de vedere tehnic, aplicația este containerizată folosind Docker, iar componentele sale sunt testate automat cu Pytest. Pentru automatizarea proceselor de instalare, testare și verificare a calității codului (prin Pylint), este configurată o soluție de integrare continuă bazată pe Jenkins.

# Versiune si functionalitati

v0 – Vizualizarea detaliilor (descriere și distribuție) și navigare intuitivă

Prima versiune a aplicației se concentrează pe afișarea unei liste de filme și seriale, fiecare element fiind însoțit de informații esențiale precum descrierea și distribuția. Platforma dispune de o interfață clară, ușor de utilizat, care permite explorarea c#Tehnoloonținutului printr-un sistem de navigație bidirecțională. Utilizatorii pot accesa cu ușurință pagina de detalii din lista principală și pot reveni rapid înapoi, fără întreruperi în fluxul de utilizare.

# Tehnologii folosite

Această aplicație a fost construită folosind un set de tehnologii care susțin atât funcționalitatea, cât și procesul de dezvoltare și testare:

- Flask – framework web ușor și flexibil, responsabil pentru logica aplicației și definirea rutelor HTTP;
- HTML & CSS – utilizate pentru structurarea conținutului și personalizarea aspectului interfeței web;
- Pytest – folosit pentru scrierea și rularea testelor unitare, asigurând corectitudinea funcțiilor;
- Pylint – pentru verificarea calității codului prin analiză statică;
- Docker – aplicat pentru crearea unui mediu izolat, portabil, prin containerizarea aplicației;
- Jenkins – automatizează execuția testelor și a verificărilor prin pipeline-uri de tip CI (integrare continuă).

# Structura proiectului

Structura aplicației este organizată astfel:

- `app/` –  conține logica principală a aplicației:

  - `lib/` – aici se află funcțiile Python responsabile pentru afișarea detaliilor legate de descriere și distribuție;

  - `test/` –  include testele unitare asociate funcțiilor definite în lib/;

- `static/` – director dedicat resurselor statice:

  - `images/` – imaginile utilizate în cadrul interfeței;

  - `styles/` – fișiere CSS pentru aspectul paginilor;

- `templates/` – conține fișierele HTML care definesc interfața aplicației (homepage, pagini cu informații despre filme etc.);

- Fișiere de configurare si rulare:

  - `filme.py` – fișierul principal care pornește aplicația Flask;

  - `Dockerfile`, `dockerstart` – necesare pentru crearea și rularea containerului Docker;

  - `Jenkinsfile` – definește pașii automatizați ai pipeline-ului în Jenkins;

  - `pytest.ini` – configurări specifice pentru rularea testelor cu Pytest;

  - `requirements` – lista cu pachetele Python necesare pentru rularea aplicației;

  - `activeaza_venv`, `start_app` – scripturi de activare a mediului virtual și pornire a aplicației.

# Configurare și rulare

## Clonare repository și configurare inițială

```text
   cd proiect/
   git clone https://github.com/larisa-mortoiu/curs_vcgj_2025_filme.git

   ********
   NOTA: INSTALARE dependinte (cu apt)

   sudo apt upgrade
   sudo apt install net-tools
   sudo apt install git
   sudo apt install python3
   sudo apt install python3-pip
   sudo apt install python3.12-venv

   cd curs_vcgj_2025_filme

   git checkout <branch_dorit>

```

## Configurare .venv și instalare pachete

Pentru activarea virtual environment, în folder-ul 'curs_vcgj_2025_filme' trebuie rulate următoarele script-uri bash:

1. `activeaza_venv` - Scriptul încearcă să activeze un virtual environment Python existent în directorul (`.venv`).  Dacă activarea reușește, afișează un mesaj de succes. Dacă nu, rulează un alt script (`activeaza_venv_jenkins`) care creează și activează un mediu virtual nou și instalează dependințele necesare.

2. `start_app` - Scriptul trebuie rulat doar după activarea venv-ului. Acesta rulează aplicația, pornind server-ul pe IP: 127.0.0.1 și port:5011. Se poate accesa din browser pe link-ul: http://127.0.0.1:5011 (sau http://localhost:5011/)

```text
mara@mara:~/proiectSCC/curs_vcgj_2025_filme$ source activeaza_venv 
    bash: .venv/bin/activate: No such file or directory
    FAIL: cannot activate venv
    Trying to create the venv in the folder: .venv
    Activating virtual environment
    Installing the dependencies
(.venv) mara@mara:~/proiectSCC/curs_vcgj_2025_filme$ . ./start_app.s
```

![start_app](https://github.com/larisa-mortoiu/curs_vcgj_2025_filme/blob/dev_Anghelina_Mara/static/images/readme_Mara/start_app.jpeg)

# Prezentare interfata web

## Pagină principală (Homepage)
Afișează o listă cu filmele disponibile, cu link-uri către pagina detaliată a fiecărui film/serial.
![homepage](https://github.com/larisa-mortoiu/curs_vcgj_2025_filme/blob/dev_Anghelina_Mara/static/images/readme_Mara/homepage.jpeg)

## Pagină film
Această pagină oferă o privire generală asupra unui film sau serial selectat, incluzând titlul și accesul rapid către paginile dedicate descrierii și distribuției.
![homepage](https://github.com/larisa-mortoiu/curs_vcgj_2025_filme/blob/dev_Anghelina_Mara/static/images/readme_Mara/gentlemen_mainpage.jpeg)

## Pagină descriere film
Conține detalii extinse despre conținutul filmului sau serialului, oferind utilizatorilor contextul narativ și tematica principală.
![gentlemen-descriere](https://github.com/larisa-mortoiu/curs_vcgj_2025_filme/blob/dev_Anghelina_Mara/static/images/readme_Mara/gentlemen_descriere.jpeg)

## Pagină distribuție film
Prezintă actorii principali și personajele interpretate, contribuind la o mai bună înțelegere a rolurilor și a distribuției producției.
![gentlemen-distributie](https://github.com/larisa-mortoiu/curs_vcgj_2025_filme/blob/dev_Anghelina_Mara/static/images/readme_Mara/gentlemen_distributie.jpeg)

# Testare cu pytest

Testarea aplicației se realizează folosind Pytest, prin teste unitare definite în fișierul `test_filme.py`, situat în directorul `app/tests/`.

Aceste teste vizează componentele principale ale aplicației:

- Testarea descrierii – verifică dacă funcția `get_description()` din modulul gentlemen_description returnează un text valid care conține elemente esențiale precum numele personajului principal și tag-uri HTML necesare afișării corecte.

- Testarea distribuției – evaluează rezultatul funcției `get_cast()` din gentlemen_cast, asigurând că returnează o listă completă de actori cu atribute precum name, character și photo, fiecare în formatul corect.


Cele două teste validează corectitudinea conținutului generat pentru pagini, nu doar existența lor, astfel:

- Validările efectuate includ:
- Confirmarea existenței unor elemente cheie precum “Eddie Horniman” sau “Theo James”;
- Asigurarea faptului că toate câmpurile actorilor sunt completate corect și că fotografiile sunt în format .jpg.

Testele sunt configurate pentru a fi rulate atât local, cât și automat, în cadrul pipeline-urilor Jenkins, oferind siguranță și stabilitate aplicației în fiecare etapă de dezvoltare.

## Testare locală 
![local-test](https://github.com/larisa-mortoiu/curs_vcgj_2025_filme/blob/dev_Anghelina_Mara/static/images/readme_Mara/local_test.jpeg)


# Verificare statica cu pylint

Pentru asigurarea calității codului sursă, aplicația utilizează Pylint, un instrument de analiză statică care inspectează:

- respectarea convențiilor de stil (spațiere, denumiri de variabile),
- utilizarea variabilelor (declarate dar nefolosite, redefinite etc.),
- structura generală a codului.

Analiza este aplicată asupra fișierelor esențiale ale aplicației:
- modulele din `app/lib/` care conțin logica pentru descriere și distribuție,
- fișierul principal `filme.py`,
- testele din `app/tests/`.

Verificările sunt integrate automat în pipeline-ul de CI (Jenkins), într-un stage dedicat – pylint - calitate cod. În cadrul acestuia, sunt rulate următoarele comenzi:

```text
    pylint --exit-zero app/lib/*.py
    pylint --exit-zero app/tests/*.py
    pylint --exit-zero filme.py
```

Opțiunea --exit-zero permite continuarea executării pipeline-ului chiar dacă sunt identificate probleme de stil sau avertismente, pentru a nu întrerupe procesul de integrare continuă.

# Utilizare Docker si containerizare aplicatie

Aplicația este containerizată folosind Docker, pentru a asigura portabilitate și rulare consecventă indiferent de mediul de execuție.

Containerizarea înseamnă „împachetarea” aplicației împreună cu toate dependințele necesare (librării, configurații, mediu virtual), astfel încât aceasta să poată fi rulată pe orice sistem care are Docker instalat, fără configurări suplimentare.

## Configurație Docker
Fișierul `Dockerfile` definește pașii pentru construirea imaginii:

- folosește imaginea de bază python:3.12-alpine;
- instalează toate pachetele din `requirements.txt;`
- creează și configurează un mediu virtual `(.venv)`;
- setează permisiuni și variabile de mediu necesare;
- expune `portul 5011` pentru aplicație;
- setează scriptul `dockerstart.sh` ca punct de intrare.

## Pornirea aplicației

Scriptul `dockerstart.sh`:

- activează mediul virtual;
- setează variabila de mediu `FLASK_APP;`
- lansează serverul Flask pe `0.0.0.0:5011`.

Această abordare asigură o rulare izolată, consistentă și ușor de replicat, indiferent de mediul în care este executată aplicația.

## Instructiuni pentru rulare aplicatie in container

Prima oara se va crea o imagine, folosind urmatoarea comanda:
```text
    sudo docker build -t mara_docker:latest .
```
Apoi, pentru a crea un container si a il rula:
```text
    sudo docker run --name mara_docker -p 8020:5011 mara_docker:latest
```
Inainte de a da start containerului, verificam daca avem atat imaginea cat si containerul:

![docker-test](https://github.com/larisa-mortoiu/curs_vcgj_2025_filme/blob/dev_Anghelina_Mara/static/images/readme_Mara/verif_docker.jpeg)

Pentru a rula aplicatia prin container com folosi urmatoarea comanda:
```text
    docker start mara_docker
```

Iar pentru a opri rularea aplicatiei:
```text
    docker stop mara_docker
```

# Pipeline Jenkins

Pentru procesul de Continuous Integration (CI), aplicația folosește Jenkins. De fiecare dată când codul este actualizat, Jenkins declanșează automat o serie de pași pentru a testa și verifica aplicația, contribuind astfel la identificarea rapidă a erorilor și menținerea calității codului.


Fișierul `Jenkinsfile` descrie etapele automate ale pipeline-ului de CI:

- `Clone repo`: Clonează automat ramura `main_Anghelina_Mara` din repository-ul GitHub:
- `Build`: creează un mediu virtual Python, îl activează și instalează toate dependințele specificate
- `Code quality`: evaluează calitatea codului sursă folosind Pylint, fără a opri pipeline-ul în caz de avertismente (prin --exit-zero):
- `Run Tests`: rulează testele unitare definite cu Pytest din mediul virtual:

Containerizare Docker: creează o imagine Docker a aplicației și pornește un container pe portul 8020, folosind un tag corespunzător build-ului curent.

Lansarea serverului Jenkins local se face prin comanda:
```text
    systemctl start jenkins
```
Pipeline-ul poate fi vizualizat într-o interfață grafică modernă și intuitivă prin extensia Blue Ocean, care oferă o imagine de ansamblu asupra fiecărui pas executat.
![pipeline](https://github.com/larisa-mortoiu/curs_vcgj_2025_filme/blob/dev_Anghelina_Mara/static/images/readme_Mara/pipeline.jpeg)


# Pull Request
Am realizat un PR din branch-ul de dezvoltare (`dev_Anghelina_Mara`) către branch-ul main (`main_Anghelina_Mara`)
![pull-request](https://github.com/larisa-mortoiu/curs_vcgj_2025_filme/blob/dev_Anghelina_Mara/static/images/readme_Mara/PR.jpeg)



--------------------------------------------------------------------
# Baican Antonia Alexandra
(insereaza readme)
--------------------------------------------------------------------
# Bancila Vlad Valentin
(insereaza readme)
--------------------------------------------------------------------
# Camburu Mihail Whilliam
(insereaza readme)
--------------------------------------------------------------------
# Constantinescu Adelina Maria
(insereaza readme)
--------------------------------------------------------------------
# Corlan Victor Alexandru
(insereaza readme)
--------------------------------------------------------------------
# Dina Nitoi Maria Alexandra
(insereaza readme)
--------------------------------------------------------------------
# Dumitrache Sorana Denisa

# CUPRINS
1. [Prezentarea generala a aplicatiei](#prezentarea-generala-a-aplicatiei)  
2. [Versiuni si functionalitati disponibile](#versiuni-si-functionalitati-disponibile)  
3. [Tehnologii utilizate](#tehnologii-utilizate)  
4. [Structura proiectului](#structura-proiectului)  
5. [Instructiuni de instalare si configurare](#instructiuni-de-instalare-si-configurare)  
6. [Interfata web prezentare](#interfata-web-prezentare)  
7. [Testare Pytest](#testare-pytest)  
8. [Analiza statica a codului cu Pylint](#analiza-statica-a-codului-cu-pylint)  
9. [Containerizare cu Docker](#containerizare-cu-docker)  
10. [Pipeline cicd cu Jenkins](#pipeline-cicd-cu-jenkins)  
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
Pagina principală (Homepage) oferă o listă cu filmele disponibile, fiecare având un link care duce către pagina detaliată a filmului sau serialului.

Pagina film afișează informații esențiale despre film/serial, inclusiv link-uri către paginile de descriere și distribuție a actorilor.

Pagini detaliate: există o pagină pentru descrierea detaliată a filmului și o altă pagină dedicată distribuției, care prezintă actorii și personajele interpretate.

## Pagina Principală (Homepage)
Această pagină afișează lista de filme disponibile. Fiecare titlu este un link care duce către pagina cu detalii specifice despre film.

![pagina-principala](https://github.com/larisa-mortoiu/curs_vcgj_2025_filme/blob/dev_Dumitrache_Denisa/static/capturi/pagina-principala.png)

## Pagina Film
Pagina dedicată fiecărui film oferă informații sumare și include linkuri către paginile ce conțin descrierea și distribuția.

![film](https://github.com/larisa-mortoiu/curs_vcgj_2025_filme/blob/dev_Dumitrache_Denisa/static/capturi/film.png)

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
--------------------------------------------------------------------
# Eftimie Albert Gabriele
(insereaza readme)
--------------------------------------------------------------------
# Gorcea Cristina
(insereaza readme)
--------------------------------------------------------------------
# Ichim Alexandru Ionut
(insereaza readme)
--------------------------------------------------------------------
# Mihalcea Larisa Maria
(insereaza readme)
--------------------------------------------------------------------
# Mirica Elena Ernestina
(insereaza readme)
--------------------------------------------------------------------
# Mitrea Bogdan Gabriel
(insereaza readme)
--------------------------------------------------------------------
# Mologani Adil
(insereaza readme)
--------------------------------------------------------------------
# Mortoiu Larisa Maria
-------------------------

# Cuprins
1. [Descriere aplicatie](#descriere-aplicatie)
1. [Versiune si functionalitati](#versiune-si-functionalitati)
1. [Tehnologii folosite](#tehnologii-folosite)
1. [Structura proiectului](#structura-proiectului)
1. [Configurare si instalare](#configurare-si-instalare)
1. [Prezentare interfata web](#prezentare-interfata-web)
1. [Testare cu pytest](#testare-cu-pytest)
1. [Verificare statica cu pylint](#verificare-statica-cu-pylint)
1. [Utilizare Docker si containerizare aplicatie](#utilizare-docker-si-containerizare-aplicatie)
1. [Pipeline Jenkins](#pipeline-jenkins)
1. [Pull Request](#pull-request)
1. [Bibliografie](#bibliografie)

# Descriere aplicatie

Aplicația "filme" constă într-o platformă web ce are ca scop principal afișarea unei liste de filme și seriale, utilizatorii având posibilitatea de a selecta fiecare film/serial în parte, pentru a accesa detalii despre acesta, precum descrierea și distribuția sa. În cadrul acesteia a fost dezvoltată o interfață web intuitivă, pentru a facilita accesul utilizatorilor la informațiile dorite.

Pentru o navigare ușoară în browser, pagina principală conține rute către toate celelalte pagini. La rândul lor, paginile conțin un link înapoi către pagina principală.

Aplicația include suport pentru containerizare printr-un Dockerfile, testare cu Pytest pentru funcțiile din `app/lib`, precum și integrare continuă prin Jenkins. Pipeline-urile automatizează instalarea dependințelor, activarea mediului virtual și rularea testelor și verificărilor statice cu Pylint.


# Versiune si functionalitati

v0 - Afișarea a două atribute (descriere și distribuție). Navigare bidirecțională.

Funcționalitatea principală implementată constă în afișarea unei liste de filme și seriale, cu detalii precum descrierea și distribuția fiecăruia. Aplicația oferă o interfață simplă, dar funcțională, pentru explorarea acestor informații. Navigarea se face prin linkuri bidirecționale între pagina principală și pagina cu detalii despre film/serial, asigurând o experiență de utilizare fluidă.

# Tehnologii folosite

Aplicația este dezvoltată folosind:

- Flask – framework web minimalist, folosit pentru logica aplicației și definirea rutelor;

- HTML și CSS – pentru structurarea și stilizarea interfeței web;

- Pytest – pentru testare unitară a componentelor aplicației;

- Pylint – pentru analiza statică a codului;

- Docker – pentru containerizarea aplicației;

- Jenkins – pentru rularea automată a testelor și verificărilor în pipeline-uri de integrare continuă.

Aplicația este una statică, fără conectare la o bază de date – datele despre filme/seriale sunt gestionate direct în cod.

# Structura proiectului

Structura aplicației este organizată astfel:

- `app/` – codul principal al aplicației:

  - `lib/` – conține funcțiile Python pentru afișarea descrierii și distribuției filmelor/serialelor;

  - `test/` – conține testele unitare pentru funcțiile din lib/;

- `static/` – resurse statice:

  - `images/` – imagini folosite în pagini;

  - `styles/` – fișiere CSS pentru stilizarea interfeței;

- `templates/` – șabloanele HTML pentru paginile aplicației: homepage, film, descriere și distribuție;

- Fișiere de configurare:

  - `filme.py` – aplicația principală Flask;

  - `Dockerfile`, `dockerstart` – pentru containerizare;

  - `jenkinsfile` – definirea pipeline-ului Jenkins;

  - `pytest.ini` – configurare Pytest;

  - `quickrequirements` – lista cu pachetele necesare;

  - `ruleaza_app`, `activeaza_venv`, `activeaza_venv_jenkins` – scripturi de pornire și configurare a mediului virtual.

![structura-proiect](https://github.com/larisa-mortoiu/curs_vcgj_2025_filme/blob/dev_Mortoiu_Larisa/static/screenshots/structura-proiect.png)

# Configurare si instalare

## Clonare repository și configurare inițială

```text
   cd Desktop/
   git clone https://github.com/larisa-mortoiu/curs_vcgj_2025_filme.git

   ********
   NOTA: INSTALARE dependinte (cu apt)

   sudo apt upgrade
   sudo apt install net-tools
   sudo apt install git
   sudo apt install python3
   sudo apt install python3-pip
   sudo apt install python3.12-venv

   cd curs_vcgj_2025_filme

   git checkout <branch_dorit>

```

## Configurare .venv și instalare pachete

Pentru activarea virtual environment, în folder-ul 'curs_vcgj_2025_filme' trebuie rulate următoarele script-uri bash:

1. `activeaza_venv` - Scriptul încearcă să activeze un virtual environment Python existent în directorul (`.venv`). Dacă activarea reușește, afișează un mesaj de succes. Dacă nu, rulează un alt script (`activeaza_venv_jenkins`) care creează și activează un mediu virtual nou și instalează dependințele necesare.

2. `ruleaza_app` - Scriptul trebuie rulat doar după activarea venv-ului. Acesta rulează aplicația, pornind server-ul pe IP: 127.0.0.1 și port:5011. Se poate accesa din browser pe link-ul: http://127.0.0.1:5011 (sau http://localhost:5011/)

![config-venv](https://github.com/larisa-mortoiu/curs_vcgj_2025_filme/blob/dev_Mortoiu_Larisa/static/screenshots/config-venv.png)


# Prezentare interfata web

## Pagină principală (Homepage)
Afișează o listă cu filmele disponibile, cu link-uri către pagina detaliată a fiecărui film/serial.
![homepage](https://github.com/larisa-mortoiu/curs_vcgj_2025_filme/blob/dev_Mortoiu_Larisa/static/screenshots/interfata-homepage.png)

## Pagină film
Conține câteva informații despre film/serial și link-urile spre paginile de descriere și distribuție.
![dynasty](https://github.com/larisa-mortoiu/curs_vcgj_2025_filme/blob/dev_Mortoiu_Larisa/static/screenshots/interfata-dynasty.png)

## Pagină descriere film
Afișează o descriere detaliată a filmului/serialului selectat.
![dynasty-descriere](https://github.com/larisa-mortoiu/curs_vcgj_2025_filme/blob/dev_Mortoiu_Larisa/static/screenshots/interfata-descriere.png)

## Pagină distribuție film
Afișează informații despre actorii din film/serial și personajele pe care aceștia le portretizează.
![dynasty-cast](https://github.com/larisa-mortoiu/curs_vcgj_2025_filme/blob/dev_Mortoiu_Larisa/static/screenshots/interfata-cast.png)

# Testare cu pytest

Pentru testarea aplicației s-au folosit teste unitare scrise cu framework-ul pytest. Testele se află în fișierul `test_filme.py`, localizat în directorul `app/tests/`.

Testele acoperă funcțiile principale din biblioteca aplicației, cum ar fi:

- Afișarea descrierii filmului/serialului - este realizată de funcția `test_dynasty_description`

- Afișarea distribuției - este realizată de funcția `test_dynasty_cast`


Cele două teste validează corectitudinea conținutului generat pentru pagini, nu doar existența lor, astfel:

- Trimite un request GET la ruta `/dynasty/description` (respectiv `/dynasty/cast`)
- Verifică dacă răspunsul are status `200 OK`.
- Compară textul HTML returnat cu descrierea așteptată din funcția `description_dy.get_description()` (analog pentru cast).
- Loghează succesul sau eroarea în funcție de validare.

Testele sunt integrate atât în rulările locale, cât și în pipeline-urile automate (Jenkins).

## Testare locală 
![testare-locala](https://github.com/larisa-mortoiu/curs_vcgj_2025_filme/blob/dev_Mortoiu_Larisa/static/screenshots/testare-locala.png)

# Verificare statica cu pylint
Pentru analiza statică a codului, se folosește Pylint, aplicat pe modulele principale ale aplicației: fișierele ce conțin funcțiile pentru cele două atribute din `app/lib`, fișierul principal `filme.py` și testele din `app/tests`.
Astfel, este evaluată calitatea scrierii codului (spații, nume de variabile, variabile declarate și neutilizate, etc.)

Verificările sunt integrate automat în pipeline-ul Jenkins, într-un stage dedicat (pylint - calitate cod), unde sunt rulate comenzile:

```text
    pylint --exit-zero app/lib/*.py
    pylint --exit-zero app/tests/*.py
    pylint --exit-zero filme.py

```
Opțiunea `--exit-zero` asigură continuarea execuției pipeline-ului chiar dacă sunt găsite probleme de stil sau avertismente, fără a opri procesul de CI.

# Utilizare Docker si containerizare aplicatie

Aplicația a fost containerizată folosind Docker pentru a asigura portabilitate și consistență între diferite sisteme. Containerizarea 
presupune „împachetarea” aplicației cu toate dependințele necesare, astfel încât să poată rula pe orice sistem, fără a depinde de configurațiile locale. În acest caz, aplicația Python este containerizată folosind Docker.

## Configurări necesare pentru containerizare. Fișierul Dockerfile
Fișierul Dockerfile definește pașii necesari pentru a construi o imagine Docker a aplicației. Folosește imaginea de bază `python:3.12-alpine`, instalează dependințele din `quickrequirements.txt`, configurează mediul virtual `(.venv)`, setează permisiuni pentru directoare și definirea variabilelor de mediu necesare. La final, expune portul 5011 și setează dockerstart.sh ca script de pornire pentru aplicație.

```text
FROM python:3.12-alpine

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
#CMD sh
```

Fișierul dockerstart.sh este responsabil cu activarea mediului virtual și pornirea aplicației Flask. Mai întâi, activează mediul virtual, setează variabila de mediu `FLASK_APP`, iar apoi pornește serverul Flask pe `0.0.0.0` și portul `5011`.

## Creare imagine container
După crearea Dockerfile, trebuie creată o imagine de container, folosind comanda:
```text
docker build -t movieimage:v1 .
```
Aceasta poate fi vizualizată astfel:

![docker-image](https://github.com/larisa-mortoiu/curs_vcgj_2025_filme/blob/dev_Mortoiu_Larisa/static/screenshots/docker-image.png)

## Creare container
Pentru a genera un container din fișierul imagine, trebuie executată comanda:

```text
docker create --name moviecontainer -p 8020:5011 movieimage:v1
```

## Execuție container
Pentru a porni containerul, folosim comanda:

```text
docker start moviecontainer
```

Containerele (active și oprite) pot fi vizualizate astfel:

```text
docker ps -a
```
![docker-container](https://github.com/larisa-mortoiu/curs_vcgj_2025_filme/blob/dev_Mortoiu_Larisa/static/screenshots/docker-container.png)

## Rularea aplicației din container
![run-app-docker](https://github.com/larisa-mortoiu/curs_vcgj_2025_filme/blob/dev_Mortoiu_Larisa/static/screenshots/run-app-docker.png)

# Pipeline Jenkins

Am folosit Jenkins pentru implementarea procesului de Continuous Integration (CI), astfel încât de fiecare dată când apar modificări asupra codului, vor fi rulate automat testele și verificările de calitate. Acest lucru ajută la detectarea rapidă a eventualelor erori și asigurarea funcționalității aplicației.

## Jenkinsfile

Fișierul Jenkinsfile definește pașii pipeline-ului de CI. Acesta automatizează testarea aplicației și verificarea calității codului la fiecare actualizare de cod. Pipeline-ul este compus din mai multe etape:

- Build: Activează mediul virtual pentru rularea comenzilor.

- Verificare cu pylint: Evaluează calitatea codului sursă din directoarele `app/lib`, `app/tests` și fișierul principal `filme.py`.

- Testare unită cu pytest: Rulează testele definite pentru funcțiile aplicației.

- Deploy în container Docker: Creează o imagine Docker cu un tag pe baza build-ului curent și pornește un container care expune aplicația pe portul 8020.

Comanda pentru pornirea Jenkins:
```text
jenkins
```
Execuția pipeline-ului este vizibilă și într-o interfață grafică prietenoasă, prin extensia Blue Ocean a Jenkins.

## Exemplu execuție pipeline Jenkins (interfață Blue Ocean)
![jenkins-blueocean](https://github.com/larisa-mortoiu/curs_vcgj_2025_filme/blob/dev_Mortoiu_Larisa/static/screenshots/jenkins-blueocean.png)

# Pull Request
Am realizat un PR din branch-ul de dezvoltare (`dev_Mortoiu_Larisa`) către branch-ul main (`main_Mortoiu_Larisa`)
![pull-request](https://github.com/larisa-mortoiu/curs_vcgj_2025_filme/blob/dev_Mortoiu_Larisa/static/screenshots/pull-request.png)

# Bibliografie

- [Flask Documentation](https://flask.palletsprojects.com/en/stable/)
- [Pytest Documentation](https://docs.pytest.org/en/latest/)
- [Docker Documentation](https://docs.docker.com/)
- [Jenkins Documentation](https://www.jenkins.io/doc/)

--------------------------------------------------------------------
# Pham Nhat Hoang
(insereaza readme)
--------------------------------------------------------------------
# Popa Andreea Elena
(insereaza readme)
--------------------------------------------------------------------
# Sandu Victor Codrin
(insereaza readme)
--------------------------------------------------------------------
# Simion Razvan Marian
(insereaza readme)
--------------------------------------------------------------------
# Tofan Ionut Lucian
(insereaza readme)
--------------------------------------------------------------------
# Zarafin Radu Adrian
(insereaza readme)
--------------------------------------------------------------------



