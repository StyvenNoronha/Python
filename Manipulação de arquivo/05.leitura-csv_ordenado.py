cursos= []

with open("text.csv","r",encoding="utf-8") as file:
    for line in file:
        lingua,categoria = line.rstrip().split(",")
        cursos.append(f"{lingua} == {categoria}")


for curso in sorted(cursos):
    print(curso)