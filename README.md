# Breaking Bad Web App
===================================

## Cuprins
1. [Descriere aplicație](#descriere-aplicație)
2. [Descriere versiune](#descriere-versiune)
   1. [Probleme cunoscute](#probleme-cunoscute)
3. [Configurare](#configurare)
4. [Exemple pagină web](#exemple-pagină-web)
5. [Testare cu pytest](#testare-cu-pytest)
6. [Verificare statică cu pylint](#verificare-statică-cu-pylint)
7. [DevOps CI](#devops-ci)
   1. [Executare pipeline Jenkins](#executare-pipeline-jenkins)


---

## Descriere aplicație

Această aplicație web oferă o interfață vizuală pentru serialul Breaking Bad. Este construită cu ajutorul framework-ului Flask și include pagini cu:

- descriere generală a serialului
- listă de personaje principale
- trailere oficiale

Structura aplicației este modulară, codul fiind organizat în:
- `filme.py`: aplicația Flask principală
- `app/lib`: module logice pentru afișarea atributelor
- `app/tests`: teste unitare pentru atribute

Aplicația include suport pentru rulare în container Docker și integrare continuă în Jenkins.

---

## Descriere versiune

### Versiunea: `v1.0`

- Pagina principală la `http://localhost:5011/`
- Rute implementate:
  - `/` – homepage
  - `/breaking-bad` – descriere
  - `/breaking-bad/characters` – personaje
  - `/breaking-bad/trailers` – trailere

### Probleme cunoscute

- Codul HTML este simplificat și nu include protecție CSRF.
- Lipsesc validări avansate pentru rute inexistente (ex: 404 custom).

---

## Configurare

### Activare venv

```bash
source activeaza_venv
```

Dacă nu există `.venv`, scriptul `activeaza_venv_jenkins` îl creează și instalează dependințele.

### Rulare aplicație

```bash
./ruleaza_aplicatia
```

Acces în browser: [http://localhost:5011](http://localhost:5011)

---

## Exemple pagină web

- Homepage: imagine Breaking Bad
- Characters: imagini + descrieri pentru Walter, Jesse, Skyler etc.
- Trailers: iframe IMDb embed pentru fiecare sezon

---

## Testare cu pytest

Aplicația include 4 teste:
- verifică dacă rutele returnează 200 OK
- verifică structura atributului `trailers`

Comandă:
```bash
pytest
```

---

## Verificare statică cu pylint

Se rulează `pylint` pe:
- `filme.py`
- `app/lib/*.py`
- `app/tests/*.py`

Comandă:
```bash
pylint app/lib/*.py app/tests/*.py filme.py
```

Rezultatele nu opresc pipeline-ul (folosim `--exit-zero`).

---

## DevOps CI

Aplicația include un `Jenkinsfile` care:

- clonează repo-ul
- activează venv-ul
- rulează `pytest` și `pylint`
- build-uiește imaginea Docker
- rulează aplicația în container (`breakingbad-container`)

### Executare pipeline Jenkins

Exemplu rulare reușită:
Containerul rulează pe `localhost:5011`.

---

