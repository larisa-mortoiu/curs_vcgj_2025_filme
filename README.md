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
