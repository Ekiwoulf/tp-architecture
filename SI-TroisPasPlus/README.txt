======================HOW TO USE======================
====Première étape : Avoir un environnement python====

Afin de pouvoir faire tourner en local notre programme, il est nécessaire d'avoir un environnement python. Pour ce faire nous utilisons virtualenv.
1) Installer Virtualenv
	- sudo apt-get install python-virtualenv

2) Configurer, utiliser et activer Virtualenv
	- mkdir ~/virtualenvironment
	- virtualenv ~/virtualenvironment/venv
	- cd ~/virtualenvironment/venv/bin
	- source activate

3) Installer les dépendances dont on a besoin
	- pip install -r requirement.txt
	
===========Deuxième étape : Setup database============

Utiliser la commande python :
	- python InitDB.py
	
=======Troisième étape : Lancer l'application=========

Utiliser la commande python :
	- python main.py

======Quatrième étape : Se conner à l'application=====

Pour vous connecter, utilisez votre mail de l'esiea :
	mail : prof@et.esiea.fr
	password : password

Sachant que l'API est un environement de test, nous avons mis à disposition uniquement 3 vols.