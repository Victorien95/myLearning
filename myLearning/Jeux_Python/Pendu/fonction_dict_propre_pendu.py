import pickle

# ouvre le dictionnaire et le lit ligne par ligne ajoute chaque ligne à la liste du nouveau dictionnaire

with open("dico", 'r') as lecture_dico:
    dico_liste = []
    line = lecture_dico.readline()
    while line:
        dico_liste.append(line)
        line = lecture_dico.readline()

# supprime les \n de chaque mots

for i in range(len(dico_liste)):
    dico_liste[i] = dico_liste[i].rstrip('\n')

# on enregiste le nouveau dico en binaire

with open("dico_bon", 'wb') as fichier_dico_bon:
    mon_pickler = pickle.Pickler(fichier_dico_bon)
    mon_pickler.dump(dico_liste)
