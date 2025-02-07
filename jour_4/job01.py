class Person:

    def __init__(self):
        self.age = 14

    def get_age(self):
        return print(f"age : {self.age}")
    
    def get_hello(self):
        if self.age <=18:
            return print(f"Hello professor")
        else:
            return print(f"Hello student")
    
    def set_age(self,age):
        self.age = age
        return self.age

class Student(Person):

    def __init__(self):
        super().__init__()

    def go_to_school(self):
        return print("i going to school")
    
    def get_age_student(self):
        return print(f"i am {self.age}")

class Professor(Person):
    def __init__(self, subject):
        super().__init__()
        self.__subject_taught = subject

    def get_age_professor(self):
        return print(f"i am {self.age}")

    def teach(self):
        return print(f"{self.__subject_taught} class is about to start")

john = Person()
john = Student()

john.get_age()
