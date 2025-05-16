# Dina-Nitoi Maria-Alexandra

# CUPRINS
1. [Prezentarea generala a aplicatiei](#prezentarea-generala-a-aplicatiei)  
2. [Versiuni si functionalitati disponibile](#versiuni-si-functionalitati-disponibile)  
3. [Tehnologii utilizate](#tehnologii-utilizate)  
4. [Structura proiectului](#structura-proiectului)  
5. [Instructiuni de instalare si configurare](#instructiuni-de-instalare-si-configurare)  
6. [Interfata web prezentare](#interfata-web-prezentare)  
7. [Testare Pytest](#testare-pytest)  
8. [Analiza statica a codului cu Pylint](#analiza-statica-a-codului-cu-pylint)  
9. [Containerizare cu Docker](#containerizare-cu-docker)  
10. [Pipeline cicd cu Jenkins](#pipeline-cicd-cu-jenkins)  
11. [Procedura Pull Request](#procedura-pull-request)  
12. [Bibliografie](#bibliografie)

#Prezentare generala a aplicatiei

Acest proiect web, intitulat „filme”, are ca scop prezentarea detaliată a unui film ales – The Prestige. Aplicația le oferă utilizatorilor acces rapid la informații esențiale despre film, precum descrierea tematică și distribuția principală, printr-o interfață intuitivă și responsivă. Din punct de vedere tehnic, aplicația este dezvoltată cu Flask și este rulată într-un mediu izolat folosind Docker, ceea ce asigură portabilitate și consistență între medii. Testele unitare sunt automatizate cu Pytest, iar verificarea calității codului este realizată prin Pylint. Întregul flux de dezvoltare – de la instalarea dependințelor, până la rularea testelor și containerizarea aplicației – este gestionat automat printr-un pipeline de integrare continuă configurat în Jenkins.


#Versiuni si functionalitati disponibile

v1.0 – Versiunea inițială stabilă

Afișarea informațiilor despre filmul The Prestige, selectat manual ca subiect principal al aplicației.

Pagini dedicate pentru:

 - Descrierea filmului – un rezumat detaliat care evidențiază tematica și atmosfera poveștii.

 - Distribuție – listă cu actorii principali, ilustrată vizual cu imagini și nume.

Navigare intuitivă între homepage și paginile detaliate, cu opțiuni de întoarcere.

Testare automată a funcționalităților prin Pytest.

Verificare statică a calității codului folosind Pylint.

Containerizare completă cu Docker, pentru rulare uniformă în medii diferite.

Integrare continuă cu Jenkins, care rulează automat:

- instalarea dependențelor

- testele unitare

- analiza codului

- build-ul imaginii Docker

#Tehnologii utilizate

- Python 3.11 – limbajul de programare utilizat pentru dezvoltarea aplicației.

- Flask – framework web ușor și flexibil, folosit pentru gestionarea rutelor și a logicii aplicației.

- HTML & CSS – pentru structura și stilizarea interfeței web.

- Pytest – pentru scrierea și rularea testelor unitare.

- Pylint – pentru analiza statică a codului și menținerea unui stil coerent.

- Docker – pentru containerizarea aplicației, oferind un mediu izolat și portabil.

- Jenkins – pentru integrare continuă: automatizează pașii de build, testare și analiză a codului.
