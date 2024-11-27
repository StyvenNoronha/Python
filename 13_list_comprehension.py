#Liste valores de 0 a 10 que sejam menor do que 4
'''
for i in range(10):
    if i < 4:
         print(i)
'''
listNumber = [i for i in range(10) if i < 4]
#print(listNumber)

# Jogos que possuem a letra O
gamesList = { "CSGO", "DOTA2", "LOL", "PUBG", "HOTS", "FIFA"}
#newList = [ g for g in gamesList if "O" in g]
#print(newList)
'''
for g in gamesList:
    if "O" in g:
        print(g)
'''  

#Jogos que zerei
gamesFinished = [ g for g in gamesList if g != "HOTS"]
print(gamesFinished)
for g in gamesList:
    if "HOTS" != g:
        print(g)