import random
import time

difficultés = 0 # initialisation
niveau = 0
compteur = 1
nombre_joueur = -1
légendaire = 0

while 1 > difficultés or difficultés > 4: # difficulté entre 1 et 4
    difficultés = input("""choisissez un niveau de difficultés 
    facile tapez 1 
    moyen tapez 2  
    difficile tapez 3
    légendaire tapez 4
    """)
    difficultés = int(difficultés)
    if difficultés == 1:
        niveau = 100
        print("""vous avez choisi le niveau facile
         le nombre est compris entre 0 et 100""")
    elif difficultés == 2:
        niveau = 1000
        print("""vous avez choisi le niveau moyen
         le nombre est compris entre 0 et 1000""")
    elif difficultés == 3:
        niveau = 10000
        print("""vous avez choisi le niveau difficile
        le nombre est compris entre 0 et 10000""")
    elif difficultés == 4:
        print("explications")
        while légendaire < 4 or légendaire > 10: #difficulté du légendaire
            légendaire = input("entrez votre nombre entre 5 et 9 inclus")
            légendaire = int(légendaire)
            niveau = 10**légendaire

    else:
        print("vous etes un mongole le jeu va prendre un certain temps")

nombre_alea = random.randint(0, niveau)
print("entrez un nombre")
temps0 = time.time()
while nombre_joueur != nombre_alea:
    nombre_joueur = input("")
    nombre_joueur = int(nombre_joueur)
    if nombre_joueur > nombre_alea:
        print("c'est moins")
        compteur +=1
    elif nombre_joueur < nombre_alea:
        print("c'est plus")
        compteur += 1
temps0 = time.time()- temps0
temps0 = int(temps0)
if temps0 > 60:
    temps0 = temps0//60
    temps1 = temps0 % 60
    print("c'est la win vous avez reussi en", compteur, "coup(s) et", temps0, "minute(s)", temps1, "seconde(s)")
else:
    print("c'est la win vous avez reussi en", compteur, "coup(s) et", temps0, "seconde(s)")

