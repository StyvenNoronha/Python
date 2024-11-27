gameName = "World of Warcraft"
gameDescription = "MMORPG"

#string [start:stop] índice começa na posição 0 | stop é a posição final -1

#busque toda string a partir da primeira posição
print(gameName[0:])

#busque toda string ate a última posição
print(gameName[:17])

#busque toda string a partir da posição 3 ate a ultima posição
print(gameName[2:])

"""
string[start:stop:step]
"""
print(gameName[0:17:2])#busca toda string a partir da posição 0 ate a posição 17 pulando de 2 em 2

#busque toda a string os indices impares
print(gameName[1::2])

#inverter uma string de trás para frente
print(gameName[::-1])