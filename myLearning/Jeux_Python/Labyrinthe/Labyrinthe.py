import log
import random
import sys


def niveau_difficulte_fonction():
    """Fonction permettant de choisir le niveau de difficultée. Choix aléatoire en ouvrant le fichier des cartes."""
    carte_choice = None
    niveau = input("\nChoisissez votre niveau de difficulté:"
                   "\nTapez 1 pour jouer en mode Facile"
                   "\nTapez 2 pour joueur en mode Difficile\n")
    while len(niveau) == 0 or len(niveau) > 1:
        niveau = input("\nNous n'avons pas compris votre choix..."
                       "\nTapez 1 ou 2 seulement svp...")
    while len(niveau) == 0 or niveau not in "12":
        niveau = input("\nTapez 1 ou 2 seulement svp...")
    if niveau == "1":
        carte_choice = random_carte_facile()
    if niveau == "2":
        carte_choice = random_carte_prison()
    return carte_choice


def random_carte_facile():
    """Choix aléatoire d'une carte facile"""
    carte_liste = []
    choix = str()
    lecture_ligne = open('dcartes/cartes_f.txt', 'U')
    for lignes in lecture_ligne:
        carte_liste.append(lignes.replace('\n', ''))
        choix = random.choice(carte_liste)
    lecture_ligne.close()
    return choix


def random_carte_prison():
    """Choix aléatoire d'une carte difficile"""
    carte_liste = []
    choix = str()
    lecture_ligne = open('dcartes/cartes_p.txt', 'r')
    for lignes in lecture_ligne:
        carte_liste.append(lignes.replace('\n', ''))
        choix = random.choice(carte_liste)
    lecture_ligne.close()
    return choix


def choix_et_carte_to_liste():
    """Focntion permettant de savoir combien de ligne contient la carte afin de créer une liste de la carte peut
    importe la taille des cartes à charger. La fonction ouvre le fichier appelé
    dans la fonction 'niveau_difficilte_fonction().
    -> Lecture des lignes et ajout des charactères dans des listes de liste. Renvoie la liste de la carte.
    """
    liste_de_la_carte = []
    lecture_lignes = open(niveau_difficulte_fonction(), "r")
    for lignes in lecture_lignes:
        liste_de_la_carte.append(list(lignes))
    lecture_lignes.close()
    return liste_de_la_carte


def valeurs_de_deplacement():
    """Fonction permettant de stocker le déplacement du joueur sous forme de liste.

    On oblige le joueur a entrer une direction et ensuite un nombre de cases.
    (Le nombre de cases est infini pour ne pas avoir à compter le nombre de deplacement à chaque fois.
    Le deplacement s'arretera tout seul en cas de rencontre avec un obstacle)

    On renvoi la direction et la valeur du déplacement ."""
    deplacement = input("\nDans quelle direction se deplacer ?"
                        "\nTapez:"
                        "\nN pour le nord, \nS pour le sud, \nO pour l'ouest, \nE pour l'est."
                        
                        "\n\nAstuce: Vous pouvez ajouter un numero pour vous deplacer plus vite")

    # Boucle permettant de vérifier que le joueur rentre bien une direction et ensuite un nombre de cases.
    while len(deplacement) == 0 or deplacement[0] not in "noseqNOSEQ" or deplacement[1:] not in "0123456789":
        deplacement = input("\nRetapez s'il vous plaît, format: Direction + nombres de cases")
    else:
        return deplacement


def num_deplacement(deplacement):
    """Permet de charger le deplacement en chiffre numérique pour les différents déplacement NOSE.
    Passe du str ou int pour calculer le déplacement en éliminant la lettre de déplacement
    et renvoi 1 si seulement une lettre.
    """
    if len(deplacement) > 1:
        numero = deplacement[1:]
        numero = int(numero)
    else:
        numero = 1
    return numero


def quitter_laby(compte_joueur, carte, index):
    confirmation = input("Voulez vous vraiment quitter la partie ?"
                        "\n -> Tapez 1 pour OUI"
                        "\n -> Tapez 2 pour NON")
    while len(confirmation) == 0 or confirmation not in "12":
        confirmation = input("1 ou 2 seulement svp...")
    else:
        if confirmation == '2':
            pass
        else:
            log.enregistrement(compte_joueur, carte, index)
            print("\n\nTrès bien, votre partie est enregistrée ! \n\nA très bientôt sur ROBOC !!")
            sys.exit()


def trouver_x(carte):
    """ Permet de trouver l'emplacement de X sur la carte. Renvoi l'index de X
    (permet aussi l'ajout de nouvelle carte peut importe la postion du X).
    """
    ligne = 0
    colonne = 0
    for i in range(len(carte)):
        for k in range(len(carte[i])):
            if carte[i][k] == "X":
                ligne = i
                colonne = k
    return ligne, colonne


def affichage_carte(carte):
    """Fonction permettant de passer de la carte en liste à la carte en string et de l'afficher."""
    tampon = str()
    long = len(carte)
    i = 0
    while i < long:
        for l in range(len(carte[i])):
            tampon += carte[i][l]
        i += 1
    print(tampon)
    return tampon


def nose(deplacement, carte, compte_joueur, index):
    """Fonction de déplacement nord sud est ou ouest + return True si la partie est gagné
    (voir fonction fin de partie).
    """
    # Quitter la partie
    if deplacement[0] in "qQ":
        quitter_laby(compte_joueur, carte, index)
    # Déplacement vers le Nord
    if deplacement[0] in "nN":
        a = num_deplacement(deplacement)
        b = trouver_x(carte)
        nord = b[0]
        k = 1
        while k <= a:
            if carte[nord - k][b[1]] != "O":
                carte[nord][b[1]] = " "
                if carte[nord - k][b[1]] == ".":
                    k += 1
                if carte[nord - k][b[1]] == "U":
                    print("\nBRAVO VOUS AVEZ GAGNE !!")
                    log.enregistrement_fin_partie(compte_joueur, index)
                    return True
                k += 1
            else:
                carte[nord - k + 1][b[1]] = "X"
                print("\nMouvement impossible")
                break
        else:
            carte[nord - k + 1][b[1]] = "X"
        affichage_carte(carte)
        log.enregistrement(compte_joueur, carte, index)

    # Déplacement vers le Sud
    if deplacement[0] in "sS":
        a = num_deplacement(deplacement)
        b = trouver_x(carte)
        sud = b[0]
        k = 1
        while k <= a:
            if carte[sud + k][b[1]] != "O":
                carte[sud][b[1]] = " "
                if carte[sud + k][b[1]] == ".":
                    k += 1
                if carte[sud + k][b[1]] == "U":
                    print("\nBRAVO VOUS AVEZ GAGNE !!")
                    log.enregistrement_fin_partie(compte_joueur, index)
                    return True
                k += 1
            else:
                carte[sud + k - 1][b[1]] = "X"
                print("\nMouvement impossible")
                break
        else:
            carte[sud + k - 1][b[1]] = "X"
        affichage_carte(carte)
        log.enregistrement(compte_joueur, carte, index)

# Déplacement vers l'est
    if deplacement[0] in "eE":
        a = num_deplacement(deplacement)
        b = trouver_x(carte)
        est = b[0]
        k = 1
        while k <= a:
            if carte[est][b[1]-k] != "O":
                carte[est][b[1]] = " "
                if carte[est][b[1]-k] == ".":
                    k += 1
                if carte[est][b[1]-k] == "U":
                    print("\nBRAVO VOUS AVEZ GAGNE !!")
                    log.enregistrement_fin_partie(compte_joueur, index)
                    return True
                k += 1
            else:
                carte[est][b[1]-k+1] = "X"
                print("\nMouvement impossible")
                break
        else:
            carte[est][b[1]-k + 1] = "X"
        affichage_carte(carte)
        log.enregistrement(compte_joueur, carte, index)

    # Déplacement vers l'Ouest
    if deplacement[0] in "oO":
        a = num_deplacement(deplacement)
        b = trouver_x(carte)
        est = b[0]
        k = 1
        while k <= a:
            if carte[est][b[1]+k] != "O":
                carte[est][b[1]] = " "
                if carte[est][b[1]+k] == ".":
                    k += 1
                if carte[est][b[1]+k] == "U":
                    print("\nBRAVO VOUS AVEZ GAGNE !!")
                    log.enregistrement_fin_partie(compte_joueur, index)
                    return True
                k += 1
            else:
                carte[est][b[1]+k-1] = "X"
                print("\nMouvement impossible")
                break
        else:
            carte[est][b[1]+k - 1] = "X"
        affichage_carte(carte)
        log.enregistrement(compte_joueur, carte, index)


def jeu(compte_joueur):
    """Fonction pour lancer le jeu. A besoin de compte_joueur dans le main pour fonctionner."""
    if compte_joueur[2] is None:
        carte = choix_et_carte_to_liste()
    else:
        reinitialisation = log.reinitialisation_carte(compte_joueur)
        if reinitialisation == "2":
            carte = choix_et_carte_to_liste()
        else:
            carte = compte_joueur[2]
    affichage_carte(carte)
    index = log.index_compte(compte_joueur)
    i = 0
    while i < 1:
        deplacement = valeurs_de_deplacement()
        victoire = nose(deplacement, carte, compte_joueur, index)
        if victoire is True:
            i += 1
        else:
            pass


def rejouer(compte_joueur):
    """Fonction rejouer qui appele la fonction 'jeu()' et boucle tant que rejoueur est égale à 1.
    A besoin de compte_joueur dans le main pour fonctionner."""
    r_joue = input("\nPour rejouer Tapez 1 sinon tapez 2")
    while len(r_joue) == 0 or r_joue not in "12" or len(r_joue) > 1:
        r_joue = input("\nTapez 1 ou 2 seulement...")
    else:
        pass

    while r_joue == "1":
        jeu(compte_joueur)
        r_joue = input("\nPour rejouer Tapez 1 sinon tapez 2")
        while len(r_joue) == 0 or r_joue not in "12" or len(r_joue) > 1:
            r_joue = input("\nTapez 1 ou 2 seulement...")
        else:
            continue
    else:
        print("\n\nPartie terminée.... A la prochaine !")