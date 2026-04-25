try:
    # On ouvre les deux fichiers en même temps
    with open("fichier1.txt", "r") as fichier_lecture, open("fichier2.txt", "a") as fichier_ecriture:
       for ligne in fichier_lecture:
               # Le filtre
               if "Alerte" in ligne:
                   fichier_ecriture.write(f"{ligne}") 

except FileNotFoundError:
    print("Erreur : Le fichier d'historique n'a pas été trouvé.")
else:
    print("Rapport généré avec succès dans rapport_alertes.txt")
