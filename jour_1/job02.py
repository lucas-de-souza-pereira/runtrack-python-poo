# basic

class Operation:

    def __init__(self,nombre1,nombre2):
        self.nombre1 = nombre1
        self.nombre2 = nombre2


p1 = Operation(12,3)

print(f"le nombre1 est {p1.nombre1}")
print(f"le nombre2 est {p1.nombre2}")

#  valeur dans argument  

class Operation2:

    def __init__(self):
        self.nombre1 = 12
        self.nombre2 = 3

    def print_number(self):
        nombre1 = self.nombre1
        nombre2 = self.nombre2
        return f"le nombre 1 est {nombre1} \nle nombre2 est {nombre2}"


p2 = Operation2()

print(p2.print_number())

# avec argument automatique

class Operation3:

    def __init__(self,nombre1,nombre2):
        self.nombre1 = nombre1
        self.nombre2 = nombre2

    def print_number(self):
        nombre1 = self.nombre1
        nombre2 = self.nombre2
        return f"le nombre1 est {nombre1} \nle nombre2 est {nombre2}"


p3 = Operation3(12,3)

print(p3.print_number())


# avec ___str___
class Operation4:

    def __init__(self,nombre1,nombre2):
        self.nombre1 = nombre1
        self.nombre2 = nombre2

    def __str__(self):
        return f"le nombre1 est {self.nombre1} \nle nombre2 est {self.nombre2}"


p4 = Operation4(12,3)

print(p4)



