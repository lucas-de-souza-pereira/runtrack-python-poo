class City:
    def __init__(self, name, population):
        self.__name = name
        self.__population = population
    
    def get_name(self):
        return self.__name
    
    def get_population(self):
        return self.__population
    
    def add_population(self):
        self.__population += 1

class Person:
    def __init__(self, name, age, citizen : City):
        self.__name = name
        self.__age = age
        self.__citizen = citizen
    
    def add_citizen(self):
        self.__citizen.add_population()


paris = City("Paris", 1000000)
marseille = City("Marseille", 861635)

print(f"Population of Paris : {paris.get_population()}")
print(f"Population of Marseille : {marseille.get_population()}")

john = Person("John", 45, paris)
myrtille = Person("Myrtille", 4, paris)
chloe = Person("Chloé", 18, marseille)

john.add_citizen()
myrtille.add_citizen()
chloe.add_citizen()

print(f"\nUpdate the population of the city of {paris.get_name()} : {paris.get_population()}")
print(f"Update the population of the city of {marseille.get_name()} : : {marseille.get_population()}")