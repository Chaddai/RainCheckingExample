# Module d'accès à l'API weathermap

# accès à internet
import urllib.request
# traduction des données depuis le format JSON vers Python
import json

# openweathermap.org demande d'utiliser une clé par compte pour accéder à l'API
apiKey = "6dbd92ed5259f5a4bfa6ada9c71fc62d"

# charger les données géographiques et leur correspondance à une id
cityListJson = open("city.list.json", encoding='utf-8')
cityList = json.load(cityListJson)
cityListJson.close()


def recupererPrevisions(ville):
    """Cette fonction accède à l'API openweathermap.org pour télécharger les
    prévisions météo sur 5 jours par tranches de 3h de la ville passée en
    paramètre"""

    idVille = trouverID(ville)
    urlAPI = "http://api.openweathermap.org/data/2.5/forecast?id={}&APPID={}&units=metric&lang=fr".format(idVille,apiKey)

    previsionsJson = urllib.request.urlopen(urlAPI)
    previsions = json.loads(previsionsJson.read().decode('utf-8'))
    previsionsJson.close()

    return previsions

def trouverID(ville):
    """Cette fonction renvoie l'id correspondant à la ville passée en paramètre
    dans la base d'openweathermap.org ou soulève une exception si elle ne la
    trouve pas"""

    for lieu in cityList:
        if lieu["name"] == ville:
            return lieu["id"]

    # si on arrive jusqu'ici, c'est qu'on n'a pas trouvé la ville dans la base
    raise ValueError("{} n'est pas un nom de ville dans la base.".format(ville))