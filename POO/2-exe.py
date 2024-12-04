class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def __str__(self):
        return f" o produto {self.name} custa R${ self.price}"

    def apply_discount(self, perc_discount):
        valorDiscount = (self.price/100) * perc_discount
        finalPrice = self.price - valorDiscount
        return int(finalPrice)


# Exemplo de uso:
notebook = Product("notebook acer",400)
print(notebook)
print(notebook.apply_discount(10))




