import random
done = False


while not done: 
    r1 = random.randint(1, 10)

    
    print('tente adivinhar um numero de 1 a 10 . ')
    print(f"dica: {r1 + 1, r1 -1}")
    p = int(input("digite um numero\n"))

    if r1 == p:
        print("parabéns voce acertou")
        done = True
    else:
        print("Voce errou")   
