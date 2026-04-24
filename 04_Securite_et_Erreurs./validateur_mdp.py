"""
Simulateur de système de sécurité qui force 
l'utilisateur à choisir un mot de passe respectant des règles précises.
"""

def check_mdp(mot_de_passe):
     On exige strictement plus de 8 caractères.
    if len(mot_de_passe) <= 8:
        # On déclenche intentionnellement une erreur pour que le programme principal la détecte et la gère.
        
        raise ValueError("Le mot de passe est trop court (min. 9 caractères).")

# Boucle infinie pour forcer la saisie tant que la règle n'est pas respectée
while True:
     mot_de_passe = input("Veuillez entrer un mot de passe de plus de 8 caractères : ")
     
     # On intercepte le 'raise' de la fonction check_mdp
     try:
         check_mdp(mot_de_passe)
         # Si on atteint cette ligne, c'est que la fonction n'a déclenché  aucune erreur. Le mot de passe est valide, on sort de la boucle. 
         break
         
     except ValueError as e:
         # On récupère le message d'erreur de la fonction  pour l'afficher à l'utilisateur avant de recommencer la boucle.
         print(f"Erreur : {e}\n")
        

print("Mot de passe enregistré avec succès !")
