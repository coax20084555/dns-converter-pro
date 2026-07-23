# ==========================================
# DNS Converter Pro
# Fichier principal
# ==========================================

import tkinter as tk
from tkinter import ttk
import os

from interface import Interface
from historique import Historique


# ------------------------------------------
# Création de l'application
# ------------------------------------------

class DNSConverterPro:

    def __init__(self):

        self.root = tk.Tk()

        self.root.title(
            "DNS Converter Pro"
        )

        self.root.geometry(
            "950x650"
        )

        self.root.minsize(
            800,
            550
        )

        self.root.configure(
            bg="#0d0d0d"
        )


        # Création du dossier historique

        if not os.path.exists(
            "historique.txt"
        ):
            open(
                "historique.txt",
                "w",
                encoding="utf-8"
            ).close()


        # Gestion historique

        self.historique = Historique()


        # Interface

        self.interface = Interface(
            self.root,
            self.historique
        )


    def lancer(self):

        self.root.mainloop()



# ------------------------------------------
# Lancement
# ------------------------------------------

if __name__ == "__main__":

    application = DNSConverterPro()

    application.lancer()