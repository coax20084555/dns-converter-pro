# ==========================================
# DNS Converter Pro
# Informations IP
# ==========================================

import urllib.request
import json



# ------------------------------------------
# Obtenir les informations IP
# ------------------------------------------

def obtenir_infos_ip(ip):

    try:

        url = (
            "https://ipinfo.io/"
            + ip
            + "/json"
        )


        requete = urllib.request.urlopen(
            url,
            timeout=5
        )


        donnees = json.loads(
            requete.read()
        )


        pays = donnees.get(
            "country",
            "Inconnu"
        )


        ville = donnees.get(
            "city",
            "Inconnue"
        )


        region = donnees.get(
            "region",
            "Inconnue"
        )


        organisation = donnees.get(
            "org",
            "Inconnue"
        )


        timezone = donnees.get(
            "timezone",
            "Inconnu"
        )


        resultat = (
            f"🌍 Pays : {pays}\n"
            f"🏙️ Ville : {ville}\n"
            f"📌 Région : {region}\n"
            f"🏢 Organisation : {organisation}\n"
            f"🕒 Fuseau horaire : {timezone}"
        )


        return resultat



    except Exception:


        return (
            "❌ Impossible de récupérer "
            "les informations IP."
        )



# ------------------------------------------
# Test rapide
# ------------------------------------------

if __name__ == "__main__":

    print(
        obtenir_infos_ip(
            "8.8.8.8"
        )
    )