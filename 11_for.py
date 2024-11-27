gamesList = { "CSGO", "DOTA2", "LOL", "PUBG", "HOTS", "FIFA"}
# Iterando valores de uma lista
'''
for g in gamesList:
    print(g)
# Quando a condição for atendida, o Loop será encerrado
'''
'''
for g in gamesList:
    if g == "gta":
        break
    print(g)
'''

# Quando a condição for atendida, o Loop vai para a  próxima iteração
'''
for g in gamesList:
    if g == "LOL":
        continue
    print(g)
'''    

# Avaliação do jogo
gameName = input("Digite o nome do jogo \n")
gameRating = int(input("Digite a nota para  o jogo\n"))

sum = 0
for i in range(gameRating):
    note = float(input("Digite a nota para o jogo\n"))
    sum += note
print(f"Média de avaliação do jogo {gameName} é { sum/gameRating:.2f}")    