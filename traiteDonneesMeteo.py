# Module de traitement des données météo, permettant d'extraire les données
# intéressantes

def extraire3h(previsions, index=0):
    """Prenant l'ensemble des prévisions et un index en paramètre, cette fonction
    extrait la tranche de prévisions sur 3h indiquée par l'index (0 étant la tranche
    de 3h actuelle)"""

    return previsions["list"][0]

def extrairePluie(tranche):
    """Prenant une tranche de 3h de prévisions, cette fonction en extrait la
    hauteur de pluie en mm sur les 3h"""

    if "rain" in tranche:
        return tranche["rain"]["3h"]
    else:
        # aucune pluie n'est prévue
        return 0

def extraireDescription(tranche):
    """Prenant une tranche de 3h de prévisions, cette fonction en extrait la
    description du temps en français sur cette tranche"""

    return tranche["weather"][0]["description"]

def extraireTimestamp(tranche):
    """Extrait le timestamp indiquant la fin de la tranche de prévision passée
    en paramètre"""

    return tranche["dt"]
