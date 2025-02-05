class Animal:

    def __init__(self):
        self.age = 0
        self.name = ""

    def growOld(self):
        return self.age + 1
        

    def appoint(self, name):
        self.name = name

frist_age = Animal()

print(f"the age of the animal is {frist_age.age}")

print(f"the age of the animal is {frist_age.growOld()}")

frist_age.appoint("Luna")

print(f"the animal is called {frist_age.name}")
