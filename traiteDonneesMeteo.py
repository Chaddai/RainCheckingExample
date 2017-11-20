# Module de traitement des données météo, permettant d'extraire les données
# intéressantes

def extraire3h(previsions, index=0):
    """Prenant l'ensemble des prévisions et un index en paramètre, cette fonction
    extrait la tranche de prévisions sur 3h indiquée par l'index (0 étant la tranche
    de 3h actuelle)"""

    return previsions["list"][0]

def extrairePluie(tranchePrevisions):
    """Prenant une tranche de 3h de prévisions, cette fonction en extrait la
    hauteur de pluie en mm sur les 3h"""

    if "rain" in tranchePrevisions:
        return tranchePrevisions["rain"]["3h"]
    else:
        # aucune pluie n'est prévue
        return 0