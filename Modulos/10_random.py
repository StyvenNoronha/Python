import random

#selecionar o valor aleatório de uma lista
list = [ 1,2,3,4,5,6,7,8,9]
#print(random.choice(list))

# 2 - Gera número aleatório em um intervalo de valores
'''a = int(input("digita um numero\n"))
b = int(input("digita outro numero\n"))
r1 = random.randint(a, b)
print(r1)
'''
# 3 - Seleciona caractere aleatório de uma string
name = "Curso Python"
r2 = random.choice(name)
print(r2)


# 4 - Selecionando mais de um valor aleatório
# Sintaxe: random.sample(sequencia, tamanho)
print(random.sample(list, 2))
print(random.sample(list, 3))
s = "Olá mundo"
print(random.sample(s, 2))