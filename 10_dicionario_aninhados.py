import pprint
gamesDict = {
    "1": {
        "name": "God of War",
        "year": 2018,
        "developer": "Santa Monica Studio"
    },
    "2": {
        "name": "The Last of Us",
        "year": 2013,
        "developer": "Naughty Dog"
    },
    "3": {
        "name": "The Last of Us Part II",
        "year": 2020,
        "developer": "Naughty Dog"
    }
}
pp = pprint.PrettyPrinter(depth=4)
pp.pprint(gamesDict)
print(gamesDict["1"])

#buscar informacoes dentroo do dicionario
print(gamesDict["1"]["name"])

#adicionar um novo elemento
gamesDict["4"] = {
    "name": "The Witcher 3: Wild Hunt",
    "year": 2015,
    "developer": "CD Projekt Red"
}
pp.pprint(gamesDict)