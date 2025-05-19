🎬 Bob Marley: One Love – Aplicație Web
Aplicație web dezvoltată în cadrul cursului VCGJ 2025, dedicată filmului Bob Marley: One Love. Aceasta oferă informații despre film, actori și descrierea acestuia, într-o interfață modernă și responsivă.

📸 Capturi de ecran
Pagina principală

Pagina cu descrierea filmului

Pagina cu actorii

Pagina detaliată a filmului

🚀 Funcționalități
Afișarea descrierii detaliate a filmului.

Listarea actorilor principali.

Design responsiv utilizând UIkit.

Imagini optimizate pentru o experiență vizuală plăcută.

Testare automată cu pytest.

Integrare continuă cu Jenkins.

Containerizare cu Docker.

🛠️ Tehnologii utilizate
Python 3.10

Flask

UIkit

Docker

Jenkins

pytest

📦 Structura proiectului
arduino
Copiază
Editează

├── app/
│   ├── __init__.py
│   ├── routes.py
│   ├── templates/
│   │   ├── base.html
│   │   ├── home.html
│   │   ├── descriere.html
│   │   ├── actori.html
│   │   └── film.html
│   └── static/
│       ├── css/
│       │   └── style.css
│       └── images/
│           └── ss/
├── Dockerfile
├── Jenkinsfile
├── requirements.txt
├── pytest.ini
├── README.md
└── run.py
⚙️ Instrucțiuni de rulare
Local
Clonează repository-ul:
Future of the Force

bash
Copiază
Editează
git clone https://github.com/larisa-mortoiu/curs_vcgj_2025_filme.git
cd curs_vcgj_2025_filme
Activează mediul virtual:
clutchpoints.com
+7
Slice of SciFi
+7
niewmedia.com
+7

bash
Copiază
Editează
source venv/bin/activate
Instalează dependențele:

bash
Copiază
Editează
pip install -r requirements.txt
Rulează aplicația:

bash
Copiază
Editează
python run.py
Accesează aplicația la http://localhost:5000.

Cu Docker
Construiește imaginea Docker:

bash
Copiază
Editează
docker build -t bobmarley_app .
Rulează containerul:

bash
Copiază
Editează
docker run -d -p 5000:5000 bobmarley_app
Accesează aplicația la http://localhost:5000.

Cu Jenkins
Asigură-te că Jenkins este instalat și rulează.

Configurează un nou job de tip Pipeline.

În secțiunea Pipeline, selectează Pipeline script from SCM și introdu URL-ul repository-ului.

Salvează și rulează job-ul.

✅ Testare
Pentru a rula testele automate:

bash
Copiază
Editează
pytest
📄 Licență
Acest proiect este licențiat sub MIT License.
bobmarleyonelove.ie
+1
cine-techno.com
+1

Pentru mai multe informații și contribuții, vizitează repository-ul principal: curs_vcgj_2025_filme.
