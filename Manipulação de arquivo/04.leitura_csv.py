with open("text.csv","r",encoding="utf-8") as file:
    for line in file:
        lingua,categoria = line.rstrip().split(",")
        print(f"{lingua} e { categoria}")