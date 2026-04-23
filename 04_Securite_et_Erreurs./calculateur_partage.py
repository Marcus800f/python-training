while True:
    try:
        montant = float(input("Quel est le montant total ? "))
        break
    except ValueError:
        print("Montant invalide, utilise des chiffres (ex: 45.50)")

while True:
    try:
        personnes = int(input("Combien de personnes paient l'addition ? "))
        
        # On tente la division directement dans le try
        part = montant / personnes 
        
        # Si la division a marché, on peut enfin sortir de la boucle !
        break 
        
    except ValueError:
        print("Erreur : Veuillez entrer un nombre entier.")
    except ZeroDivisionError:
        print("Impossible : Il faut au moins une personne pour payer !")


print(f"Chacun doit payer {part:.2f}€")
