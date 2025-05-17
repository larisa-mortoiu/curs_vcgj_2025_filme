# Mirica Elena
Această aplicație web a fost creată în cadrul cursului SCC și permite gestionarea unei colecții de filme/seriale, oferind funcționalități de bază. 
Se urmărește punerea în practică a noțiunilor esențiale învățate în cadrul disciplinei, de dezvoltare web, testare automată și integrare continuă.

Operațiile aplicației sunt gestionate prin rute bine definite în Flask. Docker a fost folosit pentru a crea un mediu de rulare consistent  indiferent de sistemul folosit. Jenkins a avut rolul de a automatiza testarea și integrarea continuă.

Pentru exemplificare, a fost prezentat serialul Bridgerton, realizat de Netflix.

## Tehnologii utilizate

- Python 3.10+
- Flask
- HTML/CSS
- Pytest
- Docker
- Jenkins

## Setup

A fost creat un director pe mașina virtuală  locală (Ubuntu 22.04) pentru dezvoltarea proiectului. Fișierele au fost editate în Visual Studio Code, descă rcat de pe pagina lor oficială (https://code.visualstudio.com/?wt.mc_id=vscom_downloads).


## Aducerea proiectului de pe server-ul git, pe cel local
 ```bash
git clone https://github.com/larisa-mortoiu/curs_vcgj_2025_filme.git
cd curs_vcgj_2025_filme
git checkout dev_Mirica_Elena
