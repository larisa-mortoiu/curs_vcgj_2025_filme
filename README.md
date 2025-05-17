# Proiect SCC – JoJo's Bizarre Adventure

Acest fișier **README.md** descrie proiectul "Proiect SCC JoJo's Bizarre Adventure", implementat în cadrul cursului **Servicii Cloud și Containerizare (SCC)**.

---

## 🌟 Descriere

Aplicația web prezintă universul **JoJo's Bizarre Adventure**:

* **Pagina de start** cu informații despre serie.
* **Pagina Trailers** cu embed-uri YouTube pentru trailere.
* **Pagina Characters** cu listă de personaje.
* **Pagina detaliu personaj** cu imagine, nume, parte (season), descriere și actor vocal.

### Tehnologii folosite

* **Flask (Python)** – backend și rutare
* **HTML + CSS** – interfață și stilizare (Jinja2 pentru templating)
* **Docker** – containerizare a aplicației
* **Jenkins** – pipeline de build, test și deploy

---

## 🚀 Cum rulezi local (fără Docker și fără virtualenv)

1. Clonează repo-ul și schimbă branch:

   ```bash
   git clone https://github.com/larisa-mortoiu/curs_vcgj_2025_filme.git
   cd curs_vcgj_2025_filme
   git checkout main_Al-Hajjih_Kais
   ```
2. Rulează aplicația direct cu Python:

   ```bash
   python3 filme.py
   ```
3. Accesează în browser: [http://127.0.0.1:5000](http://127.0.0.1:5000)

---

## 🐳 Cum rulezi cu Docker

1. Build imagine Docker:

   ```bash
   docker build -t jojo-scc-app .
   ```
2. Rulează container:

   ```bash
   docker run --rm -p 5000:5000 jojo-scc-app
   ```
3. Accesează în browser: [http://127.0.0.1:5000](http://127.0.0.1:5000)

---

## 🧪 Testare

* Testele unitare se află în folderul `app/tests/` și pot fi rulate cu:

  ```bash
  pytest -q
  ```
* Smoke-test intern este integrat în pipeline-ul Jenkins.

---

## ⚙️ Pipeline Jenkins

Fișierul `Jenkinsfile` din root definește pașii pipeline-ului:

1. **Checkout** sursă
2. **Build Image** – `docker build`
3. **Unit Tests (in-container)** – rulează `pytest` în container
4. **Smoke Test** – testează endpoint-ul interactiv
5. **Push to Hub** – pe branch `main`, face login și `docker push`

---

## 📂 Structura proiectului

```text
├── app/
│   └── lib/        # cod logic și date despre personaje
│   └── tests/      # teste unitare
├── static/         # fișiere CSS și imagini
├── templates/      # fișiere HTML (Jinja2)
├── filme.py        # aplicația Flask
├── requirements.txt
├── Dockerfile
├── dockerstart.sh  # script entrypoint
├── Jenkinsfile
├── README.md       # acest fișier
└── ...
```

---

## 👤 Autor

* Al-Hajjih Kais (Grupa 442D)

---

> ✨ Succes la evaluare și mulțumesc pentru parcurgerea proiectului!

