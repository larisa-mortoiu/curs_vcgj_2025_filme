# Anghel Alexandru Dan
# Twilight Movie Microservice

## Overview
This Flask app is part of a uni project for cloud services & containerization. It shows basic info about the movie *Twilight*.

## Structure
- `/` – Homepage
- `/twilight` – Movie page
- `/twilight/despre` – Description
- `/twilight/actori` – Actors

## How to Run

### Docker
```bash
docker build -t twilightcont .

docker run -p 5000:5000 twilightcont
```

### Jenkins
- Run pipeline defined in `Jenkinsfile`
- Make sure `pytest` is available and targets `app/tests`

## Screenshots
_Add screenshots of container, browser, console here._

## PR Log
- [ ] Code added
- [ ] Tests passing
- [ ] Reviewed by: ___
- [ ] Merged to main
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