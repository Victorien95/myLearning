import os.path
import pickle

titre = "BIENVENU SUR ROBOC"
roboc = titre.center(150, "=")
roboct_reglement = "\nREGLEMENT DE ROBOC:" \
                  "\n\nROBOC est un jeu de labyrinthe. Votre personnage est représenté par un 'X'." \
                  "\nLes murs du labyrinthe sont représentés par des 'O'" \
                  "\nLes '.' représentes des portes. " \
                  "Si vous passez une porte votre personnage avance d'une case en plus" \
                  "(il ne s'arrete pas au niveau de la porte)" \
                  "\nLa sortie est représentée par un 'U'. " \
                  "\nPour gagner votre personnage doit donc retrouver la porte." \
                  "\nPour vous déplacer, utilisez les touches directionnelles: " \
                  "\nN pour le nord \nS pour le sud \nE pour l'est \nO pour l'ouest" \
                  "\nVous pouvez rajouter un nombre alpha numérique à la suite de votre direction " \
                  "afin de vous déplacer plus vite." \
                  "\n\nAfin de rendre le jeu plus agréable vous pouvez rajouter un nombre " \
                  "supérieur aux limites du Labyrinthe" \
                  "\nRoboc s'occupera de déplacer votre personnage " \
                  "du maximum de cases possibles  en fonction du nombre" \
                  "\n\nNous vous souhaitons une agréable partie !"


def robot_reglement():
    """Affichage du bandeau ROBOC et du réglement"""
    print(roboc)
    print(roboct_reglement)


def connection():
    """Fonction pour connecter le joueur"""
    # Si le fichier de compte est inexistant on le crée et on ajoute le compte du joueur
    if not os.path.isfile("fichier_des_comptes"):
        liste_comptes = []
        compte_du_joueur = list()
        compte_du_joueur.append(input("\nNous n'avons trouvé aucun comptes."
                                      "\n\nVeuillez taper votre login"))
        compte_du_joueur.append(input("\nBonjour {} \nTapez votre mot de passe".format(compte_du_joueur[0].upper())))
        compte_du_joueur.append(None)
        liste_comptes.append(compte_du_joueur)
        with open("fichier_des_comptes", "wb") as initialisation_compte:
            mon_pickler = pickle.Pickler(initialisation_compte)
            mon_pickler.dump(liste_comptes)
        return compte_du_joueur
    else:
        # Si le fichier est existant on cherche le compte du joueur sinon on crée un nouveau compte
        with open("fichier_des_comptes", "rb") as lecture_compte:
            mon_unpickle = pickle.Unpickler(lecture_compte)
            liste_comptes = mon_unpickle.load()
        login = input("\nDes comptes joueurs on étés trouvés... \n\nTapez votre login:")
        i = 0
        long = len(liste_comptes)
        while i < long:
            compte = liste_comptes[i]
            if login == compte[0]:
                mdp = input("\nBonjour {}! \n\nTapez votre mot de passe".format(login.upper()))
                if mdp == compte[1]:
                    return compte
                else:
                    i = 0
                    decompte = 3
                    while mdp != compte[1]:
                        aff_decompte = decompte - i
                        mdp = input("\n\nMauvais mot de passe, veuillez resaisir. ({} essais)".format(aff_decompte))
                        i += 1
                        if i == 3:
                            print("\nReinitialisation")
                            return False
                    else:
                        return compte
            else:
                i += 1
        else:
            # Creation du compte si aucun compte na été trouvé
            compte_du_joueur = list()
            compte_du_joueur.append(login)
            print("\nVotre compte n'a pas été trouvé {}"
                  "\n\nCréation de votre compte...".format(login.upper()))
            mdp = input("\n\nTapez votre mot de passe".format(login.upper()))
            compte_du_joueur.append(mdp)
            compte_du_joueur.append(None)
            liste_comptes.append(compte_du_joueur)
            with open("fichier_des_comptes", "wb") as ajout_de_compte:
                mon_pickler = pickle.Pickler(ajout_de_compte)
                mon_pickler.dump(liste_comptes)
            return compte_du_joueur


def boucle_connection():
    """Permet de reinitialiser la connection si trop de mauvais mot de passe"""
    connect = connection()
    while connect is False:
        connect = connection()
    else:
        return connect


def reinitialisation_carte(compte_joueur):
    """ Fonction permettant de réinitialiser la carte
    si le joueur ne souhaite pas continuer la partie en cours"""

    if compte_joueur[2] is not None:
        continuer_la_partie = input("\nUne partie est déjà en cours sur votre compte {}"
                                    "\n\n-> Si vous souhaitez continuer: tapez 1"
                                    "\n-> Pour redémarrer une nouvelle partie: "
                                    "tapez 2".format(compte_joueur[0].upper()))
        while len(continuer_la_partie) == 0 or continuer_la_partie not in "12" or len(continuer_la_partie) > 1:
            continuer_la_partie = input("\n\nTapez 1 pour continuer ou 2 pour une nouvelle partie svp")
        else:
            if continuer_la_partie == "2":
                compte_joueur[2] = None
                return continuer_la_partie
            else:
                return continuer_la_partie


def enregistrement(compte_joueur, carte, index):
    """Enregistrement de la carte à chaque déplacement du joueur.
    Trouve le compte du joueur dans le fichier des comptes et enregistre le compte
    avec la nouvelle carte après déplacement"""
    compte_joueur[2] = carte
    with open("fichier_des_comptes", "rb") as lec_compte:
        mon_unpickle = pickle.Unpickler(lec_compte)
        comptes = mon_unpickle.load()
    comptes[index] = compte_joueur
    with open("fichier_des_comptes", "wb") as enr_compte:
        mon_pickler = pickle.Pickler(enr_compte)
        mon_pickler.dump(comptes)


def enregistrement_fin_partie(compte_joueur, index):
    """Fonction enregistrement pour la fin de partie car au lieu d'enregistrer la carte, renvoie None
    pour que le joueur recommence une partie avec la fonction 'jeu()' en boucle infini."""
    compte_joueur[2] = None
    with open("fichier_des_comptes", "rb") as lec_compte:
        mon_unpickle = pickle.Unpickler(lec_compte)
        comptes = mon_unpickle.load()
    comptes[index] = compte_joueur
    with open("fichier_des_comptes", "wb") as enr_compte:
        mon_pickler = pickle.Pickler(enr_compte)
        mon_pickler.dump(comptes)


def quitter_laby(variable, compte_joueur, index):
    if inpute == 'q' or inpute == 'Q':
        confirmation = input("Voulez vous vraiment quitter la partie ?"
                            "\n -> Tapez 1 pour OUI"
                            "\n -> Tapez 2 pour NON")
        while len(confirmation) == 0 or confirmation not in "12":
            confirmation = input("1 ou 2 seulement svp...")
        else:
            if confirmation == '2':
                pass
            else:
                print("\n\nTrès bien, votre partie est enregistrée ! \n\nA très bientôt sur ROBOC !!")
                sys.exit()


def index_compte(compte_joueur):
    """Permet de trouver l'index des comptes pour permettre l'enregistrement dans les fonctions 'enregistrement()"""
    with open("fichier_des_comptes", "rb") as lec_compte:
        mon_unpickle = pickle.Unpickler(lec_compte)
        comptes = mon_unpickle.load()
    for i in range(len(comptes)):
        if comptes[i][0] == compte_joueur[0]:
            if comptes[i][1] == compte_joueur[1]:
                return comptes.index(comptes[i])
        else:
            continue
