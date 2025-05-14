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
!!!!!!!!!!!!!!!!!!!!!!!SCREENSHOT structura-proiect!!!!!!!!!!!!!!!!!!!!!!!!!!!!

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

!!!!!!!!!!!!!!!!!!!!!SCREENSHOT config-venv!!!!!!!!!!!!!!!!!!!!!!!


# Prezentare interfata web

## Pagină principală (Homepage)
Afișează o listă cu filmele disponibile, cu link-uri către pagina detaliată a fiecărui film/serial.
!!!!!!!!!!!!!!!!!!!!!SCREENSHOT!!!!!!!!!!!!!!!!!!!!!!!

## Pagină film
Conține câteva informații despre film/serial și link-urile spre paginile de descriere și distribuție.
!!!!!!!!!!!!!!!!!!!!!SCREENSHOT!!!!!!!!!!!!!!!!!!!!!!!

## Pagină descriere film
Afișează o descriere detaliată a filmului/serialului selectat.
!!!!!!!!!!!!!!!!!!!!!SCREENSHOT!!!!!!!!!!!!!!!!!!!!!!!

## Pagină distribuție film
Afișează informații despre actorii din film/serial și personajele pe care aceștia le portretizează.
!!!!!!!!!!!!!!!!!!!!!SCREENSHOT!!!!!!!!!!!!!!!!!!!!!!!

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
!!!!!!!!!!!!!!!!!!!!!SCREENSHOT CONSOLA PYTEST!!!!!!!!!!!!!!!!!!!!!!!

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

!!!!!!!!!!!!!!!!!!!!!SCREENSHOT IMAGINE CREATA!!!!!!!!!!!!!!!!!!!!!!!

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
!!!!!!!!!!!!!!!!!!!!!SCREENSHOT CONTAINER CREAT PE BAZA IMAGINII!!!!!!!!!!!!!!!!!!!!!!!

## Rularea aplicației din container
!!!!!!!!!!!!!!!!!!!!!SCREENSHOT APP DESCHISA IN BROWSER!!!!!!!!!!!!!!!!!!!!!!!

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
!!!!!!!!!!!!!!!!!!!!!SCREENSHOT DIN BLUEOCEAN!!!!!!!!!!!!!!!!!!!!!!!

# Pull Request
Am realizat un PR din branch-ul de dezvoltare (`dev_Mortoiu_Larisa`) către branch-ul main (`main_Mortoiu_Larisa`)
!!!!!!!!!!!!!!!!!!!!!SCREENSHOT PR!!!!!!!!!!!!!!!!!!!!!!!

# Bibliografie