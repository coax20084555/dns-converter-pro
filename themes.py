# ==========================================
# DNS Converter Pro
# Gestion du thème graphique
# ==========================================


class Theme:


    # Couleurs principales

    FOND = "#0d0d0d"

    CADRE = "#171717"

    GRIS = "#252525"


    # Violet

    VIOLET = "#7b00ff"

    VIOLET_CLAIR = "#d580ff"

    VIOLET_FONCE = "#4b0082"


    # Autres

    BLANC = "#ffffff"

    VERT = "#00ff88"

    ROUGE = "#ff3366"





    @staticmethod
    def appliquer_bouton(bouton):

        bouton.configure(

            bg=Theme.VIOLET,

            fg=Theme.BLANC,

            activebackground=Theme.VIOLET_CLAIR,

            activeforeground=Theme.BLANC,

            relief="flat",

            cursor="hand2"

        )





    @staticmethod
    def effet_survol(
            bouton):


        def entrer(event):

            bouton.configure(
                bg=Theme.VIOLET_CLAIR
            )


        def sortir(event):

            bouton.configure(
                bg=Theme.VIOLET
            )


        bouton.bind(
            "<Enter>",
            entrer
        )


        bouton.bind(
            "<Leave>",
            sortir
        )





    @staticmethod
    def configurer_fenetre(
            fenetre):


        fenetre.configure(
            bg=Theme.FOND
        )