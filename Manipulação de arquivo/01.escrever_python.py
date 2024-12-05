'''
w - write
a - append
r - read
'''

name = input("digite seu nome\n")

#cria um arquivo e escreve nele
'''file = open("name.txt","w",)
file.write(name)
file.close()
'''

#Pode adicionar vários nomes em um arquivo txt
'''
file = open("name.txt","a",)
file.write(f"{name}\n")
file.close()
'''

#alternativa 2
with open("names1.txt","a") as file:
    file.write(f"{name}\n")
