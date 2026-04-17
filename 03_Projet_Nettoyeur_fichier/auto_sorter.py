import shutil
import os


REGLES = {
    "Images": [".jpg", ".png", ".gif"],
    "Documents": [".pdf", ".txt", ".docx"],
    "Musique": [".mp3", ".wav"],
    "Videos": [".mp4", ".avi"]
}


def trouver_dossier(nom_fichier):
    nom_min = nom_fichier.lower()
    for categorie, document_type in REGLES.items():
        for document_ty in document_type:


            if nom_min.endswith(document_ty):
                print(f"Le fichier {nom_fichier} va etre deplacé dans {categorie}")
                os.makedirs(f"{categorie}", exist_ok=True)
                shutil.move(nom_fichier, categorie)
                return

    print(f"Le fichier {nom_fichier} est introuvable (Divers)")



fichiers_sur_le_bureau = os.listdir('.')
for fichier_actuel in fichiers_sur_le_bureau:
    trouver_dossier(fichier_actuel)
