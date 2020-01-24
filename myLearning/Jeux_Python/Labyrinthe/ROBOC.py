import log
import Labyrinthe

log.robot_reglement()

compte_joueur = log.boucle_connection()

Labyrinthe.jeu(compte_joueur)

Labyrinthe.rejouer(compte_joueur)
