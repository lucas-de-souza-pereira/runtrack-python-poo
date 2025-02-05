class Student:
    def __init__(self, firstname,name , student_number):
        self.__name = name
        self.__firstname = firstname
        self.__student_number = student_number
        self.__credit = 0
        self.__level = self.__student_eval()
        # self.__level = ""
        # self.__student_eval()

    def add_credit(self, credit):
        if credit >= 0:
            self.__credit += credit
            self.__level = self.__student_eval()
            # self.__student_eval()
        else :
            print("error in input")

    def __student_eval(self):
        if self.__credit >= 90:
            return "Excellent"
        elif self.__credit >= 80:
            return "Very good"
        elif self.__credit >= 70:
            return "Good"
        elif self.__credit >= 60:
            return "Fair"
        else: 
            return "Insufficient"

    def print_credit(self):
        return f"{self.__firstname} {self.__name}'s credit number is {self.__credit} points"

    def student_info(self):
        print(f"Name = {self.__name}")
        print(f"First name = {self.__firstname}")
        print(f"Id = {self.__student_number}")
        print(f"Level = {self.__level}")
        

john = Student("John","Doe",145)

print(john.print_credit())
john.add_credit(10)
john.add_credit(-1)
john.add_credit(10)
john.add_credit(10)
print(john.print_credit())

john.add_credit(20)
print(john.print_credit())
john.student_info()
john.add_credit(20)
print(john.print_credit())
john.student_info()