"""

Un lecteur sécurisé qui extrait et affiche le contenu d'un fichier d'historique, sans planter si le fichier est absent.
"""

while True:
    try:
        # Ouverture en mode "r" (read)
        with open("historique.txt", "r", encoding="utf-8") as fichier:
            contenu = fichier.read()
            
            print("DÉBUT DE L'HISTORIQUE")
            print(contenu)
            print(" FIN DE L'HISTORIQUE")
            
            break # On sort de la boucle si la lecture a réussi
            
    except FileNotFoundError:
        print("Erreur : Le fichier d'historique est introuvable ou a été supprimé.")
        # On casse la boucle pour éviter un affichage infini de l'erreur 
        break
