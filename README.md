# 📺 The Walking Dead - Aplicație Web cu Flask

Acest proiect este o aplicație web simplă dezvoltată în Python folosind Flask. Scopul aplicației este să prezinte informații despre serialul *The Walking Dead* – o descriere generală, o listă de actori, trailerul video și o pagină de prezentare generală.

Aplicația este containerizată folosind Docker și poate fi rulată local sau în medii izolate.

---

## 🗂️ Structura proiectului

curs_vcgj_2025_filme/
├── app/ # (opțional - funcționalități suplimentare)
├── static/ # Fișiere media și stiluri CSS (poster, trailer, style.css)
├── templates/ # Template-uri HTML (base, actori, prezentare, descriere, trailer)
├── filme.py # Aplicația Flask
├── requirements.txt # Dependențele Python
├── Dockerfile # Definirea imaginii Docker
├── .dockerignore # Fisiere excluse din build Docker
└── README.md # Acest fișier

---

## 🔧 Setup rapid

### ▶️ Rulare fără Docker

1. Activează mediul virtual:
```bash
python3 -m venv venv
source venv/bin/activate

2. Instalează dependențele:
pip install -r requirements.txt

3. Pornește aplicația:
python3 filme.py
Aplicația va fi disponibilă la: http://localhost:5000



Rulare cu Docker

1. Build imagine:
docker build -t walking-dead-app .

2. Rulează containerul:
docker run -p 5011:5011 walking-dead-app
Accesează aplicația la: http://localhost:5011

Funcționalități UI

    -Navigare intuitivă între pagini
    -Design curat, cu CSS personalizat
    -Responsiv și ușor de extins


Autor
Proiect dezvoltat de Băncilă Vlad, în cadrul cursului VCGJ 2025 - Sisteme Web pentru Conținut Cinematografic

