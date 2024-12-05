import csv

name = input("Informe o nome da linguagem que deseja aprender?\n")
category = input("Qual categoria que a linguagem se encaixa?\n")


with open("text.csv","a",encoding="utf-8") as file:
    write = csv.writer(file, lineterminator='\n')
    write.writerow([name,category])
