"""
Système de log interactif. Il enregistre les événements  saisis par l'utilisateur dans un fichier texte(script basique).
"""

# Boucle infinie pour permettre d'enregistrer plusieurs événements à la suite
while True:
    variable = input("Quel événement voulez-vous enregistrer ? (ou tapez 'quitter') : ")
    
    # On convertit la saisie en minuscules pour que   'Quitter', 'QUITTER' etc... fonctionnent tous.
  
    if variable.lower() == "quitter":
        print("Fermeture du journal. À bientôt !")
        break
        
    
    # Le mode "a"  garantit qu'on ajoute à la suite sans écraser le passé.
    with open("historique.txt", "a", encoding="utf-8") as fichier:
        fichier.write(f"{variable}\n")
        
