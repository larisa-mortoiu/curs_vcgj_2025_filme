# Anghel Alexandru Dan
# Twilight Movie Microservice

### Docker
```bash
docker build -t twilightcont .

docker run -p 5000:5000 twilightcont
```

### Jenkins
- Run pipeline defined in `Jenkinsfile`
- Make sure `pytest` is available and targets `app/tests`

## Screenshots




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

Proiectul „Filme” este o aplicație web bazată pe Flask, concepută pentru a prezenta filme și seriale TV, cu accent pe Twilight (2008), primul film din saga de dragoste cu vampiri a lui Stephenie Meyer, cu Kristen Stewart și Robert Pattinson în rolurile principale. Aplicația oferă detalii cum ar fi intriga filmului (drama supranaturală a Bellei cu Edward în Forks, Washington), teme, succesul de box office (393 milioane USD la nivel global) și specificații tehnice. Creată pentru un curs universitar despre servicii cloud, aplicația este containerizată cu Docker pentru portabilitate, testată prin Jenkins (folosind Pytest pentru funcționalitate și Pylint pentru calitatea codului) și controlată prin versiune pe GitHub. Dispune de o interfață minimalistă, design receptiv și o conductă CI/CD pentru testare/implementare automată, demonstrând abilități în containerizare, automatizare și principii native din cloud.


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
```plaintext
C:.
|   .gitignore
|   Dockerfile
|   filme.py
|   Jenkinsfile
|   LICENSE
|   README.md
|   requirements.txt
|
+---app
|   |   filme.py
|   |
|   +---lib
|   |       actori.py
|   |       descriere.py
|   |
|   +---templates
|   |       actori.html
|   |       despre.html
|   |       home.html
|   |       twilight.html
|   |
|   \---tests
|           test_actori.py
|           test_descriere.py
|
\---static
        App1.png
        App2.png
        App3.png
        App4.png
        Capture.PNG
        Capture2.PNG
```

# Configurare și rulare

## Clonare repository și configurare inițială

```plaintext
   cd SCC/Proiect
   git clone https://github.com/larisa-mortoiu/curs_vcgj_2025_filme.git

   sudo apt upgrade
   sudo apt install net-tools
   sudo apt install git
   sudo apt install python3
   sudo apt install python3-pip
   sudo apt install python3.12-venv

   cd curs_vcgj_2025_filme

   git checkout <branch_dorit>

   docker build -t twilight-app . 
   docker run -p 5000:5000 twilight-app
```
Va apărea log-ul

```plaintext
* Serving Flask app 'filme'
 * Debug mode: off
 * Running on all addresses (0.0.0.0)
 * Running on http://127.0.0.1:5000
 * Running on http://172.17.0.2:5000
Press CTRL+C to quit
```

Si se apasă ctrl+click pe web socket-ul `http://127.0.0.1:5000`

![Capture](https://github.com/user-attachments/assets/3bce3630-e82f-490d-ac71-229fe81c0cf8)
![Capture2](https://github.com/user-attachments/assets/0be74b49-7a53-4e30-844c-b780cad949bf)


# Prezentare interfata web

## Pagină principală (Homepage)
Ar trebui să afișeze o listă cu filmele disponibile. Habar n-am cum se face asta. :(

## Pagină film
Se pornește de la o pagină de index ce duce către pagina principală a filmului, de unde se pot accesa mai departe paginile aferente descrierii și distribuției actorilor

![App1](https://github.com/user-attachments/assets/5594926f-05ac-4ec5-bec5-3f1afe312d76)
![App2](https://github.com/user-attachments/assets/6d4b0dd3-243d-4ca3-838b-e5602bff1ba5)

## Pagină descriere film
Conține detalii extinse despre conținutul filmului sau serialului, oferind utilizatorilor contextul narativ și tematica principală.

![App3](https://github.com/user-attachments/assets/2bcfb214-19da-4928-b1d9-d929eb54df05)

## Pagină distribuție film
Prezintă actorii principali și personajele interpretate, contribuind la o mai bună înțelegere a rolurilor și a distribuției producției.

![App4](https://github.com/user-attachments/assets/068f4839-3002-42b1-bc55-c8d5817bcbb1)


# Testare cu pytest

Fișierul de testare (test_actori.py) folosește pytest pentru a valida comportamentul funcției `actori_twilight()` din app/lib/actori.py.

Scop: Se asigură că funcția `actori_twilight()` returnează date nevide.
Cum funcționează:
Apelează `actori_twilight()` pentru a obține lista de actori.

`Assert len()` verifică dacă conținutul rezultatului nu este gol

Apoi se verifică dacă actorii principali din seria Twilight sunt incluși în date.

Cum funcționează: Apelează `actori_twilight()` și convertește rezultatul în minuscule.
Verifică dacă sunt prezente șirurile „kristen stewart”, „robert pattinson” și „taylor lautner”.

Șablonul actori.html folosește datele din actori_twilight() pentru a reda informații despre actor. Testele asigură:

Utilizați pytest pentru a executa testele:

`pytest app/tests/test_actori.py`

Codul de testare (test_descriere.py) validează funcționalitatea funcției descriere_twilight() din descriere.py, care generează o descriere formatată Markdown a filmului Twilight. Primul test, test_descriere_not_empty, asigură că funcția returnează un șir nevid prin eliminarea spațiilor albe și afirmând că rezultatul nu este gol. Al doilea test, test_descriere_has_keywords, verifică prezența cuvintelor cheie esențiale, cum ar fi „Bella”, „vampir” și „Twilight” (indiferență între majuscule și minuscule) pentru a confirma că descrierea acoperă temele de bază. Aceste teste asigură datele redate în despre.html—care folosește ieșirea descriere_twilight() prin intermediul {{ descriere | safe }} variabilă șablon — este atât nevide, cât și exactă din punct de vedere contextual. Deși testele existente sunt funcționale, ele ar putea fi îmbunătățite prin verificarea anumitor secțiuni (de exemplu, antete precum „### 🧛 Teme cheie”), validarea sintaxei Markdown sau verificarea cuvintelor cheie suplimentare (de exemplu, „dragoste interzisă”, „Catherine Hardwicke”). Rularea acestor teste cu pytest confirmă integritatea descrierii, asigurându-se că șablonul HTML afișează conținut semnificativ fără erori. Cazurile marginale, cum ar fi codificarea specială a caracterelor sau gestionarea întreruperilor de linie, ar trebui să fie, de asemenea, luate în considerare pentru a menține consistența interfeței de utilizare.

Utilizați pytest pentru a executa testele:

`pytest app/tests/test_descriere.py`

# Utilizare Docker si containerizare aplicatie

Aplicația este containerizată folosind Docker , o tehnologie care asigură portabilitate maximă și rulare consecventă în orice mediu de execuție, fie acesta un server local, un cloud sau un dispozitiv de testare. Containerizarea reprezintă procesul de "împachetare" a aplicației împreună cu toate dependințele sale critice (librării Python, configurații specifice, variabile de mediu și chiar un sistem de fișiere virtualizat), garantând că aplicația funcționează identic pe orice sistem care are Docker instalat, fără a necesita configurări manuale sau ajustări post-deploy. Această abordare elimină riscul discrepanțelor între medii (cum ar fi "funcționa pe mașina mea"), oferind izolare totală a resurselor și scalabilitate eficientă . Docker permite, de asemenea, definirea precisă a infrastructurii prin fișiere Dockerfile, care automatizează construirea containerelor și asigură reproductibilitatea procesului de deploy, de la dezvoltare până la producție.

## Configurație Docker
Fișierul `Dockerfile` definește infrastructura pentru containerizarea aplicației, urmând acești pași cheie:

Imagine de bază minimală : Folosește `python:3.10-slim` (o variantă redusă a imaginii Python 3.10) pentru a minimiza dimensiunea containerului, păstrând totuși funcționalitatea necesară.
Configurare director de lucru : Setează `/app` ca director de lucru în container și copiază întregul conținut al proiectului în acesta.
Instalare dependințe : Rulează `pip install` pentru a instala pachetele specificate în `requirements.txt`, folosind `--no-cache-dir` pentru a evita stocarea cache-ului și a reduce dimensiunea imaginii.
Variabilă de mediu : Definește `PYTHONPATH=/app` pentru a permite importarea corectă a modulelor Python din directorul aplicației.
Port de acces : Expune portul `5000` (utilizat de aplicație pentru comunicare).
Punct de intrare : Configurează comanda implicită `python app/filme.py` pentru a porni aplicația la rularea containerului.

## Pornirea aplicației

prin comanda `docker run -p 5000:5000 twilight-app`:

Această abordare asigură o rulare izolată, consistentă și ușor de replicat, indiferent de mediul în care este executată aplicația.


# Pipeline Jenkins




# Pull Request
Am realizat un PR din branch-ul de dezvoltare (`dev_Anghel_Alexandru`) către branch-ul main (`main_Anghel_Alexandru`)
