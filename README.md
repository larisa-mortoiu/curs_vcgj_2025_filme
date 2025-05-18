# Gorcea Cristina

---

# Cuprins

1. [Prezentare generala a aplicatiei](#prezentare-generala-a-aplicatiei)
1. [Versiune si funcționalitati disponibile](#versiune-si-functionalitati-disponibile)
1. [Tehnologii utilizate in dezvoltare](#tehnologii-utilizate-in-dezvoltare)
1. [Organizarea proiectului](#organizarea-proiectului)
1. [Instructiuni de instalare si configurare](#instructiuni-de-instalare-si-configurare)
1. [Prezentarea interfetei web](#prezentarea-interfetei-web)
1. [Testarea aplicatiei cu Pytest](#testarea-aplicatiei-cu-pytest)
1. [Analiza calitatii codului cu Pylint](#analiza-calitatii-codului-cu-pylint)
1. [Containerizarea aplicatiei cu Docker](#containerizarea-aplicatiei-cu-docker)
1. [Automatizarea prin Jenkins Pipeline](#automatizarea-prin-jenkins-pipeline)
1. [Flux de lucru colaborativ - Pull Request](#flux-de-lucru-colaborativ-pull-request)
1. [Bibliografie](#bibliografie)

# Prezentare generala a aplicatiei

Aplicația „filme” este dezvoltată pentru a oferi utilizatorilor posibilitatea de a vizualiza o colecție de filme și seriale, fiecare având pagini dedicate cu detalii precum descrierea și distribuția. Interfața aplicației este gândită pentru a fi simplă și ușor de utilizat.

Pagina principală facilitează navigarea către paginile secundare, iar acestea includ butoane de întoarcere către homepage, pentru o experiență intuitivă.

Aplicația este compatibilă cu rularea în containere Docker, include teste unitare scrise cu pytest și se integrează cu Jenkins pentru rularea automată a verificărilor și testelor.

# Versiune si funcționalitati disponibile

v0 - Afișarea a două informatii per film/serial (descriere și distribuție). Navigare bidirecțională între pagini.

Funcția principală a aplicației constă în redarea unei liste cu producții, iar fiecare are o pagină de detaliu. Interfața permite o explorare facilă a conținutului, cu linkuri clare între secțiuni.Navigarea se face prin linkuri bidirecționale între pagina principală și pagina cu detalii despre film/serial, asigurând o experiență de utilizare fluidă și plăcută.

# Tehnologii utilizate in dezvoltare

Aplicația utilizează următoarele tehnologii:

- Flask – framework-ul web principal;

- HTML & CSS – pentru dezvoltarea și stilizarea interfeței grafice;

- Pytest – pentru validare automată a funcționalităților;

- Pylint – pentru analiza stilului codului;

- Docker – pentru ambalarea și rularea aplicației în containere;

- Jenkins – pentru implementarea CI (Continuous Integration) -> pipeline-uri de integrare continuă.

Datele aplicației sunt hardcodate în codul sursă, fără folosirea unei baze de date externe.

# Organizarea proiectului

Structura proiectului este organizată în următorul mod:

- `app/` – conține codul principal al aplicației:

  - `lib/` – conține funcțiile Python pentru detalii legate de descrierea și distribuția filmelor/serialelor;

  - `tests/` – conține testele unitare pentru lib/;

- `static/` – resurse statice:

  - `images/` – imagini folosite în interfa;

  - `styles/` – fișiere CSS pentru stilizarea interfeței web;

- `templates/` – șabloanele HTML pentru paginile aplicației: homepage, film, descriere și distribuție;

- Fișiere de configurare:

  - `filme.py` – aplicația principală;

  - `Dockerfile`, `dockerstart` – configurare Docker;

  - `jenkinsfile` – definirea pipeline-ului Jenkins;

  - `pytest.ini` – configurare testare cu Pytest;

  - `quickrequirements` – lista cu pachetele necesare;

  - `ruleaza_app`, `activeaza_venv`, `activeaza_venv_jenkins` – scripturi auxiliare de pornire și configurare a mediului virtual.

![organizarea-proiectului]()

# Instructiuni de instalare si configurare

## Navigare în Desktop

```text
   cd Desktop/
```

## Clonare repository și configurare inițială

```text
   git clone https://github.com/larisa-mortoiu/curs_vcgj_2025_filme.git

   ********
   NOTA: INSTALARE dependințe (dacă lipsesc)

   sudo apt update
   sudo apt upgrade
   sudo apt install -y net-tools git python3 python3-pip python3.10-venv

```

## Navigare în proiect

```text
   cd curs_vcgj_2025_filme
   git checkout <branch_dorit>
```

## Configurare .venv și instalare pachete

Pentru activarea virtual environment (mediului virtual), se rulează următoarele script-uri bash, în folder-ul 'curs_vcgj_2025_filme':

1. `activeaza_venv` - Acest script verifică dacă există un mediu virtual Python în directorul (`.venv`). Dacă îl găsește, îl activează și afișează un mesaj de confirmare. În cazul în care mediul virtual nu este prezent, scriptul apelează automat (`activeaza_venv_jenkins`), care creează un nou mediu virtual și instalează toate dependințele necesare din fișierul de requirements.

2. `ruleaza_app` - Acest script se folosește numai după ce mediul virtual a fost activat. El pornește aplicația Flask, care va rula pe IP-ul local 127.0.0.1 și portul 5011. Aplicația poate fi accesată în browser la adresa: http://127.0.0.1:5011 sau http://localhost:5011.

### Comenzi de activare și rulare

```text
# Activarea mediului virtual (virtual environment)
. ./activeaza_venv.sh

# Pornire aplicație
. ./ruleaza_app.sh
```

![configurare-venv]()

# Prezentarea interfetei web

## Pagină principală (Homepage)

Afișează lista cu filmele disponibile, cu acces rapid prin link-uri către pagina cu detalii a fiecărui film/serial.
![homepage]()

## Pagină film

Include o scurtă prezentarea despre film/serial și două butoane către paginile de descriere și distribuție.
![stranger-things]()

## Pagină descriere film

Oferă detalii extinse despre filmul/serialul ales.
![stranger-things-descriere]()

## Pagină distribuție film

Prezintă actorii principali și personajele interpretate.
![stranger-things-distributie]()

# Testarea aplicatiei cu Pytest

Pentru validarea aplicației au fost implementate teste unitare utilizând framework-ul pytest. Aceste teste sunt definite în fișierul `test_filme.py`, aflat în directorul `app/tests/`.

Testele vizează funcțiile esentțiale din logica aplicației, anume:

- Afișarea descrierii filmului/serialului - verificată de funcția `test_descriere_st`

- Afișarea distribuției - verificată de funcția `test_distributie_st`

## Scopul testelor

Scopul testelor este de a verifica nu doar existența paginilor, ci și corectitudinea conținutului HTML generat. Fiecare test:

- Trimite un request GET la ruta `/descriere` (respectiv `/distributie`)
- Verifică dacă răspunsul are statusul HTTP `200 OK`.
- Compară conținutul returnat cu valoarea generată de funcțiile descriere_st.get_descriere() și respectiv descriere_st.get_distributie().
- Afișează în consolă un mesaj corespunzător în funcție de rezultat (succes sau eroare)

Aceste teste sunt incluse atât în procesul de rulare locală, cât și în pipeline-ul de integrare continuă configurat prin Jenkins.

## Testare locală

![testare-locala]()

# Analiza calitatii codului cu Pylint

Pentru evaluarea calității codului sursă, aplicația utilizează instrumentul Pylint, care analizează fișierele esențiale ale proiectului: modulele din app/lib (responsabile pentru afișarea descrierii și distribuției), fișierul principal filme.py și testele din app/tests.

Analiza statică urmărește aspecte precum:

- Respectarea convențiilor PEP8,

- Utilizarea corectă a spațiilor și indentării,

- Denumirea sugestivă a variabilelor,

- Evitarea variabilelor neutilizate sau redundante.

Verificările sunt automatizate în cadrul pipeline-ului Jenkins, într-o etapă special destinată verificării stilului de cod (pylint - calitate cod). În această etapă sunt executate următoarele comenzi:

```text
    pylint --exit-zero app/lib/*.py
    pylint --exit-zero app/tests/*.py
    pylint --exit-zero filme.py

```

Utilizarea opțiunii --exit-zero permite ca pipeline-ul să continue execuția chiar și atunci când Pylint identifică probleme sau avertismente, fără a opri procesul de integrare continuă.

# Containerizarea aplicatiei cu Docker

Aplicația a fost containerizată cu ajutorul Docker pentru a asigura portabilitate, independență față de mediul local și o rulare uniformă pe orice sistem. Procesul de containerizare constă în ambalarea aplicației împreună cu toate dependințele necesare într-o imagine Docker, astfel încât aceasta să poată fi executată oriunde, fără a necesita configurări suplimentare ale mediului. În cazul de față, aplicația Python este complet containerizată utilizând un fișier Dockerfile dedicat.

## Configurări necesare pentru containerizare. Fișierul Dockerfile

Fișierul Dockerfile descrie pașii necesari pentru construirea imaginii Docker a aplicației. Acesta utilizează ca bază imaginea python:3.10-alpine, după care instalează toate pachetele specificate în quickrequirements.txt, creează un mediu virtual în directorul .venv, și configurează permisiunile corespunzătoare pentru directoarele aplicației. De asemenea, sunt definite variabilele de mediu esențiale pentru rularea aplicației. La final, portul 5011 este expus, iar fișierul dockerstart.sh este desemnat ca script de inițializare pentru container.

```text
FROM python:3.12-alpine

ENV FLASK_APP filme
#ENV FLASK_CONFIG = docker

#3.10 alpine
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

Scriptul dockerstart.sh are rolul de a activa mediul virtual și de a inițializa aplicația Flask. Acesta activează mai întâi environment-ul virtual, configurează variabila de mediu FLASK_APP, iar ulterior lansează serverul Flask pe adresa 0.0.0.0, utilizând portul 5011.

## Creare imagine container

După crearea Dockerfile, este necesară crearea unei imagini de container, folosind comanda:

```text
docker build -t movieimage:v1 .
```

Imaginea creată poate fi vizualizată astfel:

![docker-image]()

## Creare container

Pentru generarea unui container din fișierul imagine, trebuie utilizată comanda:

```text
docker create --name moviecontainer -p 8020:5011 movieimage:v1
```

## Execuție container

Pentru pornirea containerul, se utilizează comanda:

```text
docker start moviecontainer
```

Containerele (atât active cât și oprite) pot fi vizualizate astfel:

```text
docker ps -a
```

![docker-container]()

## Rularea aplicației din container

![run-app-docker]()

# Automatizarea prin Jenkins Pipeline

Jenkins a fost utilizat pentru implementarea procesului de integrare continuă (CI), astfel încât, la fiecare modificare adusă codului sursă, testele automate și verificările de calitate sunt executate automat. Acest mecanism contribuie la identificarea rapidă a erorilor și la menținerea funcționalității corecte a aplicației pe parcursul dezvoltării.

## Jenkinsfile

Fișierul Jenkinsfile descrie pașii necesari pentru executarea pipeline-ului de integrare continuă. Acesta automatizează procesul de testare și verificare a aplicației la fiecare actualizare a codului sursă. Pipeline-ul este structurat în mai multe etape distincte:

- Build: Inițializează și activează mediul virtual pentru a pregăti rularea comenzilor necesare.

- Analiză cu Pylint: Verifică stilul și calitatea codului în modulele din `app/lib`, testele din `app/tests` și în fișierul principal `filme.py`.

- Testare unitară cu Pytest: Rulează testele definite pentru funcțiile aplicației pentru a valida comportamentul corect al logicii implementate.

-Deploy într-un container Docker: Creează o imagine Docker etichetată cu numărul build-ului curent și lansează un container care expune aplicația pe portul 8020.

Comanda pentru pornirea Jenkins:

```text
jenkins
```

Execuția pipeline-ului este vizibilă și într-o altă interfață grafică prin extensia Blue Ocean a Jenkins.

## Exemplu execuție pipeline Jenkins (interfață Blue Ocean)

![jenkins-blueocean]()

# Flux de lucru colaborativ - Pull Request

Am creat un PR(Pull Request) din branch-ul de dezvoltare (`dev_Gorcea_Cristina`) către branch-ul main (`main_Gorcea_Cristina`)
![pull-request]()

# Bibliografie

- [HTML Documentation ]()
- [CSS Documentation ]()
- [Flask Documentation](https://flask.palletsprojects.com/en/stable/)
- [Pytest Documentation](https://docs.pytest.org/en/latest/)
- [Docker Documentation](https://docs.docker.com/)
- [Jenkins Documentation](https://www.jenkins.io/doc/)
