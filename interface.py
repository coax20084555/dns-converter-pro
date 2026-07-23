# ==========================================
# DNS Converter Pro
# Interface graphique
# ==========================================

import tkinter as tk
from tkinter import ttk, messagebox

from fonctions import (
    convertir_url_ip,
    convertir_ip_host
)


class Interface:


    def __init__(self, root, historique):

        self.root = root
        self.historique = historique


        # Couleurs

        self.NOIR = "#0d0d0d"
        self.CADRE = "#171717"
        self.VIOLET = "#7b00ff"
        self.VIOLET_CLAIR = "#d580ff"
        self.GRIS = "#252525"


        self.creer_style()

        self.creer_menu()

        self.creer_interface()



    # --------------------------------------
    # Style
    # --------------------------------------

    def creer_style(self):

        style = ttk.Style()

        style.theme_use("default")


        style.configure(
            "TNotebook",
            background=self.NOIR,
            borderwidth=0
        )


        style.configure(
            "TNotebook.Tab",
            background=self.CADRE,
            foreground=self.VIOLET_CLAIR,
            padding=(20,10),
            font=("Arial",11)
        )


        style.map(
            "TNotebook.Tab",
            background=[
                ("selected",self.VIOLET)
            ],
            foreground=[
                ("selected","white")
            ]
        )



    # --------------------------------------
    # Menu
    # --------------------------------------

    def creer_menu(self):

        menu = tk.Menu(
            self.root,
            bg=self.CADRE,
            fg="white"
        )


        fichier = tk.Menu(
            menu,
            tearoff=0,
            bg=self.CADRE,
            fg="white"
        )


        fichier.add_command(
            label="Quitter",
            command=self.root.destroy
        )


        menu.add_cascade(
            label="Fichier",
            menu=fichier
        )


        aide = tk.Menu(
            menu,
            tearoff=0,
            bg=self.CADRE,
            fg="white"
        )


        aide.add_command(
            label="À propos",
            command=self.apropos
        )


        menu.add_cascade(
            label="Aide",
            menu=aide
        )


        self.root.config(
            menu=menu
        )



    def apropos(self):

        messagebox.showinfo(
            "DNS Converter Pro",
            "DNS Converter Pro\n\n"
            "Convertisseur URL ↔ IP\n"
            "Créé en Python avec Tkinter"
        )



    # --------------------------------------
    # Interface
    # --------------------------------------

    def creer_interface(self):


        self.tabs = ttk.Notebook(
            self.root
        )


        self.page_convertisseur = tk.Frame(
            self.tabs,
            bg=self.NOIR
        )


        self.page_historique = tk.Frame(
            self.tabs,
            bg=self.NOIR
        )


        self.tabs.add(
            self.page_convertisseur,
            text="Convertisseur"
        )


        self.tabs.add(
            self.page_historique,
            text="Historique"
        )


        self.tabs.pack(
            fill="both",
            expand=True
        )


        self.creer_convertisseur()

        self.creer_historique()



    # --------------------------------------
    # Page conversion
    # --------------------------------------

    def creer_convertisseur(self):


        titre = tk.Label(
            self.page_convertisseur,
            text="🌐 DNS CONVERTER PRO",
            bg=self.NOIR,
            fg=self.VIOLET_CLAIR,
            font=("Arial",24,"bold")
        )

        titre.pack(
            pady=30
        )


        self.entree = tk.Entry(
            self.page_convertisseur,
            width=55,
            bg=self.GRIS,
            fg="white",
            insertbackground="white",
            font=("Consolas",14),
            relief="flat"
        )


        self.entree.pack(
            pady=15
        )


        bouton_frame = tk.Frame(
            self.page_convertisseur,
            bg=self.NOIR
        )


        bouton_frame.pack(
            pady=20
        )


        self.bouton_convertir = self.creer_bouton(
            bouton_frame,
            "Convertir",
            self.convertir
        )


        self.bouton_convertir.grid(
            row=0,
            column=0,
            padx=10
        )


        self.bouton_copier = self.creer_bouton(
            bouton_frame,
            "Copier",
            self.copier
        )


        self.bouton_copier.grid(
            row=0,
            column=1,
            padx=10
        )


        self.resultat = tk.Label(
            self.page_convertisseur,
            text="En attente...",
            bg=self.NOIR,
            fg=self.VIOLET_CLAIR,
            font=("Consolas",14)
        )


        self.resultat.pack(
            pady=30
        )


        self.status = tk.Label(
            self.page_convertisseur,
            text="✓ Prêt",
            bg=self.NOIR,
            fg="#00ff88"
        )


        self.status.pack(
            side="bottom",
            pady=10
        )



    # --------------------------------------
    # Boutons
    # --------------------------------------

    def creer_bouton(
            self,
            parent,
            texte,
            commande):


        return tk.Button(
            parent,
            text=texte,
            command=commande,
            bg=self.VIOLET,
            fg="white",
            width=18,
            height=2,
            relief="flat",
            cursor="hand2"
        )



    # --------------------------------------
    # Conversion
    # --------------------------------------

    def convertir(self):

        valeur = self.entree.get().strip()


        if valeur == "":
            return


        if "." in valeur and valeur.replace(".","").isdigit():

            resultat = convertir_ip_host(
                valeur
            )

        else:

            resultat = convertir_url_ip(
                valeur
            )


        self.resultat.config(
            text=resultat
        )


        self.historique.ajouter(
            valeur,
            resultat
        )



    def copier(self):

        self.root.clipboard_clear()

        self.root.clipboard_append(
            self.resultat.cget("text")
        )



    # --------------------------------------
    # Historique
    # --------------------------------------

    def creer_historique(self):

        self.zone_historique = tk.Text(
            self.page_historique,
            bg="#101010",
            fg=self.VIOLET_CLAIR,
            font=("Consolas",12)
        )


        self.zone_historique.pack(
            fill="both",
            expand=True,
            padx=20,
            pady=20
        )


        self.zone_historique.insert(
            "end",
            self.historique.lire()
        )


        self.zone_historique.config(
            state="disabled"
        )