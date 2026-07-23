# ==========================================
# DNS Converter Pro
# Gestion de l'historique
# ==========================================

from datetime import datetime
import os



FICHIER = "historique.txt"



class Historique:


    def __init__(self):

        self.nombre_recherches = 0


        # Création du fichier si absent

        if not os.path.exists(FICHIER):

            with open(
                FICHIER,
                "w",
                encoding="utf-8"
            ) as fichier:

                fichier.write(
                    "=== DNS Converter Pro ===\n\n"
                )


        # Compter les recherches existantes

        self.compter()



    # --------------------------------------
    # Ajouter une recherche
    # --------------------------------------

    def ajouter(
            self,
            recherche,
            resultat):


        date = datetime.now().strftime(
            "%d/%m/%Y %H:%M:%S"
        )


        ligne = (
            f"[{date}]\n"
            f"Recherche : {recherche}\n"
            f"Résultat : {resultat}\n"
            f"{'-'*50}\n"
        )


        with open(
            FICHIER,
            "a",
            encoding="utf-8"
        ) as fichier:

            fichier.write(
                ligne
            )


        self.nombre_recherches += 1



    # --------------------------------------
    # Lire historique
    # --------------------------------------

    def lire(self):


        try:

            with open(
                FICHIER,
                "r",
                encoding="utf-8"
            ) as fichier:

                return fichier.read()


        except:


            return (
                "Aucun historique disponible."
            )



    # --------------------------------------
    # Effacer historique
    # --------------------------------------

    def effacer(self):


        with open(
            FICHIER,
            "w",
            encoding="utf-8"
        ) as fichier:


            fichier.write(
                "=== Historique vide ===\n"
            )


        self.nombre_recherches = 0



    # --------------------------------------
    # Compteur
    # --------------------------------------

    def compter(self):

        try:

            with open(
                FICHIER,
                "r",
                encoding="utf-8"
            ) as fichier:

                contenu = fichier.read()


            self.nombre_recherches = (
                contenu.count("Recherche :")
            )


        except:

            self.nombre_recherches = 0



    # --------------------------------------
    # Statistiques
    # --------------------------------------

    def statistiques(self):

        return (
            f"Nombre de recherches : "
            f"{self.nombre_recherches}"
        )