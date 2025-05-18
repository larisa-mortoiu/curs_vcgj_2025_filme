![image](https://github.com/user-attachments/assets/60a7dc69-a83d-4f4a-844d-3b783dc325f8)Proiect SCC - Containerizare și CI/CD

Autor: Simion Razvan-Marian

Branch: dev_Simion_Razvan

Repo: https://github.com/larisa-mortoiu/curs_vcgj_2025_filme.git

Ce am implementat:

	Am dezvoltat o aplicație web în Flask, dedicată gestionării filmelor (proiectul Projet_SCC), care conține:
	* o pagină principală cu titlul serialului și trailer-ul;
	* o pagină cu actorii principali;
	* o pagină cu descrierea serialului;
	* stil personalizat CSS cu temă adaptată și butoane interactive;
	* structură modulară templates/, static/, și filme.py.

	Aplicația a fost containerizată cu Docker și testată automat prin Jenkins.

Cum am testat:

	Am folosit:

	* rulare locală cu python3 filme.py
	* build și rulare în container Docker (docker build, docker run)
	* integrare continuă cu Jenkins (pull din GitHub, build, run)
	* comanda docker ps pentru a verifica starea containerului
	* accesarea aplicației în browser la http://localhost:5000
	
	

	Pytest:
![Pytest](https://github.com/user-attachments/assets/fb53242b-b6f2-4d26-b96c-3c3584b29511)

🐳 Cum am rulat în container (Docker)

	Comenzi folosite:

	* docker build -t mechanicressurection .
	* run -p 5000:5000 mechanicressurection

	Aplicația devine accesibilă în browser la:
	http://localhost:5000
 
![Docker](https://github.com/user-attachments/assets/01135ec9-8c47-4ef3-9d3d-e7d64e906136)




🔧 Jenkins: configurare și rulare automată

	Job creat în Jenkins: MechanicRessurection-Pipeline

	Configurat ca Pipeline script from SCM

	Repo: https://github.com/larisa-mortoiu/curs_vcgj_2025_filme.git
	Branch: dev_Simion_Razvan
	Script path: Jenkinsfile

![Jenkins](https://github.com/user-attachments/assets/861010db-8296-4238-a6b2-413bd96bb096)
