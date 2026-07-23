# ==========================================
# DNS Converter Pro
# Fonctions réseau
# ==========================================

import socket
import re



# ------------------------------------------
# Vérification IP
# ------------------------------------------

def est_une_ip(texte):

    modele = r"^(?:[0-9]{1,3}\.){3}[0-9]{1,3}$"

    return re.match(
        modele,
        texte
    ) is not None



# ------------------------------------------
# URL vers IP
# ------------------------------------------

def convertir_url_ip(url):

    try:

        # Nettoyage URL

        url = url.replace(
            "https://",
            ""
        )

        url = url.replace(
            "http://",
            ""
        )

        url = url.split(
            "/"
        )[0]


        ip = socket.gethostbyname(
            url
        )


        resultat = (
            f"🌐 Domaine : {url}\n"
            f"📍 Adresse IP : {ip}"
        )


        return resultat


    except socket.gaierror:


        return (
            "❌ Impossible de trouver "
            "l'adresse IP"
        )


    except Exception as erreur:


        return (
            f"Erreur : {erreur}"
        )



# ------------------------------------------
# IP vers nom d'hôte
# ------------------------------------------

def convertir_ip_host(ip):

    try:


        nom = socket.gethostbyaddr(
            ip
        )[0]


        resultat = (
            f"📍 IP : {ip}\n"
            f"🌐 Nom d'hôte : {nom}"
        )


        return resultat


    except socket.herror:


        return (
            "❌ Aucun nom d'hôte "
            "associé à cette IP"
        )


    except Exception as erreur:


        return (
            f"Erreur : {erreur}"
        )



# ------------------------------------------
# Détection automatique
# ------------------------------------------

def convertir_auto(entree):


    if est_une_ip(entree):

        return convertir_ip_host(
            entree
        )

    else:

        return convertir_url_ip(
            entree
        )