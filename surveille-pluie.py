# Programme principal : surveille les prévisions sur une ville et affiche un message
# d'alerte si de la pluie est prévue dans les 3h qui viennent

import sys
import time # pour gérer le temps (récupération régulière des données)
from tkinter import Tk, messagebox # afficher le pop-up d'alerte

from accesWeatherApi import recupererPrevisions
from traiteDonneesMeteo import extraire3h, extrairePluie, extraireDescription, extraireTimestamp

# Vérifie si l'appel au programme est de la bonne forme
if len(sys.argv) != 2:
    print("Usage du programme : {} NomDeLaVille".format(sys.argv[0]))
    exit()

# le premier argument doit être le nom de la ville
ville = sys.argv[1]

# cacher la fenêtre principale
root = Tk()
root.withdraw()

while(True):
    previsions = recupererPrevisions(ville)
    previsions3h = extraire3h( previsions, 0 )
    volumeDePluie = extrairePluie(previsions3h)
    description = extraireDescription(previsions3h)
    finTranche = extraireTimestamp(previsions3h)

    if volumeDePluie > 0:
        messagebox.showwarning("Prévision de pluie", "Il va pleuvoir {}mm dans les 3h qui viennent à {} ! la description est : {}.".format(volumeDePluie, ville, description))

    # on dort tant qu'on est dans la tranche de prevision actuelle
    while time.time() < finTranche:
        time.sleep(600) # 10 minutes
