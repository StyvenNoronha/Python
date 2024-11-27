#Contagem regressiva
'''
inicio = 10
for r in range(10,0,-1):
    print(r)
print('beep')

x = 10
while x >= 0:
    print(x)
    x -= 1

import winsound, time
inicio = 10
for r in range(10,0,-1):
    print(r)
    time.sleep(1)
winsound.Beep(2500, 500)

'''
#Tabuada
numberTable = int(input("Digite o numero da tabuada"))
inicio = int(input("Digite o numero de inicio"))
fim = int(input("Digite o numero de fim"))
for n in range(inicio,fim + 1,1):
    print(f"{numberTable} X {n} = { numberTable * n}")
  