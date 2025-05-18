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
