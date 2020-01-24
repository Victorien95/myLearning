from math import ceil
from random import randrange
import time

compte = int(input("Bien le bonjour jeune joueur ! \nNous vous souhaitons la bienvenu au Z Casino "
                   "\navec quelle somme souhaitez vous entrer ?"))

if compte > int(1000):
    print("Ah ouai vous ne rigolez pas ! \nLa somme de votre compte s'élève désormais à", compte, "$")
elif compte < int(100):
    print("Lol petit joueur ! \nLa somme de votre compte s'élève désormais à", compte, "$")
else:
    print("Très bien ! \nLa somme de votre compte s'élève désormais à", compte, "$")


i = 1


while i == 1:
    mise = 0
    numéro = 0
    mise2 = 0
    while mise < 1:
        mise = int(input("Quelle est le montant de votre mise ?"))
        if mise < 1:
            mise = int(input("Quelle est le montant de votre mise ? \nLe montant doit être supérieur à 1 $?"))
        numéro = int(input("Sur quelle numéro voulez vous parier ?"))
        if numéro < 0:
            numéro = int(input("Sur quelle numéro voulez vous parier ? Entre 0 et 49 svp !"))
        elif numéro > 49:
            numéro = int(input("Sur quelle numéro voulez vous parier ? Entre 0 et 49 svp !"))
    else:
        print("Vous aves choisit de miser", mise, "$ sur le numéro", numéro)

    roulette = randrange(50)
    print("la roulette tourne...")
    time.sleep(3)
    print("...et elle tombe sur le numéro.......", roulette, "!!")

    if roulette == numéro:
        mise2 = ceil(mise * 3)
        print("vous aviez misez", mise, "$", "sur le numéro", numéro, "\nvous remportez donc la somme de", mise2, "$!!")
        compte = compte + mise2
        if compte >= 0:
            print("la somme de votre compte s'élève désormais à", compte,"$")
        else:
            print("vous êtes redevable de la somme de", compte*-1, "$")
    elif roulette % 2 == 0 and numéro % 2 == 0:
        mise2 = ceil(mise * (1 / 2))
        print("vous aviez misez", mise, "$", "sur le numéro", numéro, "\net c'est un chiffre pair vous remportez donc la somme de", mise2, "$")
        compte = compte + mise2
        if compte >= 0:
            print("la somme de votre compte s'élève désormais à", compte, "$")
        else:
            print("vous êtes redevable de la somme de", compte*-1, "$")
    elif roulette % 2 == 0 and numéro % 2 == 1:
        mise2 = ceil(mise * (1 / 2))
        print("vous aviez misez", mise, "$", "sur le numéro", numéro,
              "\net c'est un chiffre impair vous remportez donc la somme de", mise2, "$")
        compte = compte + mise2
        if compte >= 0:
            print("La somme de votre compte s'élève désormais à", compte, "$")
        else:
            print("vous êtes redevable de la somme de", compte*-1, "$")
    else:
        mise2 = mise - (mise*2)
        compte = compte + mise2
        if compte >= 0:
            print("Dommage vous avez perdu \nLa somme de votre compte s'élève désormais à", compte, "$")
        else:
            print("vous êtes redevable de la somme de", compte*-1, "$")

    i = int(input("Si vous voulez rejouer tapez 1 sinon Tapez 2"))
    if i == 1:
        print("Ok c'est reparti pour un tour")
    else:
        while i != 1:
            if i == 2:
                if compte >= 0:
                    print("Vous avez choisit d'arrêter vous repartez du Z casino avec la somme de", compte, "$")
                else:
                    print("Vous avez choisit d'arrêter vous repartez du Z casino \nVous êtes redevable de la somme de", compte*-1, "$")
                break
            if i == 1:
                print("ok c'est reparti pour un tour")
            else:
                print("Vous ne savez pas taper sur 1 ou 2 ? Allez réessayons !")
                i = int(input("Si vous voulez rejouer tapez 1 sinon Tapez 2"))

