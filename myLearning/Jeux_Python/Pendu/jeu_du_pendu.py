import pendu_fonctions
import time
import pickle

# Appel de la fonction connection pour avoir le compte du joueur
compte_du_joueur = pendu_fonctions.connection()
i = 1
# Création d'une variable pour afficher le nom du joueur en majuscule
compte_upper = compte_du_joueur["login"]

print("\nAtteignez 5 points pour débloquer le niveau intermédiaire et 10 points pour débloquer le mode difficile")
time.sleep(3)
print("\nBonne chance !")
var_tampon = 0
score_partie = compte_du_joueur["score"]

while i == 1:
    # On propose difficulté supérieur si le score est supérieur à 5
    if score_partie > 5 and score_partie <= 10:
        niveau = input("Bravo {} vous avez débloqué le niveau de difficulté suivant "
                       "\nTapez 1 pour continuer en facile "
                       "\nTapez 2 pour passer en mode intermédiaire".format(compte_upper.upper()))
        # Boucle pour obliger 1 ou 2
        while len(niveau) > 1 or niveau != '1' and niveau != '2':
            niveau = input("\nDésolé vous avez du faire une erreur..."
                           "\nTapez 1 pour continuer en facile "
                           "\nTapez 2 pour passer en mode intermédiaire".format(compte_upper.upper()))
        else:
            niveau = int(niveau)
            pendu_fonctions.niveau = niveau
    # On propose difficulté supérieur si le score est supérieur à 10
    if score_partie > 10:
        niveau = input("Vous êtes vraiment fort {} vous avez débloqué le dernier niveau de difficulté !"
                       "\nTapez 1 pour continuer en facile "
                       "\nTapez 2 pour passer en mode intermédiaire"
                       "\nTapez 3 pour passer en mode difficile".format(compte_upper.upper()))
        # Boucle pour obliger 1, 2 ou 3
        while len(niveau) > 1 or niveau != '1' and niveau != '2' and niveau != '3':
            niveau = input("\nDésolé {} vous avez du faire une erreur..."
                           "\nTapez 1 pour continuer en facile "
                           "\nTapez 2 pour passer en mode intermédiaire"
                           "\nTapez 3 pour passer en mode difficile".format(compte_upper.upper()))
        # niveau de la foncion niveau du pendu qui va creer des mots plus grand
        else:
            niveau = int(niveau)
            pendu_fonctions.niveau = niveau
    # Variables pour afficher les scores
    var = pendu_fonctions.essai_pendu()
    var_tampon += var
    score_partie = compte_du_joueur["score"] + var_tampon
    print("{} vous avez un score de {} points".format(compte_upper.upper(), score_partie))
    i = input("\npour continuer tapez 1 sinon tapez 2")
    # Boucle pour obliger 1 ou 2 pour quitter
    while len(i) > 1 or i != '1' and i != '2':
        i = input("\npour continuer tapez 1 sinon tapez 2 seulement svp")
    if i == '1':
        print("Ok c'est reparti")
        i = int(i)
    if i == '2':
        i = int(i)
else:
#Enregistrement du compte avec le nouveau score si le joueur quitte la partie
    print("\n{} vous terminez la partie avec un score de "
          "{} points".format(compte_upper.upper(), score_partie))
    print("\nVeuillez patienter, nous enregistrons votre score", compte_upper.upper())
    with open("fichier_des_comptes", "rb") as lecture:
        mon_unpickle = pickle.Unpickler(lecture)
        chargement = mon_unpickle.load()
        for n in range(len(chargement)):
            if compte_du_joueur == chargement[n]:
                break

    compte_du_joueur["score"] += var_tampon
    chargement[n] = compte_du_joueur

    with open("fichier_des_comptes", "wb") as ecriture:
        mon_pickler = pickle.Pickler(ecriture)
        mon_pickler.dump(chargement)
    time.sleep(4)
    print("\nDonnées enregistrées aves succès !")
    print("\n A bientôt {}".format(compte_upper.upper()))
