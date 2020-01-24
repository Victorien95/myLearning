import sys

def test():
    a = input("taper")
    while len(a) == 0 or a[0] not in "noseNOSE" or a[1:] not in "0123456789":
        a = input(("TAPE JE TAI DIT"))
    else:
        print(a)



def quitter_laby(inpute):
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

inpute = input("tapez")


quitter_laby(inpute)

print("jambon")