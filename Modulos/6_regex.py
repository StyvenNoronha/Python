import re
text = "Lorem Ipsum is simply dummy text of the printing and typesetting industry."


#índice inicial e final de palavra
# O r significa que estamos trabalhando com uma string bruta(row string)
#match = re.search(r'typesetting', text)
#print(match.start())
#print(match.end())


#Buscando o indice que possui o ponto
site = 'http://google.com'
match = re.search(r'\.',site)
print(match)

#buscando uma lista de caracteres dentro de uma frase
padrao = "[a-m]"
result = re.findall(padrao,text)
print(result)


#verificando o inicio de uma string
rule = r'^A'
phrases = [ 'A casa e muito divertida ']
for f in phrases:
    if re.match(rule,f):
        print(f)
    else:
        print("não tem")   

#verifica o final da frase 
rulef = r'!$'
phrasesf = [ 'A casa e muito divertida ! ']
for f in phrasesf:
    if re.match(rulef,f):
        print(f)
    else:
        print("não tem")   #          