"""
Un gestionnaire interactif d'adresses IP utilisant un dictionnaire pour un accès instantané aux données.
"""

# Initialisation de notre base de données 
inventaire = {
    "Routeur": "192.168.1.1",
    "Serveur_Web": "10.0.0.5"
}



while True:
    nom = input("\nQuel serveur cherchez-vous ? (ou tapez 'quitter') : ")
    
    if nom.lower() == "quitter":
        print("Fermeture de l'inventaire.")
        break
        
    # On vérifie si la clé existe dans le dictionnaire
    if nom in inventaire:
        # Si oui on affiche la valeur associée
        print(f" Le serveur '{nom}' est à l'adresse IP : {inventaire[nom]}")
        
    else:
        print(f" Le serveur '{nom}' est inconnu.")
        # On demande la nouvelle donnée
        nouvelle_ip = input(f"Quelle est l'IP de ce nouveau serveur '{nom}' ? ")
        
        #  on crée la nouvelle paire 
        inventaire[nom] = nouvelle_ip
        
        print(f" Inventaire mis à jour  {nom}  {inventaire[nom]}")
