# Proiect SCC – JoJo's Bizarre Adventure 🌟

Acest proiect reprezintă o aplicație web dezvoltată în cadrul cursului **Servicii Cloud și Containerizare (SCC)**. Aplicația este dedicată universului **JoJo's Bizarre Adventure** și oferă utilizatorilor o experiență interactivă cu pagini despre personaje, trailere și detalii despre fiecare protagonist.

---

## 🔧 Tehnologii folosite

- **Flask (Python)** – pentru partea de backend / server
- **HTML + CSS** – pentru partea de frontend
- **Jinja2** – motor de template-uri integrat în Flask
- **Git** – pentru versionare și managementul codului

---

## ⚙️ Funcționalități implementate

- ✅ Pagină de start cu prezentarea universului JoJo
- ✅ Pagină cu trailere video
- ✅ Pagină cu lista personajelor
- ✅ Pagină detaliată pentru fiecare personaj: imagine, nume, parte, descriere etc.
- ✅ Navigare ușoară între pagini
- ✅ Stilizare completă cu CSS

---

## 🧪 Testare

- Aplicația a fost testată manual în browser (`localhost`) și funcționează corect.
- În prezent, nu există încă integrare automatizată cu Jenkins.

---

## 📦 Containerizare (în lucru)

- 🔧 Urmează integrarea cu Docker (creare Dockerfile)
- 🔧 Urmează integrarea cu Jenkins (Jenkinsfile și pipeline)

---

## 📁 Structura proiectului

```bash
├── app/
│   └── lib/ (codul sursă)
├── templates/ (fișiere HTML)
├── static/ (fișiere CSS și imagini)
├── filme.py (main Flask app)
├── README.md (acest fișier)
└── ...
