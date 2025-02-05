class Person:

    def __init__(self, frist_name, name):
        self.frist_name = frist_name
        self.name = name
        

    def introduceYourself(self):
        print("i am " + self.frist_name +" "+ self.name)

p1 = Person("John","Doe")
p2 = Person("Jean-Louis","Delabatte")


p1.introduceYourself()
p2.introduceYourself()