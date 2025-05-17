# Aplicatie Web "Filme" - Ali G Indahouse

Aceasta aplicatie web este realizata in Flask si are ca scop afisarea detaliilor despre filmul Ali G Indahouse, inclusiv o pagina de descriere si o pagina cu distributia. Proiectul este organizat modular, foloseste testare automata cu Pytest, analiza statica cu Pylint, containerizare cu Docker si integrare continua prin Jenkins.

---

## Versiune si functionalitati

v1.0 - Navigare intre pagini, afisare dinamica a datelor, testare si pipeline CI:

- Pagina principala
- Pagina de descriere (cu date din get_description())
- Pagina distributie (cu date din get_cast())
- Cod modular Python
- Teste automate si analiza cod
- Rulare locala sau in container Docker
- Pipeline complet cu Jenkins

---

## Tehnologii utilizate

- Flask - framework web pentru logica aplicatiei
- HTML & CSS - structura si stilizare interfata
- Pytest - testare automata
- Pylint - verificare calitate cod
- Docker - rulare in container
- Jenkins - rulare automata a etapelor de CI

---

## Structura proiectului

```
curs_vcgj_2025_filme/
|-- app/
|   |-- lib/
|   |   |-- cast.py           # get_cast()
|   |   |-- description.py    # get_description()
|   |-- tests/
|       |-- test_filme.py     # teste Pytest
|-- static/
|   |-- images/               # imagini actori/banner
|   |-- styles/               # fisier CSS principal
|-- templates/
|   |-- index.html
|   |-- cast.html
|   |-- description.html
|-- filme.py                  # fisier principal Flask
|-- Dockerfile                # configuratie imagine Docker
|-- Jenkinsfile               # configuratie pipeline CI
|-- requirements.txt
|-- README.md
```

---

## Configurare si rulare locala

```bash
# Clonare repository
git clone https://github.com/hoangpham-dev/curs_vcgj_2025_filme.git
cd curs_vcgj_2025_filme
git checkout dev_Pham_Hoang

# Creare si activare mediu virtual
python3 -m venv .venv
source .venv/bin/activate

# Instalare dependinte
pip install -r requirements.txt

# Rulare aplicatie Flask
flask run
```

Acces: http://localhost:5011

---

## Utilizare Docker

```bash
# Construire imagine
docker build -t filme-app .

# Rulare container
docker run --name filme-container -p 5011:5011 filme-app![docker](https://github.com/user-attachments/assets/d0e8ff32-fd53-4c9b-ae1f-532e36e1acc0)

```
![docker](https://github.com/user-attachments/assets/48ca0b67-d625-4d8d-a147-860e160ddd9e)

---

## Pipeline Jenkins (CI)

Pipeline-ul automatizat face urmatorii pasi:

1. Clone repo - descarca proiectul
2. Set up venv - creeaza si activeaza mediu virtual
3. Install deps - instaleaza pachetele din requirements.txt
4. Code quality - ruleaza pylint pe filme.py, app/lib, app/tests
5. Run tests - executa testele definite cu pytest
6. Build Docker image - creeaza imagine cu aplicatia
7. Create container - defineste container Docker cu portul expus

### Exemplu comanda pentru pornirea Jenkins:
```bash
sudo systemctl start jenkins
```
![pipeline](https://github.com/user-attachments/assets/f8762feb-b3ab-47f8-9bb4-d68f4e01fd81)

---

## Testare cu Pytest

Testele se afla in app/tests/test_filme.py si verifica:
- get_description() returneaza un dictionar valid
- get_cast() returneaza o lista de actori cu atribute corecte

Comanda rulare:
```bash
pytest app/tests
```
![pytest](https://github.com/user-attachments/assets/6dfb509b-2d1e-4ccb-be42-16efdb46eefa)

---

## Verificare cod cu Pylint

Analiza calitatii codului se face pe modulele:
```bash
pylint app/lib/*.py
pylint app/tests/*.py
pylint filme.py
```

---

## Interfata Web

- Pagina principala - linkuri catre detalii film
![homepage](https://github.com/user-attachments/assets/01324652-e84c-4dd7-ac45-911786f2dcbd)

- Pagina Descriere - text generat din get_description()
![description](https://github.com/user-attachments/assets/93be87d3-0866-4f2f-9fd9-3a4eaa206d5b)

- Pagina Distributie - actorii si rolurile din get_cast(), afisate cu imagini si detalii
![cast](https://github.com/user-attachments/assets/73556d18-92b9-4b13-82e3-93119c4b77cf)


---

## Pull Request

Modificarile si Jenkinsfile-ul au fost adaugate pe branch-ul dev_Pham_Hoang, urmate de un PR catre main.
![merge](https://github.com/user-attachments/assets/3622b285-0fb5-40d8-8418-1eb09f9e2af3)

