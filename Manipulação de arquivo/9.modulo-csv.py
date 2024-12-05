import csv

cursos = []

with open("text.csv","r",encoding="utf-8") as file:
    reader = csv.DictReader(file)
    for row in reader:
        cursos.append({"lingua":row["lingua"], "category":row["categoria"]})

print(cursos)
