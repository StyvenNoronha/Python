languages = []

with open("text.csv", encoding="utf-8") as file:
    for line in file:
        language, category = line.rstrip().split(",")
        languages.append(f"{language} - {category}") 

for language in sorted(languages):
    print(language)
