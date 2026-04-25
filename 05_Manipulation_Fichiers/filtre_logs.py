#Parcourt un fichier d'historique ligne par ligne et n'affiche que les alertes de sécurité.


try :
    with open ("historique.txt", "r") as fichier:
        
        for ligne in fichier:
            # On cherche le mot-clé dans la ligne actuelle
            if "Alerte" in ligne:
                # On affiche la ligne (le .strip() nettoie les sauts de ligne invisibles)
                print(f" {ligne.strip()}")
except FileNotFoundError:
    print("Erreur : Le fichier d'historique n'a pas été trouvé.")
    
