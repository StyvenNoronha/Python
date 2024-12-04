'''
1 - O método de classe utiliza o primeiro parâmetro cls referente a classe
2 - O método de classe pode acessar ou modificar o estado da classe 
3 - Usamos o decorator @classmethod em python para criar um método de classe
'''

class Console:
    def __init__(self, name, price):
        self.name = name
        self.price = price


    @classmethod
    def from_text(cls, string):
        import re
        item = re.findall("é \\w*", string)
        name = item[0][2:]
        price = item[1][2:]
        return  cls(name, int(price))

wiiU = Console.from_text("meu video game é Wiiu e o preço é 1500 reais")        
xbox = Console.from_text("meu video game é xbox e o preço é 2500 reais")        

print(wiiU.__dict__)
print(xbox.__dict__)