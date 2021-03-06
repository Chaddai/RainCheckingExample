﻿# Programme principal : vérifie s'il va pleuvoir dans les 3h dans une ville donnée

import sys # pour lire l'argument du programme en ligne de commande

# fonctions spécifiques à l'application
from accesWeatherApi import recupererPrevisions
from traiteDonneesMeteo import extraire3h, extrairePluie, extraireDescription

# Vérifie si l'appel au programme est de la bonne forme
if len(sys.argv) != 2:
    print("Usage du programme : {} NomDeLaVille".format(sys.argv[0]))
    exit()

# le premier argument doit être le nom de la ville
ville = sys.argv[1]


previsions = recupererPrevisions(ville)
previsions3h = extraire3h( previsions, 0 )
volumeDePluie = extrairePluie(previsions3h)
description = extraireDescription(previsions3h)

if volumeDePluie > 0:
    print("Il va pleuvoir {}mm dans les 3h qui viennent à {} ! la description est : {}.".format(volumeDePluie, ville, description))
else:
    print("Il ne pleuvra pas dans les 3h qui viennent à {}, la description est : {}.".format(ville, description))