gamesTuple = ("CSGO", "DOTA2", "LOL", "PUBG", "HOTS", "FIFA")
print(type(gamesTuple))

#nao deixa adicionar valor 
#nao pode remover valor
#nao pode ordenar valor

#buscar od dois primeiros itens da tupla
print(gamesTuple[0:2])
#buscar o ultimo item da lista
print(gamesTuple[-1])
#buscar jogos ate uma determinada posição
print(gamesTuple[:3])
#buscar jogos de uma posição em diante
print(gamesTuple[2:])
#recuperar um item da lista pelo indice
game = gamesTuple.index("PUBG")
print(game)