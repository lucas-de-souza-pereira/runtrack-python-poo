class Operation:

    def __init__(self,nombre1,nombre2):
        self.nombre1 = nombre1
        self.nombre2 = nombre2

    def addition(self):
        return self.nombre1 + self.nombre2

    def __str__(self):
        return f"le nombre1 est {self.nombre1} \nle nombre2 est {self.nombre2} \nla valeur est égale à {self.addition()}"


p1 = Operation(12,3)

print(p1)

class Operation2:

    def __init__(self,nombre1,nombre2):
        self.nombre1 = nombre1
        self.nombre2 = nombre2

    def addition(self):
        resultat = self.nombre1 + self.nombre2
        return f"le resultat est {resultat}"

p2 = Operation2(12,3)

print(p2.addition())
