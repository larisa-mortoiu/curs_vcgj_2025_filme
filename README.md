# Proiect SCC – The Blacklist Web App

**Autor:** Ichim Alexandru-Ionut (Grupa 442D)

---

## Cuprins

1. [Descriere aplicație](#descriere-aplicație)
2. [Funcționalități & Versiuni](#funcționalități--versiuni)
3. [Tehnologii folosite](#tehnologii-folosite)
4. [Configurare & Instalare](#configurare--instalare)
5. [Prezentare interfață web](#prezentare-interfață-web)
6. [Testare cu Pytest](#testare-cu-pytest)
7. [Analiză statică cu Pylint](#analiză-statică-cu-pylint)
8. [Containerizare cu Docker](#containerizare-cu-docker)
9. [Pipeline CI/CD cu Jenkins](#pipeline-cicd-cu-jenkins)
10. [Pull Request & Mentenanță](#pull-request--mentenanță)

---

## Descriere aplicație

Această aplicație web este dedicată serialului „The Blacklist” și oferă utilizatorilor o interfață simplă pentru a vizualiza:
- o descriere generală a serialului,
- personaje principale,
- trailere oficiale.

Aplicația este construită cu Flask și este modularizată astfel încât fiecare atribut (descriere, actori, trailere) este gestionat într-un fișier separat.

---

## Funcționalități & Versiuni

* **v1.0** – versiune funcțională cu:
  * pagină principală `/`
  * pagină cu descriere `/descriere`
  * pagină cu personaje `/actori`
  * pagină cu trailere `/trailer`
  * integrare Jenkins + Docker + Pytest + Pylint

---

## Tehnologii folosite

* **Python 3.10** & **Flask** – backend web
* **HTML/CSS** – afișare interfețe
* **Jinja2** – motor de template-uri
* **Pytest** – testare automată
* **Pylint** – analiză statică
* **Docker** – containerizare
* **Jenkins** – CI/CD pipeline

---

## Configurare & Instalare

1. **Clone repo & branch**:

```bash
git clone https://github.com/larisa-mortoiu/curs_vcgj_2025_filme.git
cd curs_vcgj_2025_filme
git checkout dev_Ichim_Ionut
```
2. **Rulare directă** (fără venv):
 ```bash
 python3 filme.py
 ```
3. **Rulare cu venv**:
```bash
source activeazavenv
python3 filme.py
```

Acces aplicație: [http://localhost:5077](http://localhost:5077)

---


## Prezentare interfață web

### 1. Homepage
![Homepage](https://github.com/larisa-mortoiu/curs_vcgj_2025_filme/blob/main_Ichim_Ionut/static/images/home_page.png)

### 2. Actori
![Characters](https://github.com/larisa-mortoiu/curs_vcgj_2025_filme/blob/main_Ichim_Ionut/static/images/actori.png)

### 3. Trailers
![Trailers](https://github.com/larisa-mortoiu/curs_vcgj_2025_filme/blob/main_Ichim_Ionut/static/images/trailer.png)

### 4. Descriere
![Trailers](https://github.com/larisa-mortoiu/curs_vcgj_2025_filme/blob/main_Ichim_Ionut/static/images/descriere.png)

---

## Testare cu Pytest

Testele validează:
- codul 200 pentru fiecare rută
- verificea pozelor de pe pagina actori

```bash
python3 -m pytest app/tests/ -q
```
![image](https://github.com/larisa-mortoiu/curs_vcgj_2025_filme/blob/main_Ichim_Ionut/static/images/pytest.png)
---

## Analiză statică cu Pylint

```bash
PYTHONPATH=. pylint --exit-zero app/tests/test_filme.py
PYTHONPATH=. pylint --exit-zero filme.py
```

Se folosește `--exit-zero` în Jenkins pentru a nu întrerupe pipeline-ul la warning-uri.
![image](https://github.com/larisa-mortoiu/curs_vcgj_2025_filme/blob/main_Ichim_Ionut/static/images/pylint.png)
---

## Containerizare cu Docker

```bash
docker build -t theblacklist-app .
docker run -p 5077:5077 theblacklist-app
```

Aplicația devine accesibilă la: [http://localhost:5077](http://localhost:5077)

---

## Pipeline CI/CD cu Jenkins

Pipeline-ul include pașii:

1. Build
2. Analiză statică cu Pylint
3. Testare unitară cu Pytest
4. Deploy: Pornire container local (`tneblacklist-container`)


Exemplu rulare cu succes:
![Pipeline](https://github.com/larisa-mortoiu/curs_vcgj_2025_filme/blob/main_Ichim_Ionut/static/images/pipeline.png)

---

## Pull Request & Mentenanță

* Dezvoltarea se face pe branch `dev_Ichim_Ionut`
* Se deschide PR către `main_Ichim_Ionut`
* După review și succes pipeline, se face merge și build automat pe `main`

---
