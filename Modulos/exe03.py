import re
#achar todos que sao caracteres especiais e incluindo espaços
text = "LoremIpsumissimplydummytextoftheprintingandtypesettingindustry0@@@@@@@."
verifica = re.compile(r'[^a-zA-Z0-9]')
result = re.findall(verifica,text)
print(result)