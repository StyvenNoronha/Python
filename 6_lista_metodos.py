gamesList = ["CSGO", "DOTA2", "LOL", "PUBG", "HOTS"]

#tamanho da lista
print(len(gamesList))

#recuperar um item da lista pelo indice
game = gamesList.index("PUBG")
print(game)
print(gamesList[game])

#adicionar um item na lista
gamesList.append("FIFA")
print(gamesList)

#Ordernar a lista
gamesList.sort()
print(gamesList)

alfabeto = ["q","w","e","r","t","y","u","i","o","p","a","s","d","f","g","h","j","k","l","z","x","c","v","b","n","m"]
alfabeto.sort()
#print(alfabeto)

#copiar uma lista para outra
lista_copia = gamesList.copy()
lista_copia.remove("PUBG")
print(lista_copia)

#remover um todos os itens da lista
gamesList.clear()
print(gamesList)