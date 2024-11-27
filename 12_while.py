gameName = input("Digite o nome do jogo \n")

qtdRanting = 0
totalRanting = 0
rating = 0
average = 0

while(rating != -1):
    rating = float(input("Digite a nota para o jogo. Para para digite -1\n"))
    if(rating != -1):
        totalRanting += rating #totalRating + ranting
        qtdRanting += 1 # qtdRanting + 1
        average = totalRanting / qtdRanting
print(f"Média das avaliações do jogo {gameName} é {average:.2f} ")         



