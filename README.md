# Proiect SCC – JoJo's Bizarre Adventure

Acest fișier **README.md** descrie proiectul "Proiect SCC JoJo's Bizarre Adventure", implementat în cadrul cursului **Servicii Cloud și Containerizare (SCC)**.

---

## 🌟 Descriere

Aplicația web prezintă universul **JoJo's Bizarre Adventure**:

* **Pagina de start** cu informații despre serie.
  ![image](https://github.com/user-attachments/assets/74a2f34b-7b2f-4a9e-a900-c06cdadfb1d8)

* **Pagina Trailers** cu embed-uri YouTube pentru trailere.
  ![image](https://github.com/user-attachments/assets/4a502892-f7e7-4387-baa7-49d437da784b)

* **Pagina Characters** cu lista de personaje.
  ![image](https://github.com/user-attachments/assets/b1a81241-4560-4a99-94d9-43b8b2928ebb)

* **Pagina detaliu personaj** cu imagine, nume, parte (sezon), descriere și voice actor.
  ![image](https://github.com/user-attachments/assets/46762e9e-3ba5-4749-b955-8dda3465a197)


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
  python3 -m pytest app/tests/test_filme.py -q
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

 ![image](https://github.com/user-attachments/assets/db7f4abf-6c4d-4a1f-8509-b897fc4ca1ab)

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
