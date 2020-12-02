# Design SI-TroisPasPlus

## Base de donées

	Dans notre base de données, nous avons dans un premier temps une table **Vols disponibles**, avec comme entrée:
	- ID vol <-
	- ID avion
	- Date
	- Heure de départ
	- Heure d'arrivée
	- Lieu départ
	- Destination
	- Nb places disponibles
	
	Ensuite nous avons une **Réservation**:
	- ID Réservation
	- ID vol <-
	- ID Client <-
	- Prix

	Et enfin une table **Client**:
	- ID Client <-
	- Nom
	- Prénom
	- Civilité
	- Date de naissance
	- Adresse mail
	- Password

## Language et techno

	Pour le language de programmation, nous avons choisi le Python, car c'est assez simple de mettre en oeuvre ce genre
d'API avec les librairies proposé (Flask, mysql ...).


## Organisation du code
	
	Nous aurons plusieurs parties:
	- Une page d'accueille, pour mettre le login du client, ou la création d'un nouveau compte.
	(Nous precisons que nous ne gerons pas la partie sécurité pour le stockage de mot de passe)
	- Ensuite lorsque le client est connécté, il peut voir les vols disponibles, reserver un vol, et voir ses réservations.
	- Si nous avons le temps :
		- Une option pour supprimer une reservation
		- Le vol aller-retour
		- Choix de siege (Donc ajout d'un table **avion**)
		