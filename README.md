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
