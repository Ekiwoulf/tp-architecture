import sqlite3

conn = sqlite3.connect('database.db')
cursor = conn.cursor()


cursor.execute("""DROP TABLE IF EXISTS client""")
cursor.execute("""DROP TABLE IF EXISTS vol""")
cursor.execute("""DROP TABLE IF EXISTS reservation""")

cursor.execute("""CREATE TABLE IF NOT EXISTS client(
                   id INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE,
                   nom TEXT,
                   prenom TEXT,
                   civilite TEXT,
                   date_de_naissance TEXT,
                   adresse_mail TEXT,
                   password TEXT)
                   """)
cursor.execute("""CREATE TABLE IF NOT EXISTS vol(
                   id INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE,
                   id_avion TEXT,
                   date TEXT,
                   heure_départ TEXT,
                   heure_arrivée TEXT,
                   lieu_départ TEXT,
                   destination TEXT,
                   nb_places_disponibles TEXT,
                   prix FLOAT)
                   """)
cursor.execute("""CREATE TABLE IF NOT EXISTS reservation(
                   id INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE,
                   id_vol INTEGER,
                   id_client INTEGER,
                   date TEXT,
                   destination TEXT,
                   lieu_départ TEXT,
                   prix FLOAT)
                   """)

# Create some clients
cursor.execute("""
            INSERT INTO client(nom,prenom,civilite,date_de_naissance,adresse_mail,password) VALUES (?,?,?,?,?,?)""",
               ("DOUCET", "Simon", "Monsieur", "09/05/1995", "sdoucet@et.esiea.fr", "test"))
cursor.execute("""
            INSERT INTO client(nom,prenom,civilite,date_de_naissance,adresse_mail,password) VALUES (?,?,?,?,?,?)""",
               ("NEZAR", "Oussama", "Monsieur", "04/01/1998", "nezar@et.esiea.fr", "test"))
cursor.execute("""
            INSERT INTO client(nom,prenom,civilite,date_de_naissance,adresse_mail,password) VALUES (?,?,?,?,?,?)""",
               ("LESNE", "Alexandre", "Monsieur", "07/08/1998", "lesne@et.esiea.fr", "test"))
cursor.execute("""
            INSERT INTO client(nom,prenom,civilite,date_de_naissance,adresse_mail,password) VALUES (?,?,?,?,?,?)""",
               ("CISSE", "Aly-Bocar", "Monsieur", "00/00/0000", "prof@et.esiea.fr", "password"))

# Create some vols
cursor.execute("""INSERT INTO vol(id_avion,date,heure_départ,heure_arrivée,lieu_départ,destination,
                       nb_places_disponibles,prix) VALUES (?,?,?,?,?,?,?,?)""",
               ("789654", "12/12/2020", "12:50", "00:00", "Paris", "New-york", 350, 400.50))
cursor.execute("""INSERT INTO vol(id_avion,date,heure_départ,heure_arrivée,lieu_départ,destination,
                          nb_places_disponibles,prix) VALUES (?,?,?,?,?,?,?,?)""",
               ("789410", "30/12/2020", "02:50", "03:45", "Paris", "Brest", 150,233.58))
cursor.execute("""INSERT INTO vol(id_avion,date,heure_départ,heure_arrivée,lieu_départ,destination,
                          nb_places_disponibles,prix) VALUES (?,?,?,?,?,?,?,?)""",
               ("789789", "01/12/2020", "16:50", "17:50", "Paris", "Marseilles", 20,630.45))

# Create some reservations
cursor.execute("""INSERT INTO reservation(id_vol,id_client,date,destination,lieu_départ,prix) VALUES (?,?,?,?,?,?)""",
               ("1", 1,"12/12/2020","New-york", "Paris", 400.50))
cursor.execute("""INSERT INTO reservation(id_vol,id_client,date,destination,lieu_départ,prix) VALUES (?,?,?,?,?,?)""",
               ("1", 2,"12/12/2020","New-york", "Paris", 400.50))
cursor.execute("""INSERT INTO reservation(id_vol,id_client,date,destination,lieu_départ,prix) VALUES (?,?,?,?,?,?)""",
               ("1", 3,"12/12/2020","New-york", "Paris", 400.50))
conn.commit()
conn.close()
