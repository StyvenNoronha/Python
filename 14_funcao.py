def name(nome):
    print(f'Ola {nome}')

name('Styven')


def soma(n1,n2):
    print(n1 + n2)


soma(1,1)

def create_game():
    name = input("Digite o nome do jogo \n")
    yearLaunch = int(input("Digite o ano de lançamento do jogo \n"))
    gamePrice = float(input("Digite o preço do jogo \n"))
    planInclude = input("Esta incluso no serviço mensal \n")
    noteRating = float(input("Digite a nota de avaliação do jogo\n"))

    print(f"{name} - R${gamePrice}")

create_game()