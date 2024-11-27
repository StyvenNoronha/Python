#calculo da distancia entre dois pontos
'''
distancia  = int(input("Digite a distancia em km : "))
if distancia <= 200:
    print("O preço da passagem é de R$0,50 por km")
    print("O preço da passagem é de R$",distancia*0.50)
else:
    print("O preço da passagem é de R$0,35 por km")
    print("O preço da passagem é de R$",distancia*0.35)
'''

#aumento salário funcionário
salario = float(input("Digite o salário do funcionário : "))
if salario >= 1250:
    print("O salário do funcionário é de R$",salario)
    print("O salário do funcionário com aumento é de R$",salario*1.10)
else:
    print("O salário do funcionário é de R$",salario)
    print("O salário do funcionário com aumento é de R$",salario*1.15)