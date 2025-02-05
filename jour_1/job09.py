class Product:
    def __init__(self,name,priceET):
        self.name = name
        self.priceET = priceET
        self.VAT = 0.2

    def calculatePriceIT(self):
        return self.priceET + (self.priceET *self.VAT)
    
    def __str__(self):
        return f"Product {self.name} / Price {self.calculatePriceIT()}"


porduit1 = Product("banane",2)
porduit2 = Product("pomme",3)
porduit3 = Product("orange",1.2)

print(porduit1)
print(porduit2)
print(porduit3)