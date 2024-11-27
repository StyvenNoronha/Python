dicionarioGame = {
    "nome":"fifa",
    "ano":2019,
    "desenvolvedor":"EA",
    "genero":[
        "esporte",
        "futebol",
        "simulador"
    ]
}

print(type(dicionarioGame))
print(dicionarioGame["genero"])
print(dicionarioGame["genero"][1])
#adicionar um novo elemento
print(dicionarioGame.get('ano'))
#Buscar apenas as chaves do dicionario
print(dicionarioGame.keys())
#Buscar apenas os valores do dicionario
print(dicionarioGame.values())
#Buscar todos os itens do dicionario
print(dicionarioGame.items())
#adicionar um novo elemento
dicionarioGame["author"] = "EA"
print(dicionarioGame)
#atualizar um elemento
dicionarioGame["ano"] = 2027
print(dicionarioGame)
#remover um elemento
dicionarioGame.pop("ano")
print(dicionarioGame)