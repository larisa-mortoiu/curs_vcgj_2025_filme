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
