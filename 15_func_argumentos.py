def fullname(fname,lname):
    print(f"seu nome completo é {fname + lname}")


fullname("styven", "noronha")



def soma(n1,n2):
    return n1 + n2

print(soma(5,5))


#argumentos default
def address(country="Brasil"):
    print(f"Eu moro no {country}")

address()    
address("Canadá")    


##########################################################

def ratingGame(qrdRating):
    gameName = input("Digite o nome do jogo \n")


    sum = 0
    for i in range(qrdRating):
        note = float(input("Digite a nota para o jogo\n"))
        sum += note
    print(f"Média de avaliação do jogo {gameName} é { sum/qrdRating:.2f}") 


ratingGame(2)    