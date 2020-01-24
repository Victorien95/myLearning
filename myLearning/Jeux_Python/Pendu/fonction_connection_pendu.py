import os.path
import pickle


def connection():
    # On vérifie si le fichier de comptes joueurs existe si il n'existe pas on le créée et on ajoute le nouveau joueur
    # sinon on renvoi à la suite pour vérifier les comptes existant
    if not os.path.isfile("fichier_des_comptes"):
        print("\nFichier de comptes non trouvé nous allons creer votre compte veuillez patienter...")
        time.sleep(3)
        with open("fichier_des_comptes", 'wb') as fichier_des_comptes_ecriture:
            liste_des_comptes = []
            print("\nL'initialisation des comptes est prête ! ")
            compte_joueur_default = {"login": input(" Veuillez tapez votre login"), "mdp": input("tapez votre mot de passe"),
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
            print("\nBienvenue", verification_compte.upper(), "vous disposez de", dico_du_compte["score"],
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
                mdp = input("tapez votre mot de passe")
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
                        time.sleep(3)
                        return connection()