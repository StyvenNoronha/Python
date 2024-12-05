def ler():
    with open("texto.txt","r",encoding="utf-8") as file:
        for line in file:
            print(line)

def lendo(nome,lines):
    from itertools import islice
    with open(nome, encoding="utf-8") as file:
        for line in islice(file, lines):
            print(line)
lendo("texto.txt",1)
