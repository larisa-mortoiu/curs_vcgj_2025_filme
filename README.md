# Proiect Web Simplu: Descriere și Distribuție Filme

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

## Prezentarea Paginilor Web
Aplicația web oferă o navigare simplă între pagini:

* **Pagina Principală** Afișează o listă de filme disponibile. Fiecare element din listă este un link către pagina de detalii a filmului respectiv.
  
* **Pagina Detaliilor Filmului** Prezintă informații scurte despre film (regie, genuri, durată, an lansare) și afișează posterul filmului. Conține butoane pentru a naviga către pagina de descriere completă, pagina de distribuție și înapoi la lista principală.
  
* **Pagina Descrierii Filmului** Afișează descrierea detaliată a filmului, preluată din modulul `biblioteca_filme.py`.
  
* **Pagina Distribuției Filmului** Listează actorii principali, personajele interpretate și o scurtă descriere a personajului, însoțită de o fotografie a actorului/personajului. Datele sunt preluată din modulul `biblioteca_filme.py`.

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
    docker run --name scc_container -p 8020:25568 scc:latest
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
