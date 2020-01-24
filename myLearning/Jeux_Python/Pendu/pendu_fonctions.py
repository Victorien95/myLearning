import random
import os.path
import pickle
import time


def connection():
    # On vérifie si le fichier de comptes joueurs existe si il n'existe pas on le créée et on ajoute le nouveau joueur
    # sinon on renvoi à la suite pour vérifier les comptes existant
    if not os.path.isfile("fichier_des_comptes"):
        print("\nFichier de comptes non trouvé nous allons creer votre compte veuillez patienter...")
        time.sleep(4)
        with open("fichier_des_comptes", 'wb') as fichier_des_comptes_ecriture:
            liste_des_comptes = []
            print("\nL'initialisation des comptes est prête ! ")
            compte_joueur_default = {"login": input("\nVeuillez tapez votre login"),
                                     "mdp": input("\nTapez votre mot de passe svp"),
                                     "score": 0}
            liste_des_comptes.append(compte_joueur_default)
            verification_compte_default = compte_joueur_default["login"]
            mon_pickle_comptes = pickle.Pickler(fichier_des_comptes_ecriture)
            mon_pickle_comptes.dump(liste_des_comptes)
            print("\nBienvenue {}".format(verification_compte_default.upper()))
            return compte_joueur_default
    else:
        print("\nDes comptes existant ont été trouvés")
# On ouvre le fichier de comptes joueurs + on demande le compte du joueur
    with open("fichier_des_comptes", 'rb') as fichier_des_comptes_ouverture:
        mon_unpickler_comptes = pickle.Unpickler(fichier_des_comptes_ouverture)
        ouverture_comptes = mon_unpickler_comptes.load()
        verification_compte = input("Qu'elle est votre compte ?")

        # Boucle pour vérifier si le compte est présent sinon création de compte +
        # enregistrement nouveau fichier et nouveau compte

        for i in range(len(ouverture_comptes)):
            dico_du_compte = ouverture_comptes[i]
            if verification_compte in dico_du_compte["login"]:
                break
        else:
            print("\nVotre compte n'existe pas, nous allons creer votre compte", verification_compte.upper())
            mdp = input("Tapez votre mot de passe")
            nouveau_compte = {"login": verification_compte, "mdp": mdp, "score": 0}
            compte_du_joueur = nouveau_compte
            print("\nBienvenue", verification_compte.upper(), "vous disposez de", nouveau_compte["score"],
                  "points pour le moment")
            ouverture_comptes.append(nouveau_compte)
            with open("fichier_des_comptes", "wb") as fichier_des_comptes_ecriture:
                mon_pickle_comptes = pickle.Pickler(fichier_des_comptes_ecriture)
                mon_pickle_comptes.dump(ouverture_comptes)
                return compte_du_joueur

        # Boucle pour logger le compte joueur si il existe
        for i in range(len(ouverture_comptes)):
            dico_du_compte = ouverture_comptes[i]
            if verification_compte in dico_du_compte["login"]:
                print("\nVotre compte a été trouvé")
                compte_du_joueur = ouverture_comptes[i]
                mdp = input("Tapez votre mot de passe")
                break
        if mdp in dico_du_compte["mdp"]:
            print("\nVous etes connecté", verification_compte.upper(),
                  "vous disposez de", dico_du_compte["score"], "point(s)")
            compte_du_joueur = ouverture_comptes[i]
            return compte_du_joueur
        if mdp not in compte_du_joueur["mdp"]:
            print("\nvotre mot de passe est incorrecte")
            for valeurss in compte_du_joueur["mdp"]:
                if mdp == compte_du_joueur["mdp"]:
                    print("\nVous etes connecté", verification_compte.upper(),
                          "vous disposez de", dico_du_compte["score"], "point(s)")
                    return compte_du_joueur
                if mdp != compte_du_joueur["mdp"]:
                    mdp = input("\nRetapez votre mdp svp si vous avez oubliez votre mot de passe tapez *")
                    if mdp == compte_du_joueur["mdp"]:
                        print("\nVous etes connecté", verification_compte.upper(),
                              "vous disposez de", dico_du_compte["score"], "point(s)")
                        compte_du_joueur = ouverture_comptes[i]
                        return compte_du_joueur
                    if mdp == "*":
                        print("\nRéinitialisation... ...   ...")
                        time.sleep(4)
                        return connection()


def le_choix_du_pendu():
    # On charge le dico
    with open('dico_bon', 'rb') as fichier_choix:
        mon_unpickle = pickle.Unpickler(fichier_choix)
        dico_recuperer = mon_unpickle.load()
    # on choisit un mot aléatoire dans la liste
    choix_du_pendu = random.choice(dico_recuperer)
    return choix_du_pendu


def mot_en_fonction_du_niveau(niveau):
    # on initialise la variable "mot" avec la fonction "le_choix_du_pendu"
    mot = le_choix_du_pendu()
    # on prend la longueur de mot dans la varibale "long"
    long = len(mot)
    # si le niveau est egale a 0 (facile) la longueur du mot sera inférieur à 5 lettres
    if niveau == 1:
        while long > 4:
            mot = le_choix_du_pendu()
            long = len(mot)
        else:
            return mot
    # si le niveau est egale a 1 (moyen)
    # la longueur du mot sera comprise entre 4 et 7 lettres
    if niveau == 2:
        while 5 < long > 7:
            mot = le_choix_du_pendu()
            long = len(mot)
        else:
            return mot
    # si le niveau est egale a 2 (difficile) la longueur du mot sera supérieur à 7 lettres
    if niveau == 3:
        while long < 8:
            mot = le_choix_du_pendu()
            long = len(mot)
        else:
            return mot




niveau = 1



def essai_pendu():
    liste_des_lettre_bonne = []
    liste_des_lettre_mauvaise = []
    point_de_la_partie = 0
    points_gagnes = 0
    if niveau == 1:
        print("\nVous jouer en mode facile... Chargement, veuillez patienter...")
        points_gagnes = 2
    if niveau == 2:
        print("\nVous jouez en mode intermediare... Chargement, veuillez patienter...")
        points_gagnes = 3
    if niveau == 3:
        print("\nVous jouez en mode difficile... Chargement, veuillez patienter...")
        points_gagnes = 5
    varibale_stock = mot_en_fonction_du_niveau(niveau)
    time.sleep(4)
    print("\nLe pendu à choisit son dernier mot... pourrez vous le devenier ? \nVous avez 11 coups")
    mot_tampon = '_ ' * len(varibale_stock)
    mot_tampon = mot_tampon.split(' ')
    del mot_tampon[-1]
    print(" ".join(mot_tampon))
    nombre_de_coup_a_jouer = 11
    while "_" in mot_tampon:
        print("\nLettre(s) déja tapez valide:", liste_des_lettre_bonne,
              "\nLettre(s) déjà tapez non valide", liste_des_lettre_mauvaise)
        lettre_choisit = input('\nTapez une lettre')
        while lettre_choisit not in 'AZERTYUIOPQSDFGHJKLMWXCVBNazertyuiopqsdfghjklmwxcvbn' or len(lettre_choisit) > 1:
            lettre_choisit = input('\nTapez une lettre seulement svp')
        lettre_choisit = str(lettre_choisit)
        while lettre_choisit in liste_des_lettre_bonne:
            lettre_choisit = input("\nVous avez déjà choisit cette lettre, veuillez en choisir une autre")
        if lettre_choisit in varibale_stock:
            for i in range(len(mot_tampon)):
                if lettre_choisit == varibale_stock[i]:
                    mot_tampon[i] = lettre_choisit.upper()
                    print("\nLa lettre que vous avez choisit est présente:\n", " ".join(mot_tampon))
                    liste_des_lettre_bonne.append(lettre_choisit)
        else:
            while lettre_choisit in liste_des_lettre_mauvaise:
                lettre_choisit = input("\nVous avez déjà choisit cette lettre, veuillez en choisir une autre")
            nombre_de_coup_a_jouer -= 1
            print("\nDésolé cette lettre ne fait pas partie du mot du pendu..."
                  "\nIl vous reste", nombre_de_coup_a_jouer, "coup(s)")
            liste_des_lettre_mauvaise.append(lettre_choisit)
            if nombre_de_coup_a_jouer == 0:
                point_de_la_partie -= points_gagnes
                print("\nVous avez perdu...! \nVous perdez", points_gagnes, "point(s)")
                print("\nLe mot du pendu était:\n", varibale_stock)
                return point_de_la_partie
    else:
        point_de_la_partie += points_gagnes
        print("\nVous avez gagner ! vous remportez", points_gagnes, "points")
    if point_de_la_partie < 0:
        print("\nDésolé c'est terminé pour vous")
    else:
        return point_de_la_partie