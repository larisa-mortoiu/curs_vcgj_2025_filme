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
Proiect SCC - Containerizare și CI/CD

Autor: Achitei Mihai-Alexandru

Branch: dev_Achitei_Alexandru

Repo: https://github.com/larisa-mortoiu/curs_vcgj_2025_filme.git

✅ Ce am implementat

	Am dezvoltat o aplicație web în Flask, dedicată gestionării filmelor (proiectul Projet_SCC), care conține:
	* o pagină principală cu titlul serialului și trailer-ul;
	* o pagină cu actorii principali;
	* o pagină cu descrierea serialului;
	* stil personalizat CSS cu temă adaptată și butoane interactive;
	* structură modulară templates/, static/, și filme.py.

	Aplicația a fost containerizată cu Docker și testată automat prin Jenkins.

🔍 Cum am testat

	Am folosit:

	* rulare locală cu python3 filme.py
	* build și rulare în container Docker (docker build, docker run)
	* integrare continuă cu Jenkins (pull din GitHub, build, run)
	* comanda docker ps pentru a verifica starea containerului
	* accesarea aplicației în browser la http://localhost:5000
	
	

	Pytest:
![pytest](https://github.com/user-attachments/assets/fb53242b-b6f2-4d26-b96c-3c3584b29511)

🐳 Cum am rulat în container (Docker)

	Comenzi folosite:

	* docker build -t sonsofanarchy .
	* run -p 5000:5000 sonsofanarchy

	Aplicația devine accesibilă în browser la:
	http://localhost:5000
 
![docker](https://github.com/user-attachments/assets/6d44727f-0f86-4d8b-8061-81db8597cbbf)



🔧 Jenkins: configurare și rulare automată

	Job creat în Jenkins: SonsOfAnarchy-PipeLine

	Configurat ca Pipeline script from SCM

	Repo: https://github.com/larisa-mortoiu/curs_vcgj_2025_filme.git
	Branch: dev_Achitei_Alexandru
	Script path: Jenkinsfile

![Jenkins](https://github.com/user-attachments/assets/861010db-8296-4238-a6b2-413bd96bb096)
--------------------------------------------------------------------
# Al Hajjih Kais

# Proiect SCC – JoJo's Bizarre Adventure

**Autor:** Al-Hajjih Kais (Grupa 442D)

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

Aplicația **JoJo's Bizarre Adventure** este un site informativ despre celebrul serial manga/anime, implementat în Flask (Python) cu HTML/CSS (Jinja2). Oferă:

* **Landing Page:** scurt istoric și descriere generală
* **Trailers:** colecție de clipuri video embed din YouTube
* **Characters:** listă de personaje principale cu poze și denumiri
* **Detalii Personaj:** pagină dedicată fiecărui personaj cu Stand, descriere, voice actor și imagine

Toate paginile sunt construite pe aceeași structură de template-uri și stiluri comune.

---

## Funcționalități & Versiuni

* **v0.1** – structură de bază și landing page static
* **v0.2** – pagini dinamice pentru trailers și characters
* **v0.3** – detalii personaj și link-uri între pagini
* **v1.0** – integrare Docker, testare Pytest și pipeline Jenkins

---

## Tehnologii folosite

* **Python 3.12 & Flask**: server web și rutare dinamică
* **Jinja2**: generare HTML din template-uri
* **CSS & Grid/Flexbox**: layout și responsivitate
* **Docker**: containerizare și portabilitate
* **Pytest**: testare automată unități și endpoint-uri
* **Pylint**: analiză statică a calității codului
* **Jenkins**: orchestrare CI/CD cu pipeline declarativ

---

## Structura proiectului

```text
curs_vcgj_2025_filme/
├── app/
│   ├── lib/            # logica aplicației (data despre personaje)
│   └── tests/          # teste unitare Pytest
├── static/
│   ├── images/         # poze personaje și decor
│   └── styles/         # fișiere CSS comune
├── templates/
│   ├── base.html       # layout de bază
│   ├── home.html       # landing page
│   ├── trailers.html   # pagină trailere
│   ├── cast.html       # listă personaje
│   └── character.html  # detaliu personaj
├── filme.py            # aplicația Flask
├── requirements.txt    # dependențe Python (Flask, pytest)
├── Dockerfile          # definiție imagine Docker
├── dockerstart.sh      # script entrypoint container
├── Jenkinsfile         # pipeline CI/CD
└── README.md           # documentația proiectului
```

---

## Configurare & Instalare

1. **Clone repo & branch**:

   ```bash
   git clone https://github.com/larisa-mortoiu/curs_vcgj_2025_filme.git
   cd curs_vcgj_2025_filme
   git checkout main_Al-Hajjih_Kais
   ```
2. **Rulare directă** (fără venv):

   ```bash
   python3 filme.py
   ```

   Accesează: [http://127.0.0.1:5000](http://127.0.0.1:5000)

> Dacă ai Python instalat global, tot ce trebuie este `python3`.

---

## Prezentare interfață web

1. **Landing Page**

   * Banner și descriere sumară
   * Navigare navbar: Home, Trailers, Characters
  
    ![image](https://github.com/user-attachments/assets/74a2f34b-7b2f-4a9e-a900-c06cdadfb1d8)

2. **Trailers**

   * Grid responsive cu iframe-uri YouTube
  
    ![image](https://github.com/user-attachments/assets/4a502892-f7e7-4387-baa7-49d437da784b)

3. **Characters**

   * Carduri cu imagine, nume și link detalii
   ![image](https://github.com/user-attachments/assets/b1a81241-4560-4a99-94d9-43b8b2928ebb)

4. **Detail Page**

   * Stand power, descriere, voice actor, imagine mare
  
     ![image](https://github.com/user-attachments/assets/46762e9e-3ba5-4749-b955-8dda3465a197)

---

## Testare cu Pytest

Teste unitare incluse în `app/tests/`: verifică:

* Pagina de start `/` răspunde 200
* `/trailers`, `/cast` și `/character/<slug>` răspund 200
* Conținut minim așteptat (nume serie, titlu personaj)

**Rulare**:

```bash
python3 -m pytest app/tests/ -q
```
![image](https://github.com/user-attachments/assets/b8175eeb-b70a-458c-aa53-e6cb30eb69b0)

---

## Containerizare cu Docker

**Build & run local**:

```bash
docker build -t jojo-scc-app .
docker run --rm -p 5000:5000 jojo-scc-app
```

Port 5000 expus, aplicația este gasita la adresa [http://localhost:5000](http://localhost:5000)

---

## Pipeline CI/CD cu Jenkins

Pași declarativi în `Jenkinsfile`:

1. Checkout cod
2. Build Docker Image
3. Unit Tests (in-container cu override ENTRYPOINT)
4. Smoke Test (HTTP check fără port binding)
5. Push to Docker Hub (pe `main`)
   
![image](https://github.com/user-attachments/assets/db7f4abf-6c4d-4a1f-8509-b897fc4ca1ab)

Credențiale: `dockerhub-creds` (ID în Jenkins)


---

## Pull Request & Mentenanță

* Dezvoltarea se face pe branch `dev_Al-Hajjih_Kais`
* Se deschide PR către `main_Al-Hajjih_Kais`
* După review și succes pipeline, se face merge și build automat pe `main`

---

--------------------------------------------------------------------
# Anghel Alexandru Dan
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
# 📦 Proiect: Aplicație web Flask – Lucifer  
**Autor:** Camburu Mihail  
**Branch:** `dev_Camburu_mihail`  
**Repo:** [https://github.com/larisa-mortoiu/curs_vcgj_2025_filme](https://github.com/larisa-mortoiu/curs_vcgj_2025_filme)

---

## ✅ Ce am implementat

Am dezvoltat o aplicație web în Flask, dedicată serialului **Lucifer**, care conține:

- o pagină principală cu titlul serialului și trailerul video;
- o pagină cu actorii principali și fotografiile lor;
- o pagină cu descrierea serialului, stilizată tematic;
- stil personalizat CSS cu temă dark și butoane interactive;
- structură modulară `templates/`, `static/`, `filme.py`.

Aplicația a fost **containerizată cu Docker** și testată automat prin **Jenkins**.

---

## 🔍 Cum am testat

Am folosit:

- rulare locală cu `python3 filme.py`
- build și rulare în container Docker (`docker build`, `docker run`)
- integrare continuă cu Jenkins (pull din GitHub, build, run)
- comanda `docker ps` pentru a verifica starea containerului
- accesarea aplicației în browser la `http://localhost:5000`

---

## 🐳 Cum am rulat în container (Docker)

Comenzi folosite:

```bash
docker build -t lucifer-app .
docker run -d -p 5000:5000 lucifer-app
```

Aplicația devine accesibilă în browser la:
```
http://localhost:5000
```

Verificare container:
```bash
docker ps
```

---

## 🔧 Jenkins: configurare și rulare automată

1. Job creat în Jenkins: `lucifer-pipeline`
2. Configurat ca **Pipeline script from SCM**
   - Repo: `https://github.com/larisa-mortoiu/curs_vcgj_2025_filme.git`
   - Branch: `dev_Camburu_mihail`
   - Script path: `Jenkinsfile`
3. Etape în Jenkinsfile:
   - `Checkout` din GitHub
   - `Docker build`
   - `Docker run`
   - `docker ps`

---

## 📁 Structura proiectului

```
.
├── filme.py
├── Dockerfile
├── Jenkinsfile
├── requirements.txt
├── templates/
│   ├── pagina_principala.html
│   ├── pagina_actori.html
│   └── pagina_descriere_film.html
├── static/
│   ├── style/
│   │   └── fisier_css.css
│   └── images/
└── README_Camburu_Mihail.md
```

---

### 🔚 Proiect realizat cu succes, funcțional atât local cât și în mediu automatizat.

---
--------------------------------------------------------------------
# Constantinescu Adelina Maria

Această aplicație web este o implementare personalizată dedicată filmului _The Curious Case of Benjamin Button_. Proiectul oferă o interfață web modernă prin care utilizatorii pot vizualiza informații despre distribuția filmului și descrierea tematicii, fiind construit cu Python și Flask, cu suport pentru testare automată și analiză statică a codului.

---

## 📑 Cuprins

- [Funcționalități](#funcționalități)
- [Tehnologii utilizate](#tehnologii-utilizate)
- [Structura proiectului](#structura-proiectului)
- [Configurare și rulare](#configurare-și-rulare)
- [Interfață web](#interfață-web)
- [Testare și analiză cod](#testare-și-analiză-cod)
- [Rulare cu Docker](#rulare-cu-docker)
- [Etape pipeline Jenkins](#etape-pipeline-jenkins)
- [Pull Request](#pull-request)



---
## Funcționalități

- Pagina principală de tip homepage cu titlu, imagine și mesaj introductiv
- Afișarea descrierii filmului _The Curious Case of Benjamin Button_ într-o pagină dedicată
- Afișarea distribuției (actori și personaje) cu poze și descrieri individuale
- Navigare ușoară între pagini (linkuri + butoane vizuale)
- Design modern cu CSS personalizat și fonturi Google Fonts

---

## Tehnologii utilizate

- Python 3.10
- Flask (pentru server web)
- HTML5 & CSS3 (interfață)
- Pytest (testare automată)
- Pylint (analiză cod)
- Jenkins (CI/CD pipeline)
- Docker (pentru rulare izolată)


---

## Structura proiectului

```text
CURS_VCGJ_2025_FILME/
├── app/
│   ├── lib/
│   │   ├── curious_case_cast.py
│   │   └── curious_case_description.py
│   └── tests/
│       └── test_filme.py
├── static/
│   ├── images/
│   └── styles/
│       ├── attributes.css
│       ├── curious_case.css
│       └── homepage.css
├── templates/
│   ├── curious_case_cast.html
│   ├── curious_case_description.html
│   ├── curious_case.html
│   └── homepage.html
├── .gitignore
├── activeaza_venv
├── activeaza_venv_Jenkins
├── Dockerfile
├── dockerstart.sh
├── filme.py
├── Jenkinsfile
├── LICENSE
├── pytest.ini
├── README.md
├── requirements.txt
└── start_app.sh
```

---

## Configurare și rulare
### Configurare initiala

1. Clonează proiectul local:

```bash
cd Desktop/proiect/
git clone https://github.com/larisa-mortoiu/curs_vcgj_2025_filme.git
```

2. Instalare pachete de baza
```bash
sudo apt update && sudo apt upgrade
sudo apt install git
sudo apt install python3
sudo apt install python3-pip
sudo apt install python3.10-venv  # sau python3.12-venv, în funcție de versiune
sudo apt install net-tools
```
3. Trecere in folderul cu proiectul
```bash
 cd curs_vcgj_2025_filme
 ```
4. Comuta pe branch-ul personal
```bash
git checkout dev_Constantinescu_Adelina
```
### Configurare .venv
Proiectul include două scripturi bash utile pentru rulare rapidă și automată în orice mediu:



#### 🔹 `activeaza_venv`

Acest script verifică dacă există un mediu virtual activabil în directorul `.venv`.

- Dacă mediul virtual există și poate fi activat → îl pornește imediat
- Dacă nu există sau activarea eșuează → scriptul rulează automat `activeaza_venv_Jenkins`, care:
  - Creează un nou mediu virtual
  - Instalează automat toate pachetele necesare din `requirements.txt`

Această abordare ajută la rularea proiectului atât în medii locale, cât și în Jenkins.



#### 🔹 `start_app.sh`

După activarea mediului virtual, rulează acest script pentru a porni aplicația Flask.

- Serverul pornește pe adresa `127.0.0.1`, portul `5011`
- Aplicația poate fi accesată din browser la:
  - [http://127.0.0.1:5011](http://127.0.0.1:5011)
  - sau
  - [http://localhost:5011](http://localhost:5011)

---
## Interfață web

###  Pagini disponibile

- **Homepage** (`/`)
  - Pagina principală cu titlul proiectului, un mesaj de întâmpinare și posterul filmului
  - Buton de acces către pagina dedicată filmului
  - ![Homepage](https://github.com/larisa-mortoiu/curs_vcgj_2025_filme/blob/main_Constantinescu_Adelina/static/images/homepage.png)
- **Pagina filmului** (`/curious_case`)
  - Oferă două butoane pentru navigare:
    - 🔸 **Descriere** (`/curious_case/description`)
    - 🔸 **Distribuție** (`/curious_case/cast`)
    - ![Main Page](https://github.com/larisa-mortoiu/curs_vcgj_2025_filme/blob/main_Constantinescu_Adelina/static/images/main_page.png)
- **Descriere** (`/curious_case/description`)
  - Afișează un text narativ formatat despre film, regizor, tematică și mesajul său
  - ![Descriere](https://github.com/larisa-mortoiu/curs_vcgj_2025_filme/blob/main_Constantinescu_Adelina/static/images/description_page.png)
- **Distribuție** (`/curious_case/cast`)
  - Listează actorii principali, numele personajelor și o scurtă descriere
  - Include imagini reprezentative pentru fiecare actor
  - ![Cast](https://github.com/larisa-mortoiu/curs_vcgj_2025_filme/blob/main_Constantinescu_Adelina/static/images/cast_page.png)

---

## Testare și analiză cod

Testarea aplicației se realizează folosind **Pytest**, prin teste unitare definite în fișierul `test_filme.py`, localizat în directorul `app/tests/`.


### Ce validează testele

Testele acoperă funcționalitatea principală a aplicației Flask:

- **Testarea descrierii filmului**  
  Se testează funcția `get_description()` din modulul `curious_case_description`.  
  Verificările includ:
  - Răspunsul HTTP al rutei `/curious_case/description` este 200 (OK)
  - Textul HTML generat conține cuvinte-cheie esențiale precum `Brad Pitt`, `Cate Blanchett`, `David Fincher`
  - Descrierea returnată de funcție este identică cu cea afișată în pagină

- **Testarea distribuției**  
  Se evaluează funcția `get_cast()` din `curious_case_cast`, accesată prin ruta `/curious_case/cast`.  
  Verificările includ:
  - Statusul răspunsului este valid
  - Fiecare actor și numele personajului sunt afișate corect în HTML
  - Se validează existența câmpurilor `name` și `character` pentru fiecare membru din distribuție



### Obiectivul testelor

Scopul testelor este să confirme:
- că datele generate de backend sunt afișate corect în interfața HTML
- că toate elementele esențiale ale aplicației apar în pagini
- că modificările în cod nu afectează funcționalitatea de bază



### Rulare locală

Testele pot fi rulate local folosind comanda:

```bash
pytest app/tests/
```
 - ![Teste](https://github.com/larisa-mortoiu/curs_vcgj_2025_filme/blob/main_Constantinescu_Adelina/static/images/test.png)

 ### Analiză statică a codului

Pentru asigurarea unui cod curat și ușor de întreținut, aplicația utilizează **Pylint**, un instrument de analiză statică Python.

Verificările acoperă:
- Respectarea convențiilor de stil (naming, indentare, lungime linii)
- Utilizarea corectă a variabilelor (nefolosite, redefinite)
- Organizarea logică a modulelor

Analiza este aplicată pe:
- modulele din `app/lib/`
- fișierul principal `filme.py`
- fișierele de test

---

### Integrare în Jenkins

Analiza Pylint este integrată într-o etapă dedicată a pipeline-ului Jenkins. Comenzile utilizate:

```bash
pylint --exit-zero app/lib/*.py
pylint --exit-zero app/tests/*.py
pylint --exit-zero filme.py
```
---

## Rulare cu Docker

Aplicația poate fi rulată rapid și izolat folosind Docker. Acest lucru este util pentru testare, livrare sau rulare pe orice sistem fără a instala dependințele manual.


Asigură-te că te afli în directorul proiectului unde se află `Dockerfile`, apoi rulează:

```bash
docker build -t adelina_docker:latest .
sudo docker run --name adelina_docker -p 8020:5011 adelina_docker:latest
```

Pentru a rula aplicatia prin container vom folosi urmatoarea comanda:

    sudo docker start adelina_docker
Pentru a opri rularea aplicatiei:

    sudo docker stop adelina_docker

---

## Etape pipeline Jenkins

Pentru integrarea continuă, aplicația utilizează **Jenkins**, care rulează automat o serie de pași la fiecare actualizare a codului.

Etapele definite în `Jenkinsfile` sunt:

- **Clone repo**: preia automat codul din branch-ul `main_Constantinescu_Adelina`
- **Build**: creează și activează un mediu virtual Python, instalează dependințele
- **Code quality**: rulează `pylint` cu `--exit-zero` pentru a verifica stilul fără a bloca execuția
- **Run Tests**: rulează testele unitare definite cu `pytest`
- **Containerizare Docker**: creează și rulează o imagine Docker a aplicației pe portul `8020`


```bash
    systemctl start jenkins
```
![Jenkins](https://github.com/larisa-mortoiu/curs_vcgj_2025_filme/blob/main_Constantinescu_Adelina/static/images/jenkins.png)

---

## Pull Request
Dupa finalizarea cerintelor, am realizat un pull request de pe `dev_Constantinescu_Adelina` catre `main_Constantinescu_Adelina`.
![Readme](https://github.com/larisa-mortoiu/curs_vcgj_2025_filme/blob/main_Constantinescu_Adelina/static/images/readme.png)

--------------------------------------------------------------------
# Corlan Victor Alexandru

-------------------------

## Cuprins
1.  [Prezentare Generală](#prezentare-generală)
2.  [Tehnologii Utilizate](#tehnologii-utilizate)
3.  [Structura Proiectului](#structura-proiectului)
4.  [Configurare Inițială a Sistemului](#configurare-inițială-a-sistemului)
    * [Instalarea Programelor Necesare](#instalarea-programelor-necesare)
    * [Rularea Aplicației Python](#rularea-aplicației-python)
5.  [Prezentarea Paginilor Web](#prezentarea-paginilor-web)
6.  [Procesul de Testare cu Pytest](#procesul-de-testare-cu-pytest)
7.  [Analiza Codului cu Pylint](#analiza-codului-cu-pylint)
8.  [Containizare cu Docker](#containizare-cu-docker)
9.  [Pipeline-ul Jenkins](#pipeline-ul-jenkins)
10. [Cum se face un Pull Request pe GitHub](#cum-se-face-un-pull-request-pe-github)

## Prezentare Generală
Acest proiect implementează o aplicație web simplă, bazată pe framework-ul Flask, pentru a afișa informații despre filme specifice, incluzând o pagină principală pentru selectarea filmului, o pagină de detalii scurte cu poster, o pagină cu descrierea completă și o pagină cu lista actorilor și detaliile personajelor. Proiectul include, de asemenea, instrumente pentru testare (Pytest), analiză statică a codului (Pylint), containizare (Docker) și automatizare a proceselor CI/CD (Jenkins Pipeline).

## Tehnologii Utilizate
* **Flask:** Framework web minimalist pentru Python.
* **HTML5 & CSS3:** Pentru structura și stilizarea paginilor web.
* **Python:** Limbajul de programare principal.
* **Pytest:** Framework pentru scrierea și rularea testelor unitare și de integrare.
* **Pylint:** Unealtă pentru analiză statică a codului Python, ajutând la identificarea erorilor și a problemelor de stil.
* **Docker:** Platformă pentru dezvoltarea, livrarea și rularea aplicațiilor în containere.
* **Jenkins:** Server de automatizare open-source, utilizat aici pentru a construi un pipeline CI/CD.

## Structura Proiectului
Proiectul este organizat în următoarele directoare și fișiere principale:

- `app/` –  Directorul principal al aplicației:

  - `lib/` – Director pentru bibliteca de afișare a descierii și distribuției filmelor;

  - `test/` –  Teste unitare și de integrare cu Pytest;

- `static/` – Director pentru fișiere statice (CSS, imagini);

  - `photos/` – Imagini utilizate în aplicație (postere, fotografii actori);

  - `styles/` – Fișiere CSS pentru stilizare;

- `templates/` – Director pentru șabloanele HTMLș

- Fișiere de configurare si rulare:

  - `filme.py` – fișierul principal pentru aplicația Flask;

  - `Dockerfile` – Instrucțiuni pentru construirea imaginii Docker;
  
  - `dockerstart` – Script executat la pornirea containerului Docker;

  - `Jenkinsfile` – Definiția pipeline-ului Jenkins;

  - `pytest.ini` – Fișier de configurare pentru Pytest;

  - `requirements` – Lista dependențelor Python (pentru pip);

  - `activeaza_venv`, `activeaza_venv_jenkins` - Script pentru activarea mediului virtual local
  
  - `ruleaza_aplicatia` – Script pentru rularea locală a aplicației Flask;

## Configurare Inițială a Sistemului

### Instalarea Programelor Necesare
Pentru a rula și dezvolta proiectul, este necesară instalarea următoarelor programe pe sistemul de operare:
* **Python 3.6+:**
*     sudo apt install python3
* **pip:**
*     sudo apt install python3-pip
* **Git:**
*     sudo apt install git
* **Docker:**
*     curl -fsSL https://get.docker.com -o get-docker.sh
      sh get-docker.sh
* **Jenkins:**
     ```bash
    sudo apt install fontconfig openjdk-21-jre
    sudo wget -O /etc/apt/keyrings/jenkins-keyring.asc \
    https://pkg.jenkins.io/debian-stable/jenkins.io-2023.key
    echo "deb [signed-by=/etc/apt/keyrings/jenkins-keyring.asc]" \
    https://pkg.jenkins.io/debian-stable binary/ | sudo tee \
    /etc/apt/sources.list.d/jenkins.list > /dev/null
    sudo apt-get update
    sudo apt-get install jenkins
    ```
### Rularea Aplicației Python
Utilizarea unui mediu virtual este o practică recomandată pentru a izola dependențele proiectului de cele ale sistemului.

1.  Depozitul de cod este de obicei obținut prin clonare și apoi se navighează în directorul proiectului:
    ```bash
    cd proiect_scc
    git clone https://github.com/larisa-mortoiu/curs_vcgj_2025_filme.git
    git checkout dev_Corlan_Victor
    ```
2.  Activarea mediului virtual este necesară pentru a folosi pachetele instalate în el. Acest lucru se realizează prin executarea scriptului de activare:
        ```bash
        source activeaza_venv
        ```
3. Rularea aplicației prin scriptul corespunzător:
       ```bash
        source ruleaza_aplicatia
        ```

![ruleaza_aplicatia](https://github.com/larisa-mortoiu/curs_vcgj_2025_filme/blob/main_Corlan_Victor/static/photos/rulare_aplicatie.png)

## Prezentarea Paginilor Web
Aplicația web oferă o navigare simplă printre filme:

* **Pagina Principală** Afișează o listă de filme disponibile. Fiecare element din listă este un link către pagina de detalii a filmului respectiv.

![pagina_principala](https://github.com/larisa-mortoiu/curs_vcgj_2025_filme/blob/main_Corlan_Victor/static/photos/pagina_principala.png)
  
* **Pagina Detaliilor Filmului** Prezintă informații scurte despre film (regie, genuri, durată, an lansare) și afișează posterul filmului. Conține butoane pentru a naviga către pagina de descriere completă, pagina de distribuție și înapoi la lista principală.

![pagina_film](https://github.com/larisa-mortoiu/curs_vcgj_2025_filme/blob/main_Corlan_Victor/static/photos/pagina_film.png)
  
* **Pagina Descrierii Filmului** Afișează descrierea detaliată a filmului, preluată din modulul `biblioteca_filme.py`.

![pagina_descriere](https://github.com/larisa-mortoiu/curs_vcgj_2025_filme/blob/main_Corlan_Victor/static/photos/pagina_descriere.png)
  
* **Pagina Distribuției Filmului** Listează actorii principali, personajele interpretate și o scurtă descriere a personajului, însoțită de o fotografie a actorului/personajului. Datele sunt preluată din modulul `biblioteca_filme.py`.

![pagina_distributie](https://github.com/larisa-mortoiu/curs_vcgj_2025_filme/blob/main_Corlan_Victor/static/photos/pagina_distributie.png)

## Procesul de Testare cu Pytest
Proiectul utilizează `pytest` pentru a rula teste automate. Testele sunt localizate în directorul `app/tests/` și verifică funcționalitatea aplicației Flask și a modulelor interne.

* Fișierul `app/tests/test_filme.py` conține cazurile de testare:
- Verifică formatul răspunsului funcțiilor găsite în biblioteci
- Verifică începutul descrierii, că este conform celei dorite
- Verifică existența câmpului "actor" la distribuție
- Verifică faptul că serverul de Flask răspunde corect la cererile de GET
  
* Fișierul `pytest.ini` conține setări de configurare pentru `pytest`.

Pentru a rula testele:
1.  Mediul virtual este activat (dacă nu este deja activat).
2.  Se navighează la directorul rădăcină al proiectului.
3.  Comanda `pytest app/tests/` este utilizată pentru a descoperi și executa testele din directorul specificat.

![testare_pytest](https://github.com/larisa-mortoiu/curs_vcgj_2025_filme/blob/main_Corlan_Victor/static/photos/testare_pytest.png)

## Analiza Codului cu Pylint
`Pylint` este folosit pentru a analiza static codul Python, ajutând la menținerea unui stil de cod consistent și la identificarea potențialelor erori.

* Rularea manuală a Pylint se poate face pe fișierele sau directoarele Python:
   ```bash
    pylint --exit-zero app/lib/*.py
    pylint --exit-zero app/tests/*.py
    pylint --exit-zero filme.py
    ```
* Analiza Pylint este, de asemenea, integrată în pipeline-ul Jenkins pentru a asigura că modificările respectă standardele de cod înainte de a fi integrate.

## Containizare cu Docker
Aplicația poate fi containizată folosind Docker, asigurând un mediu de rulare consistent.

* `Dockerfile` conține instrucțiunile pentru a construi imaginea Docker a aplicației. Acesta definește mediul de bază, copiază fișierele proiectului, instalează dependențele și configurează cum rulează aplicația.
* `dockerstart.sh` este un script simplu executat la pornirea containerului, folosit pentru a activa mediul virtual în container (dacă este necesar) și a lansa aplicația Flask.

Pentru a construi imaginea Docker:
1.  Se navighează la directorul rădăcină al proiectului (unde se află `Dockerfile`).
2.  Comanda `docker build -t scc:latest .` este utilizată pentru a construi imaginea. Numele și tag-ul imaginii pot fi specificate după `-t`.
3. Se rulează un container din imaginea construită:
    ```bash
    docker run --name scc -p 25568:25568 scc:latest
    ```

## Pipeline-ul Jenkins

`Jenkinsfile` definește un pipeline de Integrare Continuă (CI). Acesta automatizează pașii de construire, testare și analiză a codului de fiecare dată când sunt făcute modificări în depozitul Git.

Pipeline-ul este structurat în următoarele etape:
1.  **Clone repo:** Preluarea codului sursă dintr-un depozit Git specificat.
2.  **Build:** Crearea unui mediu virtual Python și instalarea dependențelor proiectului.
3.  **pylint - calitate cod:** Rularea uneltei Pylint pentru a verifica calitatea și stilul codului Python din diferite părți ale proiectului.
4.  **Unit Testing cu pytest:** Executarea testelor automate definite în directorul `app/tests/` utilizând framework-ul Pytest.
5.  **Deploy:** Construirea imaginii Docker a aplicației și crearea unui container Docker din această imagine.

Pentru a rula acest pipeline, o instanță Jenkins trebuie să fie configurată și conectată la depozitul GitHub.

![rulare_jenkins](https://github.com/larisa-mortoiu/curs_vcgj_2025_filme/blob/main_Corlan_Victor/static/photos/rulare_jenkins.png)

## Cum se face un Pull Request pe GitHub

1.  Modificările sunt adăugate și comise:
    ```bash
    git add .
    git commit -m "Modificări"
    ```
2.  Ramura locală este împinsă pe GitHub:
    ```bash
    git push
    ```
3.  Pe pagina depozitului de pe GitHub, o notificare sugerează crearea unui Pull Request din ramura nou împinsă.
4.  Se selectează opțiunea "Compare & pull request".
5.  Detaliile PR-ului sunt completate, incluzând un titlu descriptiv și o explicație a modificărilor.
6.  Pull Request-ul este trimis.
7.  Se așteaptă revizuirea codului de către alți colaboratori
8. După aprobare și trecerea verificărilor automate, modificările sunt integrate (merge PR-ul) în ramura principală.
![pull_request](https://github.com/larisa-mortoiu/curs_vcgj_2025_filme/blob/main_Corlan_Victor/static/photos/pull_request.png)
![pull_request_2](https://github.com/larisa-mortoiu/curs_vcgj_2025_filme/blob/main_Corlan_Victor/static/photos/pull_request_2.png)

# Dina Nitoi Maria Alexandra

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

# Prezentarea generala a aplicatiei

Acest proiect web, intitulat **Filme**, are ca scop prezentarea detaliată a unui film ales – The Prestige.
Aplicația le oferă utilizatorilor acces rapid la informații esențiale despre film, precum descrierea tematică și distribuția principală, printr-o interfață intuitivă și responsivă. Din punct de vedere tehnic, aplicația este dezvoltată cu **Flask** și este rulată într-un mediu izolat folosind **Docker**, ceea ce asigură portabilitate și consistență între medii. Testele unitare sunt automatizate cu **Pytest**, iar verificarea calității codului este realizată prin **Pylint**. Întregul flux de dezvoltare – de la instalarea dependințelor, până la rularea testelor și containerizarea aplicației – este gestionat automat printr-un pipeline de integrare continuă configurat în **Jenkins**.


# Versiuni si functionalitati disponibile

v1.0 – Versiunea actuală

Afișarea informațiilor despre filmul The Prestige, selectat manual ca subiect principal al aplicației.

Pagini dedicate pentru:

 - Descrierea filmului – un rezumat detaliat care evidențiază tematica și atmosfera poveștii.

 - Distribuție – listă cu actorii principali, ilustrată vizual cu imagini și nume.

Navigare intuitivă între homepage și paginile detaliate, cu opțiuni de întoarcere.

Testare automată a funcționalităților prin Pytest.

Verificare statică a calității codului folosind Pylint.

Containerizare completă cu Docker, pentru rulare uniformă în medii diferite.

Integrare continuă cu Jenkins, care rulează automat:

- instalarea dependențelor

- testele unitare

- analiza codului

- build-ul imaginii Docker

# Tehnologii utilizate

- Python 3.11 – limbajul de programare utilizat pentru dezvoltarea aplicației.

- Flask – framework web ușor și flexibil, folosit pentru gestionarea rutelor și a logicii aplicației.

- HTML & CSS – pentru structura și stilizarea interfeței web.

- Pytest – pentru scrierea și rularea testelor unitare.

- Pylint – pentru analiza statică a codului și menținerea unui stil coerent.

- Docker – pentru containerizarea aplicației, oferind un mediu izolat și portabil.

- Jenkins – pentru integrare continuă: automatizează pașii de build, testare și analiză a codului.

# Structura proiectului

![Structura](https://github.com/larisa-mortoiu/curs_vcgj_2025_filme/blob/dev_Dina_Alexandra/static/images/screenshots/structure_of_project.jpg)
  
  Conține logica principală a aplicației.
   - lib/ – module Python care oferă datele pentru descriere și distribuție:
   the_prestige_cast.py – returnează lista actorilor.
   the_prestige_description.py – returnează descrierea filmului.
   
   - tests/ – teste unitare scrise cu Pytest:
   test_filme.py – verifică funcțiile din lib/.

- static/  
  
  Conține resurse statice accesate de aplicație.
  - images/ – imaginile folosite pentru actori și background.
  - styles/ – fișiere CSS pentru stilizarea paginilor HTML.


- templates/
  
   Fișiere HTML care definesc structura vizuală a paginilor web.
  - homepage.html – pagina de pornire.
  - the_prestige_cast.html – pagină cu distribuția.
  - the_prestige_description.html – pagină cu descrierea filmului.
  - the_prestige.html – pagină principală pentru film.

- Aplicația Flask principală
  - filme.py – aplicația Flask principală, definește rutele.  


- Fișiere de configurare și automatizare
  - Jenkinsfile – definește pașii de build/test/deploy în Jenkins.  
  - Dockerfile – folosit pentru a construi imaginea Docker.
  
- Scripturi de rulare și mediu
  - pytest.ini – configurare pentru rularea testelor.  
  - requirements.txt – lista librăriilor necesare.  
  - dockerstart.sh – script de pornire în container.  
  - run_app.sh – script de rulare locală.  
  - activate_venv.sh / activate_venv_jenkins – scripturi pentru activarea mediului virtual.  

  # Instructiuni de instalare si configurare

  ## Configurație inițială
 Navighează în directorul Desktop al utilizatorului curent, locul unde va fi clonat proiectul.
```
cd ~/Desktop/            
```

Clonează repository-ul GitHub local
```
git clone https://github.com/larisa-mortoiu/curs_vcgj_2025_filme.git
```

Intră în directorul nou creat care conține fișierele proiectului clonat.
```
cd curs_vcgj_2025_filme
```

Aceasta afișează toate branch-urile remote disponibile în repository-ul GitHub.
```
git branches -r     
```

Creează local un branch nou denumit dev_Dina_Alexandra pe baza branch-ului cu același nume de pe remote și comută pe el.
```
git checkout -b dev_Dina_Alexandra origin/dev_Dina_Alexandra
```
Rulează scriptul de activare a mediului virtual, sau îl creează dacă nu există.
```
. ./activeaza_venv.sh     
```
Pornește aplicația Flask, setând IP-ul și portul pentru accesarea în browser.
```
. ./ruleaza_app.sh    
```
 ## Configurare .venv și instalare pachete
 Pentru a rula aplicația local, este necesară activarea unui mediu virtual Python. Acest proces este automatizat prin scripturi bash aflate în rădăcina proiectului:

- activeaza_venv.sh
 Acest script încearcă să activeze un mediu virtual existent în directorul .venv.
 Dacă .venv nu există sau activarea eșuează, scriptul creează automat un nou mediu virtual și instalează toate pachetele din requirements.txt.

-start_app.sh
 Se folosește doar după activarea mediului virtual. Scriptul lansează aplicația Flask pe IP-ul 127.0.0.1, portul 5011. Poți accesa aplicația din browser la:
 http://127.0.0.1:5011 sau http://localhost:5011

 ![Running_App](https://github.com/larisa-mortoiu/curs_vcgj_2025_filme/blob/dev_Dina_Alexandra/static/images/screenshots/Running_app.png)

 # Interfata web prezentare

 ## Pagina principală (Homepage)
  Este punctul de start al aplicației, oferind utilizatorului o primă interacțiune și acces rapid către detalii despre filmul selectat.
  
  ![Home_page](https://github.com/larisa-mortoiu/curs_vcgj_2025_filme/blob/dev_Dina_Alexandra/static/images/screenshots/homepage_image.png)

 ## Pagina film
 
 Oferă o prezentare sumară a filmului, cu opțiuni de navigare către pagina de descriere detaliată sau distribuție, permițând utilizatorului să aleagă ce informație dorește să exploreze mai departe.

  ![Movie](https://github.com/larisa-mortoiu/curs_vcgj_2025_filme/blob/dev_Dina_Alexandra/static/images/screenshots/the_prestige_movie.png)

  ## Secțiunea de descriere 
  Oferă o prezentare amplă a subiectului filmului, evidențiind temele și atmosfera acestuia.
  
  ![Description](https://github.com/larisa-mortoiu/curs_vcgj_2025_filme/blob/dev_Dina_Alexandra/static/images/screenshots/description1.png)
  ![Description](https://github.com/larisa-mortoiu/curs_vcgj_2025_filme/blob/dev_Dina_Alexandra/static/images/screenshots/description2.png)
  
  ## Secțiunea de distribuție
  Afișează actorii principali împreună cu personajele pe care le interpretează.
   ![Cast](https://github.com/larisa-mortoiu/curs_vcgj_2025_filme/blob/dev_Dina_Alexandra/static/images/screenshots/cast.jpg)
   
  # Testare Pytest

Pentru a valida funcționalitatea corectă a aplicației, au fost implementate teste unitare cu ajutorul framework-ului Pytest. Acestea sunt definite în fișierul test_filme.py, aflat în directorul app/tests/.

Testele vizează componentele esențiale ale aplicației:

Testarea descrierii filmului 
 - Verifică dacă descrierea filmului returnată de get_descriere()
 - Caută în textul descrierii anumite cuvinte-cheie relevante pentru tematica filmului The Prestige

Testarea distribuției
 - Evaluează formatul general al listei de actori returnată de get_actori()
 - Confirmă prezența actorilor principali în listă
   
Pentru fiecare test:

Se apelează funcțiile din the_prestige_description.py și the_prestige_cast.py.

Se verifică tipul valorii returnate.

Se confirmă prezența anumitor elemente esențiale în conținutul returnat (ex: lungimea textului descriptiv, existența unor actori cunoscuți).

Testele rulează atât local (manual, cu comanda pytest), cât și automat, prin intermediul pipeline-ului Jenkins configurat în proiect. Acest lucru contribuie la menținerea unei funcționări stabile și verificabile a aplicației la fiecare modificare.

## Testare locală

  ![Test](https://github.com/larisa-mortoiu/curs_vcgj_2025_filme/blob/dev_Dina_Alexandra/static/images/screenshots/tests.png)

## Testare automată

Prin intermediul Jenkinsfile
```
stage('Run Tests - pytest') {
          steps {
              sh '''
                  . ${VENV_DIR}/bin/activate
                  pytest app/tests
              '''
   }
 }
 ```
# Analiza statica a codului cu Pylint
Pentru verificarea calității codului sursă, proiectul utilizează Pylint – un instrument de analiză statică ce ajută la menținerea unui stil de cod curat și coerent. Analiza este aplicată asupra fișierelor esențiale ale aplicației, precum modulele din app/lib/, fișierul principal filme.py și testele din app/tests/.

Această etapă detectează automat aspecte precum:

- probleme de formatare ;

- denumiri improprii pentru variabile sau funcții;

- cod inutil sau variabile nefolosite;

- abateri de la bunele practici Python.

Verificarea Pylint este integrată în procesul de integrare continuă (CI) printr-un stage dedicat în Jenkins, care rulează automat comenzile:

```
pylint --exit-zero app/lib/*.py
pylint --exit-zero app/tests/*.py
pylint --exit-zero filme.py
```

# Containerizare cu Docker

Containerizarea este o tehnică prin care aplicația și toate dependențele ei sunt împachetate într-un mediu izolat, numit container. Acesta rulează la fel indiferent de sistemul de operare sau configurația locală, ceea ce elimină problemele de compatibilitate („merge la mine, dar nu la tine”).

În acest proiect, containerizarea este realizată cu Docker și ne ajută să rulăm aplicația într-un mod predictibil, portabil și ușor de distribuit, fie local, fie într-un mediu de producție sau testare.

# Configurație. Dockerfile

Fișierul Dockerfile definește pașii pentru construirea imaginii:

- Pornește de la o imagine `python:3.11-alpine`.
- Creează un utilizator non-root `dina_docker`.
- Setează directorul de lucru și copiază codul aplicației.
- Oferă permisiuni de execuție scriptului `dockerstart.sh`.
- Creează un mediu virtual și instalează dependențele.
- Rulează aplicația Flask ca utilizator non-root pe portul 5011.

# Containter și imagine Docker

Creare imagine: 

``` docker build -t movieimage:v1 .```

 ![Docker](https://github.com/larisa-mortoiu/curs_vcgj_2025_filme/blob/dev_Dina_Alexandra/static/images/screenshots/docker-images.jpeg)

Creare container:  

 ```docker create --name moviecontainer -p 8020:5011 movieimage:v1```

 ![Docker](https://github.com/larisa-mortoiu/curs_vcgj_2025_filme/blob/dev_Dina_Alexandra/static/images/screenshots/doker_commands.jpeg)
 
 Pornire container:
 
 ```docker start moviecontainer```
 
 ![Docker](https://github.com/larisa-mortoiu/curs_vcgj_2025_filme/blob/dev_Dina_Alexandra/static/images/screenshots/docker_homepage.png)

După pornirea aplicației cu `./dockerstart.sh`, aceasta va fi accesibilă în browser la adresa locală: **http://127.0.0.1:8020**.

# Pipeline CI/CD cu Jenkins

Jenkins este un instrument de automatizare folosit în acest proiect pentru a gestiona procesul de integrare continuă. El a fost configurat astfel încât să detecteze automat modificările din repository-ul GitHub și să execute un set de pași definiți în fișierul Jenkinsfile. Acești pași includ activarea mediului virtual, instalarea dependințelor, rularea testelor și verificarea calității codului. Prin această automatizare, Jenkins asigură că fiecare actualizare a aplicației este verificată și validată într-un mod consistent, fără intervenție manuală.

#Jenkinsfile
Fișierul Jenkinsfile definește pașii automatizați pe care Jenkins îi urmează. Acest pipeline asigură integrarea continuă, permițând dezvoltatorului să verifice rapid dacă aplicația funcționează corect după fiecare modificare. Pipeline-ul conține următoarele stagii:

- Clone repo
 Clonarea codului sursă din ramura dev_Dina_Alexandra a repository-ului GitHub pentru a pregăti aplicația pentru build.

- Set up virtual environment
 Creează un mediu virtual Python (.venv), îl activează și instalează toate pachetele necesare specificate în requirements.txt.

- Code Quality - pylint
 Verifică stilul și calitatea codului folosind pylint pe modulele aplicației (app/lib, app/tests, filme.py) fără a opri execuția dacă sunt avertismente.

- Run Tests - pytest
 Rulează testele unitare definite în app/tests folosind pytest pentru a valida funcționalitatea aplicației.

- Deploy
 Construiește o imagine Docker din aplicație și creează un container cu un port expus, pentru a putea fi rulată ulterior în izolare.

Pentru a porni serverul Jenkins local, este suficient să rulezi comanda:

```jenkins```

Aceasta va inițializa serverul pe portul implicit (de obicei 8080), permițând accesul la interfața web Jenkins prin adresa:
http://localhost:8080 sau http://127.0.0.1:8080


Pipeline-ul este configurat astfel încât, la fiecare push în repository-ul GitHub, să se declanșeze automat o execuție a pipeline-ului prin intermediul agentului Jenkins. Acest comportament este asigurat prin bifarea opțiunii **GitHub hook trigger for GITScm polling**, precum și prin activarea opțiunii **Poll SCM**, care determină verificarea modificărilor în repository la fiecare 2 minute. Astfel, proiectul se actualizează constant în funcție de modificările aduse codului sursă.

# Procedura Pull Request
Modificările aduse în branch-ul de dezvoltare dev_Dina_Alexandra au fost propuse pentru a fi integrate în ramura principală main_Dina_Alexandra prin crearea unui Pull Request.

 ![PR](https://github.com/larisa-mortoiu/curs_vcgj_2025_filme/blob/dev_Dina_Alexandra/static/images/screenshots/PR.jpeg)


# Bibliografie
- [Docker Documentation](https://docs.docker.com/)
- [Git Documentation](https://git-scm.com/doc)
- [Jenkins Documentation](https://www.jenkins.io/doc/)
- [Repo crchende/sysinfo  ](https://github.com/crchende/sysinfo)

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

# Procedura Pull Request
Modificările realizate în branch-ul de dezvoltare (dev_Dumitrache_Denisa) au fost propuse pentru integrare în ramura principală (main_Dumitrache_Denisa) printr-un Pull Request (PR):
![pull-request](https://github.com/larisa-mortoiu/curs_vcgj_2025_filme/blob/dev_Dumitrache_Denisa/static/capturi/pull-request.png)

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

## Cuprins

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

![venv](https://github.com/larisa-mortoiu/curs_vcgj_2025_filme/blob/b7a37ef1d518c0db1a3444fa2d5008cb6d79f122/static/screenshots_README/venv.png)

# Prezentarea interfetei web

## Pagină principală (Homepage)

Afișează lista cu filmele disponibile, cu acces rapid prin link-uri către pagina cu detalii a fiecărui film/serial.
![stranger-things-homepage](https://github.com/larisa-mortoiu/curs_vcgj_2025_filme/blob/b7a37ef1d518c0db1a3444fa2d5008cb6d79f122/static/screenshots_README/home%20page.png)

## Pagină film

Include o scurtă prezentarea despre film/serial și două butoane către paginile de descriere și distribuție.
![stranger-things_serial_home](https://github.com/larisa-mortoiu/curs_vcgj_2025_filme/blob/b7a37ef1d518c0db1a3444fa2d5008cb6d79f122/static/screenshots_README/serial_home.png)

## Pagină descriere film

Oferă detalii extinse despre filmul/serialul ales.
![stranger-things-descriere](https://github.com/larisa-mortoiu/curs_vcgj_2025_filme/blob/b7a37ef1d518c0db1a3444fa2d5008cb6d79f122/static/screenshots_README/descriere.png)

## Pagină distribuție film

Prezintă actorii principali și personajele interpretate.
![stranger-things-distributie](https://github.com/larisa-mortoiu/curs_vcgj_2025_filme/blob/b7a37ef1d518c0db1a3444fa2d5008cb6d79f122/static/screenshots_README/distributie.png)

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

![pytest](https://github.com/larisa-mortoiu/curs_vcgj_2025_filme/blob/b7a37ef1d518c0db1a3444fa2d5008cb6d79f122/static/screenshots_README/pytest.png)

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

![docker](https://github.com/larisa-mortoiu/curs_vcgj_2025_filme/blob/b7a37ef1d518c0db1a3444fa2d5008cb6d79f122/static/screenshots_README/docker_images.png)

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

![docker-container](https://github.com/larisa-mortoiu/curs_vcgj_2025_filme/blob/b7a37ef1d518c0db1a3444fa2d5008cb6d79f122/static/screenshots_README/container.png)

## Rularea aplicației din container

![rulare-din-container](https://github.com/larisa-mortoiu/curs_vcgj_2025_filme/blob/b7a37ef1d518c0db1a3444fa2d5008cb6d79f122/static/screenshots_README/home%20page.png)

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

![jenkins-blueocean](https://github.com/larisa-mortoiu/curs_vcgj_2025_filme/blob/b7a37ef1d518c0db1a3444fa2d5008cb6d79f122/static/screenshots_README/blue-ocean.png)

# Flux de lucru colaborativ - Pull Request

Am creat un PR(Pull Request) din branch-ul de dezvoltare (`dev_Gorcea_Cristina`) către branch-ul main (`main_Gorcea_Cristina`)
![PR](https://github.com/larisa-mortoiu/curs_vcgj_2025_filme/blob/b7a37ef1d518c0db1a3444fa2d5008cb6d79f122/static/screenshots_README/Pull%20Request.png)

# Bibliografie

- [HTML Documentation ](https://www.w3schools.com/html/html_intro.asp)
- [CSS Documentation ](https://www.w3schools.com/CSSref/index.php)
- [Flask Documentation](https://flask.palletsprojects.com/en/stable/)
- [Pytest Documentation](https://docs.pytest.org/en/stable/contents.html)
- [Docker Documentation](https://docs.docker.com/)
- [Jenkins Documentation](https://www.jenkins.io/doc/)
--------------------------------------------------------------------
# Ichim Alexandru Ionut
# Proiect SCC – The Blacklist Web App

**Autor:** Ichim Alexandru-Ionut (Grupa 442D)

---

## Cuprins

1. [Descriere aplicație](#descriere-aplicație)
2. [Funcționalități & Versiuni](#funcționalități--versiuni)
3. [Tehnologii folosite](#tehnologii-folosite)
4. [Configurare & Instalare](#configurare--instalare)
5. [Prezentare interfață web](#prezentare-interfață-web)
6. [Testare cu Pytest](#testare-cu-pytest)
7. [Analiză statică cu Pylint](#analiză-statică-cu-pylint)
8. [Containerizare cu Docker](#containerizare-cu-docker)
9. [Pipeline CI/CD cu Jenkins](#pipeline-cicd-cu-jenkins)
10. [Pull Request & Mentenanță](#pull-request--mentenanță)

---

## Descriere aplicație

Această aplicație web este dedicată serialului „The Blacklist” și oferă utilizatorilor o interfață simplă pentru a vizualiza:
- o descriere generală a serialului,
- personaje principale,
- trailere oficiale.

Aplicația este construită cu Flask și este modularizată astfel încât fiecare atribut (descriere, actori, trailere) este gestionat într-un fișier separat.

---

## Funcționalități & Versiuni

* **v1.0** – versiune funcțională cu:
  * pagină principală `/`
  * pagină cu descriere `/descriere`
  * pagină cu personaje `/actori`
  * pagină cu trailere `/trailer`
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

## Configurare & Instalare

1. **Clone repo & branch**:

```bash
git clone https://github.com/larisa-mortoiu/curs_vcgj_2025_filme.git
cd curs_vcgj_2025_filme
git checkout dev_Ichim_Ionut
```
2. **Rulare directă** (fără venv):
 ```bash
 python3 filme.py
 ```
3. **Rulare cu venv**:
```bash
source activeazavenv
python3 filme.py
```

Acces aplicație: [http://localhost:5077](http://localhost:5077)

---


## Prezentare interfață web

### 1. Homepage
![Homepage](https://github.com/larisa-mortoiu/curs_vcgj_2025_filme/blob/main_Ichim_Ionut/static/images/home_page.png)

### 2. Actori
![Characters](https://github.com/larisa-mortoiu/curs_vcgj_2025_filme/blob/main_Ichim_Ionut/static/images/actori.png)

### 3. Trailers
![Trailers](https://github.com/larisa-mortoiu/curs_vcgj_2025_filme/blob/main_Ichim_Ionut/static/images/trailer.png)

### 4. Descriere
![Trailers](https://github.com/larisa-mortoiu/curs_vcgj_2025_filme/blob/main_Ichim_Ionut/static/images/descriere.png)

---

## Testare cu Pytest

Testele validează:
- codul 200 pentru fiecare rută
- verificea pozelor de pe pagina actori

```bash
python3 -m pytest app/tests/ -q
```
![image](https://github.com/larisa-mortoiu/curs_vcgj_2025_filme/blob/main_Ichim_Ionut/static/images/pytest.png)
---

## Analiză statică cu Pylint

```bash
PYTHONPATH=. pylint --exit-zero app/tests/test_filme.py
PYTHONPATH=. pylint --exit-zero filme.py
```

Se folosește `--exit-zero` în Jenkins pentru a nu întrerupe pipeline-ul la warning-uri.
![image](https://github.com/larisa-mortoiu/curs_vcgj_2025_filme/blob/main_Ichim_Ionut/static/images/pylint.png)
---

## Containerizare cu Docker

```bash
docker build -t theblacklist-app .
docker run -p 5077:5077 theblacklist-app
```

Aplicația devine accesibilă la: [http://localhost:5077](http://localhost:5077)

---

## Pipeline CI/CD cu Jenkins

Pipeline-ul include pașii:

1. Build
2. Analiză statică cu Pylint
3. Testare unitară cu Pytest
4. Deploy: Pornire container local (`tneblacklist-container`)


Exemplu rulare cu succes:
![Pipeline](https://github.com/larisa-mortoiu/curs_vcgj_2025_filme/blob/main_Ichim_Ionut/static/images/pipeline.png)

---

## Pull Request & Mentenanță

* Dezvoltarea se face pe branch `dev_Ichim_Ionut`
* Se deschide PR către `main_Ichim_Ionut`
* După review și succes pipeline, se face merge și build automat pe `main`

---

--------------------------------------------------------------------
# Mihalcea Larisa Maria
## Cuprins
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
```
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
        ├── docker.png
        ├── docker-run.png
        ├── home.png
        ├── jenkins-blueocean.png
        ├── personaje.png
        ├── pull-request.png
        ├── recenzii.png
        ├── testare-pytest.png
        ├── trailer.png
        └── verificare-pylint.png
```


# Instrucțiuni de instalare
```
bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r quickrequirements.txt
python3 filme.py
```
Accesează aplicația la: [http://127.0.0.1:5050](http://127.0.0.1:5050)

# Pagini disponibile
- / – Pagina de start
- /despre – Despre serial
- /descriere – Prezentare detaliată
- /personaje – Actori principali
- /trailer – Trailer oficial YouTube
- /recenzii – Afișare și trimitere recenzii

### Capturi interfață
- ![home](https://github.com/larisa-mortoiu/curs_vcgj_2025_filme/blob/main_Mihalcea_Larisa/static/screenshots/home.png?raw=true)
- ![descriere](https://github.com/larisa-mortoiu/curs_vcgj_2025_filme/blob/main_Mihalcea_Larisa/static/screenshots/descriere.png?raw=true)
- ![personaje](https://github.com/larisa-mortoiu/curs_vcgj_2025_filme/blob/main_Mihalcea_Larisa/static/screenshots/personaje.png?raw=true)
- ![trailer](https://github.com/larisa-mortoiu/curs_vcgj_2025_filme/blob/main_Mihalcea_Larisa/static/screenshots/trailer.png?raw=true)
- ![recenzii](https://github.com/larisa-mortoiu/curs_vcgj_2025_filme/blob/main_Mihalcea_Larisa/static/screenshots/recenzii.png?raw=true)

# Testare Pytest
```
bash
pytest app/tests/
```
- verificare status 200 pentru rute
- testare adăugare recenzie

![pytest](https://github.com/larisa-mortoiu/curs_vcgj_2025_filme/blob/main_Mihalcea_Larisa/static/screenshots/testare-pytest.png?raw=true)

# Analiză cu Pylint
```
bash
pylint filme.py app/lib/*.py app/tests/*.py --exit-zero
```
![pylint](https://github.com/larisa-mortoiu/curs_vcgj_2025_filme/blob/main_Mihalcea_Larisa/static/screenshots/verificare-pylint.png?raw=true)

# Utilizare Docker
```
bash
docker build -t suits-app .
docker run -p 5050:5050 suits-app
```
![docker](https://github.com/larisa-mortoiu/curs_vcgj_2025_filme/blob/main_Mihalcea_Larisa/static/screenshots/docker-run.png?raw=true)
![docker](https://github.com/larisa-mortoiu/curs_vcgj_2025_filme/blob/main_Mihalcea_Larisa/static/screenshots/docker.png?raw=true)
# Integrare Jenkins
Pipeline-ul rulează automat:
- instalare dependințe
- pylint
- pytest
- build container Docker
![jenkins](https://github.com/larisa-mortoiu/curs_vcgj_2025_filme/blob/main_Mihalcea_Larisa/static/screenshots/jenkins-blueocean.png?raw=true)

# Pull Request
PR din dev_nume_student către main, aprobat și testat automat.
![pull-request](https://github.com/larisa-mortoiu/curs_vcgj_2025_filme/blob/main_Mihalcea_Larisa/static/screenshots/pull-request.png?raw=true)

# Surse
- [Flask Docs](https://flask.palletsprojects.com)
- [Pytest](https://docs.pytest.org)
- [Docker](https://docs.docker.com)
- [Jenkins](https://www.jenkins.io)
- [Pylint](https://pylint.pycqa.org)
--------------------------------------------------------------------
# Mirica Elena Ernestina

Această aplicație web a fost creată în cadrul cursului SCC și permite gestionarea unei colecții de filme/seriale, oferind funcționalități de bază. 
Se urmărește punerea în practică a noțiunilor esențiale învățate în cadrul disciplinei, de dezvoltare web, testare automată și integrare continuă.

Operațiile aplicației sunt gestionate prin rute bine definite în Flask. Docker a fost folosit pentru a crea un mediu de rulare consistent  indiferent de sistemul folosit. Jenkins a avut rolul de a automatiza testarea și integrarea continuă.

Pentru exemplificare, a fost prezentat serialul Bridgerton, realizat de Netflix.

## Cuprins

- [Tehnologii utilizate](#tehnologii-utilizate)
- [Setup](#setup)
- [Aducerea proiectului pe local](#aducerea-proiectului-pe-local)
- [Alte pachete folosite](#alte-pachete-folosite)
- [Fișiere din proiect](#fișiere-din-proiect)
- [Interfața web](#interfața-web)
- [Testare pytest](#testare-pytest)
- [Testare pylint](#testare-pylint)
- [Docker](#docker)
- [Jenkins](#jenkins)
- [Pull request](#pull-request)

## Tehnologii utilizate

- HTML/CSS
- Flask
- Python 3.10+
- Pytest
- Pylint
- Docker
- Jenkins

## Setup

A fost creat un director pe mașina virtuală  locală (Ubuntu 22.04) pentru dezvoltarea proiectului. Fișierele au fost editate în Visual Studio Code, descărcat de pe pagina lor oficială (https://code.visualstudio.com/?wt.mc_id=vscom_downloads).


## Aducerea proiectului pe local

Pentru a lucra local la proiect, este necesară clonarea acestuia de pe serverul GitHub și accesarea ramurii de dezvoltare relevante. Comenzile de mai jos realizează descărcarea codului și comutarea pe ramura dev_Mirica_Elena, unde se află implementarea in progress. 

Numai după testarea aplicației se pot adăuga modificările în main_Mirica_Elena.

 ```bash
git clone https://github.com/larisa-mortoiu/curs_vcgj_2025_filme.git
cd curs_vcgj_2025_filme
git checkout dev_Mirica_Elena
```

## Alte pachete folosite
 ```bash
sudo apt install git
sudo apt install python3
sudo apt install python3-pip
sudo apt install python3.12-venv
```

## Fișiere din proiect

- **`filme.py`** – Punctul de pornire al aplicației. Inițializează și rulează serverul Flask.
- **`requirements.txt`** – Lista cu toate bibliotecile necesare pentru rularea aplicației.
- **`Dockerfile`** – Conține instrucțiuni pentru construirea imaginii Docker.
- **`Jenkinsfile`** – Configurație pentru rularea automată a testelor și build-ului în Jenkins.
- **`pytest.ini`** – Setări pentru rularea testelor cu `pytest`.
- **`dockerstart.sh`** – Script pentru rularea aplicației în Docker.
- **`activeaza_venv`** – Activează mediul virtual pe Linux. Verifică întâi dacă există un mediu virtual activabil în directorul .venv. Dacă nu există, se creează și se instalează pachetele din requirements.txt. Altfell se activează mediul.
- **`start_app.sh`** – Script pentru pornirea aplicației în mediu local (după activeaza_venv). Serverul pornește la adresa 127.0.0.1, portul 5011. Poate fi accesată din browser.
- **`activeaza_venv_jenkins`** – Activează mediul virtual într-un mediu de CI precum Jenkins.
- **`test_filme.py`** – Testează funcționalitățile specifice din `filme.py`, cum ar fi validarea și manipularea datelor filmelor. Are definite mai multe funcții în interior.
- **`homepage.html`** – Pagina principală generală sau de introducere a aplicației (landing page).
- **`bridgerton.html`** – Pagină care poate combina informațiile despre serial într-o prezentare unificată.
- **`bridgerton_cast.html`** – Afișează distribuția serialului "Bridgerton".
- **`bridgerton_description.html`** – Pagina cu descrierea și contextul serialului "Bridgerton".
- **`bridgerton_cast.py`** – Script Python care gestionează date legate de distribuția serialului "Bridgerton".
- **`bridgerton_description.py`** – Script care conține descrierea serialului.
- **`README.md`** – Acest fișier, conținând descrierea proiectului și modul de realizare.



## Interfața web
Homepage

![Homepage](https://github.com/larisa-mortoiu/curs_vcgj_2025_filme/blob/dev_Mirica_Elena/static/images/homepage.png)

Pagina principală Bridgerton

![bridgerton.html](https://github.com/larisa-mortoiu/curs_vcgj_2025_filme/blob/dev_Mirica_Elena/static/images/bridgerton_html.png)

Descrierea Bridgerton

![bridgerton_description.html](https://github.com/larisa-mortoiu/curs_vcgj_2025_filme/blob/dev_Mirica_Elena/static/images/bridgerton_description_html.png)

Cast Bridgerton

![bridgerton_cast.html](https://github.com/larisa-mortoiu/curs_vcgj_2025_filme/blob/dev_Mirica_Elena/static/images/bridgerton_cast_html.png)

## Testare pytest

Aceste teste au rolul de a garanta stabilitatea logicii aplicației și de a semnala din timp orice eroare apărută în manipularea datelor filmelor. 

- **Structura descrierii (`bridgerton_description`)**
  - Verifică dacă textul returnat este împărțit în paragrafe corecte.
  - Asigură că fiecare paragraf are o lungime minimă pentru a evita conținutul gol sau superficial.
  - Confirmă că tagurile HTML `<p>` și `</p>` sunt corect închise.

- **Distribuția actorilor (`bridgerton_cast`)**
  - Se verifică extensia imaginilor actorilor (doar `.jpg`, `.jpeg` și `.png` sunt permise).
  - Numele fișierelor de imagine trebuie să fie lowercase, fără spații.
  - Se detectează și raportează eventualele duplicate în lista de actori.

Ele pot fi rulate folosind comanda:

```bash
pytest 
```

![Testare pytest](https://github.com/larisa-mortoiu/curs_vcgj_2025_filme/blob/dev_Mirica_Elena/static/images/pytest.png)

Testele au trecut cu succes.



## Testare pylint

Pylint este utilizat pentru a analiza calitatea codului din proiect. Acesta verifică respectarea convențiilor de numire și stil, complexitatea funcțiilor și claselor, prezența comentariilor și docstring-urilor, codul neutilizat (variabile, importuri) și posibile erori de logică, cum ar fi apeluri incorecte sau atribute lipsă.

Pentru a analiza codul, folosește comanda:

```bash
pylint [nume_fisier]
```

Următoarea imagine este un test pentru filme.py.

![Testare pylint](https://github.com/larisa-mortoiu/curs_vcgj_2025_filme/blob/dev_Mirica_Elena/static/images/pylint.png)

Se poate afirma că acest cod poate fi îmbunătățit.

## Docker

In Dockerfile se definesc:

- Se creează un utilizator (`elena_docker`).
- Se setează directorul de lucru la `/home/elena_docker`.
- Se copiază în container fișierele aplicației: codul sursă, șabloanele HTML, fișierele statice și scripturile.
- Se creează un mediu virtual Python în container (`.venv`) și se instalează automat dependențele din `requirements.txt`.
- Se folosește portul `5011` (portul pe care aplicația rulează în container).
- Aplicația este pornită folosind scriptul `dockerstart.sh`.

Script-ul dockerstart.sh activează mediul virtual și pornește aplicația Flask. De asemenea, setează variabila de mediu `FLASK_APP` necesară pentru inițializarea corectă a aplicației.

Comenzi utilizate:
```bash
docker build -t elena_docker:latest .
sudo docker run --name elena_docker -p 8020:5011 elena_docker:latest
sudo docker start elena_docker
sudo docker stop elena_docker
```

Output rulare dockertsart.sh:

![Docker](https://github.com/larisa-mortoiu/curs_vcgj_2025_filme/blob/dev_Mirica_Elena/static/images/docker.png)

La accesarea link-ului se va ajunge la aceeași pagină web, dar containerizată.

## Jenkins

Pipeline-ul definit rulează în orice agent disponibil (`agent any`) și conține următoarele etape principale:
- Se clonează automat codul sursă din branch-ul `main_Mirica_Elena` al repository-ului
- Se actualizează pip și se instalează toate pachetele necesare definite în requirements.txt, precum și instrumentele de testare pytest și pylint
- Se rulează automat testele din fișierele aflate în app/tests/, iar dacă unele teste eșuează, pipeline-ul continuă. Tot aici se rulează analiza statică pylint pe codul sursă și pe testele scrise


După rularea tuturor etapelor, Jenkins va afișa mesajul final Pipeline finished, indiferent de rezultatul testelor sau al analizei pylint.

![Jenkins](https://github.com/larisa-mortoiu/curs_vcgj_2025_filme/blob/dev_Mirica_Elena/static/images/jenkins.png)

Vizualizarea pipe-line-ului se face în Blue Ocean:

![Blue Ocean](https://github.com/larisa-mortoiu/curs_vcgj_2025_filme/blob/dev_Mirica_Elena/static/images/blue_ocean.png)

## Pull request

Am solocitat aprobarea unui coleg pentru a adăuga modificări în main_Mirica_Elena:

![Pull Request](https://github.com/larisa-mortoiu/curs_vcgj_2025_filme/blob/dev_Mirica_Elena/static/images/pull_request.png)

--------------------------------------------------------------------
# Mitrea Bogdan-Gabriel


# Cuprins
1. [Descriere aplicație](#descriere-aplicație)
2. [Versiune și funcționalități](#versiune-și-funcționalități)
3. [Tehnologii utilizate](#tehnologii-utilizate)
4. [Structura proiectului](#structura-proiectului)
5. [Configurare și rulare locală](#configurare-și-rulare-locală)
6. [Prezentare interfață web](#prezentare-interfață-web)
7. [Testare cu Pytest](#testare-cu-pytest)
8. [Analiză statică cu Pylint](#analiză-statică-cu-pylint)
9. [Containerizare cu Docker](#containerizare-cu-docker)
10. [Pipeline Jenkins](#pipeline-jenkins)
11. [Pull Request](#pull-request)
12. [Bibliografie](#bibliografie)

---

# Descriere aplicație

Aplicația este o platformă web construită cu Flask, care afișează informații despre serialul ales – „Dark”. Utilizatorul poate accesa o pagină de descriere și o pagină despre actori, fiecare organizată într-un mod vizual modern și interactiv. Aplicația este simplă, dar include toate funcționalitățile cerute: rutare, afișare de informații, containerizare, testare automată și integrare continuă.


# Versiune și funcționalități

Versiunea curentă oferă următoarele funcționalități:
- Pagina principală (homepage) cu un card atractiv despre serialul „Dark”
- Pagină dedicată serialului, cu două rute: „Descriere” și „Actori”
- Pagină de descriere cu text informativ și imagine integrată
- Pagină de actori cu layout grafic modern: carduri individuale pentru fiecare actor
- Navigare intuitivă prin butoane și linkuri
- Interfață responsive (bazată pe CSS)


# Tehnologii utilizate

- **Python + Flask** – framework pentru aplicația web
- **HTML + CSS** – layout și stilizare interfață
- **Pytest** – testare unitară
- **Pylint** – analiză statică a codului
- **Docker** – containerizare și rulare multiplatformă
- **Jenkins + Blue Ocean** – automatizare pipeline CI/CD


# Structura proiectului
Structura proiectului este organizată astfel:

```text
curs_vcgj_2025_filme/
├── app/
│   ├── lib/
│   │   ├── actori.py             # funcție pentru afișarea actorilor
│   │   └── descriere.py          # funcție pentru afișarea descrierii
│   └── tests/
│       ├── test_actori.py        # teste unitare pentru actori
│       └── test_descriere.py     # teste unitare pentru descriere
│
├── static/
│   ├── images/                   # imagini pentru interfața web
│   ├── screenshots/              # capturi de ecran pentru README
│   └── styles/
│       └── style.css             # stilizarea paginilor HTML
│
├── templates/
│   ├── index.html                # homepage
│   ├── dark.html                 # pagină principală pentru serial
│   ├── descriere.html            # pagină cu descrierea serialului
│   └── actori.html               # pagină cu actorii serialului
│
├── Dockerfile                    # fișier de build pentru containerizare
├── Jenkinsfile                   # definirea pipeline-ului Jenkins
├── filme.py                      # aplicația Flask
└── README.md                     # documentația proiectului
```


# Configurare și rulare locală

### 1. Clonare repository

```bash
git clone https://github.com/larisa-mortoiu/curs_vcgj_2025_filme.git
cd curs_vcgj_2025_filme
git checkout dev_Mitrea_Bogdan
```

### 2. Instalare dependențe

```bash
sudo apt update
sudo apt install python3 python3-pip docker.io
pip install flask pytest pylint
```

### 3. Rulare aplicație local

```bash
python3 filme.py
```

Aplicația poate fi accesată la: http://127.0.0.1:5000/


# Prezentare interfață web

### Homepage

Pagina principală conține un card vertical dedicat serialului **Dark**, care direcționează utilizatorul spre pagina dedicată serialului.

![homepage](https://github.com/larisa-mortoiu/curs_vcgj_2025_filme/blob/dev_Mitrea_Bogdan/static/screenshots/homepage.jpeg)


### Pagina „Dark”

Această pagină afișează titlul serialului și două carduri verticale:
- **Descriere**
- **Actori**

Cardurile au efecte vizuale la hover și sunt centrate pe ecran.

![page-dark](https://github.com/larisa-mortoiu/curs_vcgj_2025_filme/blob/dev_Mitrea_Bogdan/static/screenshots/page-dark.jpeg)


### Pagina descriere

Conține o imagine banner în partea de sus și un text informativ extins despre serial. Totul este centrat și responsive.

![descriere-dark-1](https://github.com/larisa-mortoiu/curs_vcgj_2025_filme/blob/dev_Mitrea_Bogdan/static/screenshots/descriere-dark-1.jpeg)

![descriere-dark-2](https://github.com/larisa-mortoiu/curs_vcgj_2025_filme/blob/dev_Mitrea_Bogdan/static/screenshots/descriere-dark-2.jpeg)

---

### Pagina actori

Actorii principali sunt afișați în carduri verticale, alternând între stânga și dreapta unei linii centrale. Fiecare card include:
- Numele actorului
- Rolul interpretat
- O scurtă descriere
- Imagine reprezentativă

![actori-dark-1](https://github.com/larisa-mortoiu/curs_vcgj_2025_filme/blob/dev_Mitrea_Bogdan/static/screenshots/actori-dark-1.jpeg)

![actori-dark-2](https://github.com/larisa-mortoiu/curs_vcgj_2025_filme/blob/dev_Mitrea_Bogdan/static/screenshots/actori-dark-2.jpeg)


# Testare cu Pytest

Testele unitare se află în directorul `app/tests/` și validează:

- Prezența actorului principal;
- Numărul minim de actori;
- Conținutul descrierii;
- Lungimea minimă a descrierii.

Comandă rulare locală:

```bash
pytest app/tests/
```

![teste-pytest](https://github.com/larisa-mortoiu/curs_vcgj_2025_filme/blob/dev_Mitrea_Bogdan/static/screenshots/teste-pytest.jpeg)

# Analiză statică cu Pylint

Analiza codului a fost realizată folosind `pylint` asupra următoarelor fișiere:

```bash
PYTHONPATH=$(pwd) pylint --exit-zero app/lib/*.py
PYTHONPATH=$(pwd) pylint --exit-zero app/tests/*.py
PYTHONPATH=$(pwd) pylint --exit-zero filme.py
```

![pylint](https://github.com/larisa-mortoiu/curs_vcgj_2025_filme/blob/dev_Mitrea_Bogdan/static/screenshots/pylint.jpeg)

Scor obținut: `10.00/10`

Toate regulile de stil, structură și documentare au fost respectate.


# Containerizare cu Docker

Containerizarea este un proces prin care aplicația este „împachetată” împreună cu toate dependințele ei (biblioteci, configurări etc.) într-un mediu izolat – numit **container** – astfel încât să poată rula pe orice sistem, indiferent de configurația locală.

Prin folosirea Docker:
- asigurăm portabilitatea aplicației (funcționează identic pe orice mașină)
- evităm problemele de tipul „merge la mine, dar nu la tine”
- putem construi imagini (versiuni exacte ale aplicației) care pot fi partajate ușor
- rulăm aplicația într-un mod controlat, fără a ne baza pe sistemul de operare local

### Structura fișierului `Dockerfile`

Fișierul `Dockerfile` definește pas cu pas **cum se construiește imaginea** Docker. Conținutul complet al `Dockerfile` folosit:

```text
FROM python:3.10-slim

WORKDIR /app

COPY . .

RUN pip install flask pytest

EXPOSE 5000

CMD ["python3", "filme.py"]
```

### Creare imagine container

După ce `Dockerfile` a fost scris și salvat în directorul principal al proiectului, putem construi imaginea rulând comanda:

```bash
docker build -t darkimage:v1 .
```

### Rulare container

După ce imaginea a fost creată, putem porni aplicația într-un container folosind comanda:

```bash
docker run -d --name darkcontainer -p 8020:5000 darkimage:v1
```
Aplicația devine accesibilă la adresa: http://127.0.0.1:8020

Containerele (active și oprite) pot fi vizualizate astfel:

```text
docker ps -a
```

# Pipeline Jenkins

Pentru procesul de Continuous Integration (CI), fișierul `Jenkinsfile` definește un pipeline format din patru etape esențiale pentru asigurarea calității aplicației:

1. **Build** – construiește imaginea Docker pe baza fișierului `Dockerfile`
2. **Pylint** – rulează analiza statică a codului (cu `--exit-zero` pentru a nu opri pipeline-ul)
3. **Pytest** – execută testele unitare definite în `app/tests/`
4. **Deploy** – pornește containerul rezultat la final, pe portul 8020

Acest pipeline este rulat într-un job de tip *Pipeline* și este configurat să ruleze direct din fișierul `Jenkinsfile` al proiectului. 
Lansarea serverului Jenkins local se face prin comanda:

```text
systemctl start jenkins
```

Interfața grafică Blue Ocean oferă o vizualizare clară de ansamblu a fiecărei etape:

![jenkins](https://github.com/larisa-mortoiu/curs_vcgj_2025_filme/blob/dev_Mitrea_Bogdan/static/screenshots/jenkins-pipeline.jpeg)


# Pull Request

Am realizat un PR din branch-ul de dezvoltare (dev_Mitrea_Bogdan) către branch-ul main (main_Mitrea_Bogdan)

![pull-request](https://github.com/larisa-mortoiu/curs_vcgj_2025_filme/blob/dev_Mitrea_Bogdan/static/screenshots/pull-request.jpeg)


# Bibliografie

- [Flask Documentation](https://flask.palletsprojects.com/)
- [Pytest Documentation](https://docs.pytest.org/)
- [Pylint Documentation](https://pylint.readthedocs.io/)
- [Docker Documentation](https://docs.docker.com/)
- [Jenkins Documentation](https://www.jenkins.io/doc/)

--------------------------------------------------------------------
# Mologani Adil

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
# Aplicatie Web "Filme" - Ali G Indahouse

Aceasta aplicatie web este realizata in Flask si are ca scop afisarea detaliilor despre filmul Ali G Indahouse, inclusiv o pagina de descriere si o pagina cu distributia. Proiectul este organizat modular, foloseste testare automata cu Pytest, analiza statica cu Pylint, containerizare cu Docker si integrare continua prin Jenkins.

---

## Cuprins

- [Versiune si functionalitati](#versiune-si-functionalitati)
- [Tehnologii utilizate](#tehnologii-utilizate)
- [Structura proiectului](#structura-proiectului)
- [Configurare si rulare locala](#configurare-si-rulare-locala)
- [Utilizare Docker](#utilizare-docker)
- [Pipeline Jenkins (CI)](#pipeline-jenkins-ci)
- [Testare cu Pytest](#testare-cu-pytest)
- [Verificare cod cu Pylint](#verificare-cod-cu-pylint)
- [Interfata Web](#interfata-web)
- [Pull Request](#pull-request)
- [Licenta](#licenta)

---

## Versiune si functionalitati

v1.0 - Navigare intre pagini, afisare dinamica a datelor, testare si pipeline CI:

- Pagina principala
- Pagina de descriere (cu date din get_description())
- Pagina distributie (cu date din get_cast())
- Cod modular Python
- Teste automate si analiza cod
- Rulare locala sau in container Docker
- Pipeline complet cu Jenkins

---

## Tehnologii utilizate

- Flask - framework web pentru logica aplicatiei
- HTML & CSS - structura si stilizare interfata
- Pytest - testare automata
- Pylint - verificare calitate cod
- Docker - rulare in container
- Jenkins - rulare automata a etapelor de CI

---

## Structura proiectului

```
curs_vcgj_2025_filme/
|-- app/
|   |-- lib/
|   |   |-- cast.py           # get_cast()
|   |   |-- description.py    # get_description()
|   |-- tests/
|       |-- test_filme.py     # teste Pytest
|-- static/
|   |-- images/               # imagini actori/banner
|   |-- styles/               # fisier CSS principal
|-- templates/
|   |-- index.html
|   |-- cast.html
|   |-- description.html
|-- filme.py                  # fisier principal Flask
|-- Dockerfile                # configuratie imagine Docker
|-- Jenkinsfile               # configuratie pipeline CI
|-- requirements.txt
|-- README.md
```

---

## Configurare si rulare locala

```bash
# Clonare repository
git clone https://github.com/hoangpham-dev/curs_vcgj_2025_filme.git
cd curs_vcgj_2025_filme
git checkout dev_Pham_Hoang

# Creare si activare mediu virtual
python3 -m venv .venv
source .venv/bin/activate

# Instalare dependinte
pip install -r requirements.txt

# Rulare aplicatie Flask
flask run
```

Acces: http://localhost:5011

---

## Utilizare Docker

```bash
# Construire imagine
docker build -t filme-app .

# Rulare container
docker run --name filme-container -p 5011:5011 filme-app![docker](https://github.com/user-attachments/assets/d0e8ff32-fd53-4c9b-ae1f-532e36e1acc0)

```
![docker](https://github.com/user-attachments/assets/48ca0b67-d625-4d8d-a147-860e160ddd9e)

---

## Pipeline Jenkins (CI)

Pipeline-ul automatizat face urmatorii pasi:

1. Clone repo - descarca proiectul
2. Set up venv - creeaza si activeaza mediu virtual
3. Install deps - instaleaza pachetele din requirements.txt
4. Code quality - ruleaza pylint pe filme.py, app/lib, app/tests
5. Run tests - executa testele definite cu pytest
6. Build Docker image - creeaza imagine cu aplicatia
7. Create container - defineste container Docker cu portul expus

### Exemplu comanda pentru pornirea Jenkins:
```bash
sudo systemctl start jenkins
```
![pipeline](https://github.com/user-attachments/assets/f8762feb-b3ab-47f8-9bb4-d68f4e01fd81)

---

## Testare cu Pytest

Testele se afla in app/tests/test_filme.py si verifica:
- get_description() returneaza un dictionar valid
- get_cast() returneaza o lista de actori cu atribute corecte

Comanda rulare:
```bash
pytest app/tests
```
![pytest](https://github.com/user-attachments/assets/6dfb509b-2d1e-4ccb-be42-16efdb46eefa)

---

## Verificare cod cu Pylint

Analiza calitatii codului se face pe modulele:
```bash
pylint app/lib/*.py
pylint app/tests/*.py
pylint filme.py
```

---

## Interfata Web

- Pagina principala - linkuri catre detalii film
![homepage](https://github.com/user-attachments/assets/01324652-e84c-4dd7-ac45-911786f2dcbd)

- Pagina Descriere - text generat din get_description()
![description](https://github.com/user-attachments/assets/93be87d3-0866-4f2f-9fd9-3a4eaa206d5b)

- Pagina Distributie - actorii si rolurile din get_cast(), afisate cu imagini si detalii
![cast](https://github.com/user-attachments/assets/73556d18-92b9-4b13-82e3-93119c4b77cf)


---

## Pull Request

Modificarile si Jenkinsfile-ul au fost adaugate pe branch-ul dev_Pham_Hoang, urmate de un PR catre main.
![merge](https://github.com/user-attachments/assets/3622b285-0fb5-40d8-8418-1eb09f9e2af3)


--------------------------------------------------------------------
# Popa Andreea Elena

# Cuprins
1. [Prezentarea generala a aplicatiei](#prezentarea-generala-a-aplicatiei)
2. [Versiuni si functionalitati disponibile](#versiuni-si-functionalitati-disponibile)
3. [Tehnologii utilizate](#tehnologii-utilizate)
4. [Structura proiectului](#structura-proiectului)
5. [Instructiuni de instalare si configurare](#instructiuni-de-instalare-si-configurare)
6. [Interfata web prezentare](#interfata-web-prezentare)
7. [Testare cu pytest](#testare-cu-pytest)
8. [Verificare statica cu pylint](#verificare-statica-cu-pylint)
9. [Utilizare Docker si containerizare aplicatie](#utilizare-docker-si-containerizare-aplicatie)
10. [Pipeline Jenkins](#pipeline-jenkins)
11. [Pull Request](#pull-request)
12. [Bibliografie](#bibliografie)

# Prezentarea generala a aplicatiei
Aplicația *MovieHub* este o aplicație web dezvoltată cu Flask, având ca scop afișarea detaliilor despre filmul *The Imitation Game (2014)*. Utilizatorii pot naviga printr-o interfață simplă și intuitivă pentru a vedea o descriere completă, distribuția actorilor (cu poze) și trailerul oficial.

# Versiuni si functionalitati disponibile
Versiunea curentă `v0` include:
- afișarea unui film cu două atribute: descriere și distribuție
- galerie actori cu imagini egale
- trailer video embedded (YouTube)
- navigare între pagini cu linkuri de întoarcere
- testare automată cu Pytest
- analiză statică cu Pylint
- rulare locală și containerizare cu Docker
- pipeline CI/CD cu Jenkins

# Tehnologii utilizate
- **Flask** – framework backend pentru rute și logică aplicație
- **HTML + CSS** – interfață și stilizare web
- **Pytest** – testare unitară
- **Pylint** – analiză statică a codului Python
- **Docker** – rulare în container
- **Jenkins** – CI/CD cu lint, test și build automat

# Structura proiectului
```
curs_vcgj_2025_filme/
├── app
│   ├── __init__.py
│   ├── lib
│   │   ├── actori.py
│   │   ├── descriere.py
│   │   ├── __init__.py
│   │   └── __pycache__/
│   └── tests
│       ├── __init__.py
│       ├── __pycache__ /
│       ├── test_actori.py
│       ├── test_descriere.py
│       └── test_filme.py
├── Dockerfile
├── filme.py
├── Jenkinsfile
├── LICENSE
├── __pycache__/
├── quickrequirements.txt
├── readme_andreea_temp.md
├── README.md
└── static
    └── screenshots/
9 directories, 34 files
```

![structura-proiect](https://github.com/larisa-mortoiu/curs_vcgj_2025_filme/blob/main_Popa_Andreea/static/screenshots/structura-proiect.png?raw=true)

# Instructiuni de instalare si configurare
```bash
# clonare repo
cd ~/Desktop
git clone https://github.com/larisa-mortoiu/curs_vcgj_2025_filme.git
cd curs_vcgj_2025_filme
git checkout dev_popa_andreea

# activare mediu virtual
source activeaza_venv.sh

# instalare dependinte
pip install -r quickrequirements.txt

# rulare aplicatie
. ./ruleaza_app.sh
```

Aplicația este accesibilă la: [http://127.0.0.1:5050](http://127.0.0.1:5050)

# Interfata web prezentare
- `/` – Pagina principală cu poster și buton
- `/imitation-game` – Detalii film
- `/imitation-game/descriere` – Descriere detaliată
- `/imitation-game/actori` – Galerie actori cu poze egale
- `/imitation-game/trailer` – Trailer embed din YouTube

## Capturi interfață
![homepage](https://github.com/larisa-mortoiu/curs_vcgj_2025_filme/blob/main_Popa_Andreea/static/screenshots/homepage.png?raw=true)
![filmpage](https://github.com/larisa-mortoiu/curs_vcgj_2025_filme/blob/main_Popa_Andreea/static/screenshots/film-page.png?raw=true)
![descriere](https://github.com/larisa-mortoiu/curs_vcgj_2025_filme/blob/main_Popa_Andreea/static/screenshots/descriere.png?raw=true)
![actori](https://github.com/larisa-mortoiu/curs_vcgj_2025_filme/blob/main_Popa_Andreea/static/screenshots/actori.png?raw=true)
![trailer](https://github.com/larisa-mortoiu/curs_vcgj_2025_filme/blob/main_Popa_Andreea/static/screenshots/trailer.png?raw=true)

# Testare cu pytest
```bash
pytest app/tests/
```
Teste acoperite:
- status 200 pentru fiecare rută
- conținut `descriere` (cu „Turing” / „Enigma”)
- conținut `actori` (cu „Cumberbatch” / „Knightley”)
- import corect funcții din `app/lib`

## Rulare pytest
![testare-pytest](https://github.com/larisa-mortoiu/curs_vcgj_2025_filme/blob/main_Popa_Andreea/static/screenshots/testare-pytest.png?raw=true)

# Verificare statica cu pylint
```bash
pylint filme.py app/lib/*.py app/tests/*.py --exit-zero
```
Se validează stilul și structurarea codului fără oprirea pipeline-ului (prin `--exit-zero`).

![verificare-pylint](https://github.com/larisa-mortoiu/curs_vcgj_2025_filme/blob/main_Popa_Andreea/static/screenshots/verificare-pylint.png?raw=true)

# Utilizare Docker si containerizare aplicatie
```bash
docker build -t filme-app .
docker run -p 5050:5050 filme-app
```
Aplicația devine accesibilă la [http://localhost:5050](http://localhost:5050)

![docker-build](https://github.com/larisa-mortoiu/curs_vcgj_2025_filme/blob/main_Popa_Andreea/static/screenshots/docker-build.png?raw=true)
![docker-run](https://github.com/larisa-mortoiu/curs_vcgj_2025_filme/blob/main_Popa_Andreea/static/screenshots/docker-run.png?raw=true)

# Pipeline Jenkins
Pipeline-ul definit în `Jenkinsfile` conține etape de:
- build mediu virtual
- rulare `pylint`
- rulare `pytest`
- build Docker image
- run container cu `filme.py`

Execuția este vizibilă în interfața Blue Ocean Jenkins.

![jenkins-blueocean](https://github.com/larisa-mortoiu/curs_vcgj_2025_filme/blob/main_Popa_Andreea/static/screenshots/jenkins-blueocean.png?raw=true)

# Pull Request
PR creat din branch `dev_popa_andreea` către `main`, aprobat de reviewer și validat prin rularea testelor automate în Jenkins.

![pull-request](https://github.com/larisa-mortoiu/curs_vcgj_2025_filme/blob/main_Popa_Andreea/static/screenshots/pull-request.png?raw=true)

# Bibliografie
- [Flask](https://flask.palletsprojects.com)
- [Pytest](https://docs.pytest.org)
- [Docker](https://docs.docker.com)
- [Jenkins](https://www.jenkins.io/doc)
- [Pylint](https://pylint.pycqa.org)



--------------------------------------------------------------------
# Sandu Victor Codrin
# Bob Marley: One Love – Aplicație Web

Aplicație web dezvoltată în cadrul cursului VCGJ 2025, dedicată filmului **Bob Marley: One Love**.  
Aceasta oferă informații despre film, actori și descrierea acestuia, într-o interfață modernă și responsivă.

---

## Capturi de ecran

### Pagina principală
![Pagina principală](https://raw.githubusercontent.com/larisa-mortoiu/curs_vcgj_2025_filme/main_Sandu_Codrin/static/images/ss/home.png)

### Pagina cu descrierea filmului
![Descriere film](https://raw.githubusercontent.com/larisa-mortoiu/curs_vcgj_2025_filme/main_Sandu_Codrin/static/images/ss/descriere.png)

### Pagina cu actorii
![Actori](https://raw.githubusercontent.com/larisa-mortoiu/curs_vcgj_2025_filme/main_Sandu_Codrin/static/images/ss/actori.png)

### Pagina detaliată a filmului
![Detalii film](https://raw.githubusercontent.com/larisa-mortoiu/curs_vcgj_2025_filme/main_Sandu_Codrin/static/images/ss/film.png)

---

## Funcționalități

- Afișarea descrierii detaliate a filmului
- Listarea actorilor principali
- Design responsiv utilizând [UIkit](https://getuikit.com/)
- Imagini optimizate pentru o experiență vizuală plăcută
- Testare automată cu `pytest`
- Integrare continuă cu Jenkins
- Containerizare cu Docker

---

## Tehnologii utilizate

- Python 3.10
- Flask
- UIkit
- Docker
- Jenkins
- Pytest

---

## Structura proiectului

```text
├── app/
│   ├── lib/
│   │   ├── actori.py
│   │   └── descriere.py
│   ├── tests/
│   │   └── test_file.py
│   ├── templates/
│   │   ├── base.html
│   │   ├── home.html
│   │   ├── descriere.html
│   │   ├── actori.html
│   │   └── film.html
│   └── static/
│       ├── styles/
│       │   └── style.css
│       └── images/
│           └── ss/
├── Dockerfile
├── Jenkinsfile
├── quickrequirements.txt
├── pytest.ini
├── filme.py
├── activeaza_venv_jenkins
├── ruleaza_app.sh
└── README.md
```

---

## Instrucțiuni de rulare

### Local

```bash
git clone https://github.com/larisa-mortoiu/curs_vcgj_2025_filme.git
cd curs_vcgj_2025_filme
python3 -m venv venv
source venv/bin/activate
pip install -r quickrequirements.txt
python filme.py
```

Accesează aplicația la: [http://localhost:5000](http://localhost:5000)

---

### Cu Docker

```bash
docker build -t bobmarley_app .
docker run -d -p 5000:5000 bobmarley_app
```

Accesează aplicația la: [http://localhost:5000](http://localhost:5000)

---

### Cu Jenkins

1. Asigură-te că Jenkins este instalat și activ
2. Creează un job de tip Pipeline
3. Configurează:
   - SCM: Git
   - URL: `https://github.com/larisa-mortoiu/curs_vcgj_2025_filme.git`
   - Branch: `main_Sandu_Codrin`
4. Rulează jobul și urmărește rezultatele în consola Jenkins

---

## Testare

Pentru a rula testele:

```bash
pytest app/tests/
```

---

## Licență

Acest proiect este licențiat sub MIT License.

---

Pentru detalii suplimentare, accesează branch-ul:  
[main_Sandu_Codrin](https://github.com/larisa-mortoiu/curs_vcgj_2025_filme/tree/main_Sandu_Codrin)

--------------------------------------------------------------------
# Simion Razvan Marian
Projet_SCC - Gestionare Filme cu Flask, Docker și Jenkins

**Autor:** Simion Razvan-Marian  
**Branch activ:** `dev_Simion_Razvan`  
**Repository:** [github.com/larisa-mortoiu/curs_vcgj_2025_filme](https://github.com/larisa-mortoiu/curs_vcgj_2025_filme.git)

---

Descriere

**Proiect_SCC** este o aplicație web dezvoltată cu [Flask](https://flask.palletsprojects.com/), ce oferă o interfață simplă și intuitivă pentru afișarea informațiilor despre un serial. Proiectul integrează tehnologii moderne precum **Docker** și **Jenkins** pentru a facilita dezvoltarea continuă și rularea în containere.

---

Funcționalități principale

- Pagina principală cu titlul serialului și trailer integrat;
- Pagina cu actorii principali ai serialului;
- Pagina de descriere a serialului;
- Stil personalizat folosind CSS și butoane interactive;
- Arhitectură modulară:
  - `filme.py` – logica aplicației
  - `templates/` – pagini HTML
  - `static/` – stiluri și fișiere media

---

Testare

Aplicația a fost testată folosind următoarele metode:

- Rulare locală:
  ```bash
  python3 filme.py
  ```

- Build & run în Docker:
  ```bash
  docker build -t mechanicressurection .
  docker run -p 5000:5000 mechanicressurection
  ```

- Verificarea stării containerului:
  ```bash
  docker ps
  ```

- Accesarea aplicației:
  [http://localhost:5000](http://localhost:5000)

- Testare unitară cu **Pytest**:

  ![Pytest](https://github.com/user-attachments/assets/7293bb1b-aa9b-41d4-b223-de7999d192a8)

---

Docker

Comenzile folosite pentru containerizare:

```bash
docker build -t mechanicressurection .
docker run -p 5000:5000 mechanicressurection
```

Aplicația devine accesibilă în browser la:  
**http://localhost:5000**

![Docker](https://github.com/user-attachments/assets/01135ec9-8c47-4ef3-9d3d-e7d64e906136)

---

Integrare Continuă (CI) cu Jenkins

Am automatizat procesul de build și testare printr-un job configurat în **Jenkins**, folosind:

- Tip job: **Pipeline**
- Sursa: **Script from SCM**
- Repo: [GitHub - curs_vcgj_2025_filme](https://github.com/larisa-mortoiu/curs_vcgj_2025_filme.git)
- Branch: `dev_Simion_Razvan`
- Path script: `Jenkinsfile`

Numele jobului în Jenkins: **MechanicRessurection-Pipeline**

![Jenkins](https://github.com/user-attachments/assets/e3a3680c-cc68-4779-bc42-09bbcde374a7)

---

Structura proiectului

```
Projet_SCC/
├── Dockerfile
├── filme.py
├── requirements.txt
├── templates/
│   ├── index.html
│   ├── actori.html
│   └── descriere.html
├── static/
│   └── style.css
└── Jenkinsfile
```

---

Tehnologii utilizate

- [Python 3](https://www.python.org/)
- [Flask](https://flask.palletsprojects.com/)
- [Docker](https://www.docker.com/)
- [Jenkins](https://www.jenkins.io/)
- [Pytest](https://docs.pytest.org/)

--------------------------------------------------------------------
# Tofan Ionut Lucian
# Proiect SCC – Interstellar WEB APP

**Autor:** Tofan Ionut Lucian (Grupa 442D)

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
![Docker](https://github.com/user-attachments/assets/1f1b00d0-ef65-4b04-b675-6a5cf2bc2780)

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
--------------------------------------------------------------------
# Zarafin Radu Adrian
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
PYTHONPATH=. pylint --exit-zero app/tests/test_filme.py
PYTHONPATH=. pylint --exit-zero filme.py
```

Se folosește `--exit-zero` în Jenkins pentru a nu întrerupe pipeline-ul la warning-uri.
![image](https://github.com/larisa-mortoiu/curs_vcgj_2025_filme/blob/dev_Zarafin_Radu/static/screenshots/testare_pylint.png)
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
--------------------------------------------------------------------



