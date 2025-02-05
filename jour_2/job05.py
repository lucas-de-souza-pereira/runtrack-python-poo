class Car:

    def __init__(self):
        self.__brand = ""
        self.__model = ""
        self.__year = ""
        self.__kilometer = ""
        self.__running = False
        self.__tank = 50

    def set_car(self,brand,model,year,kilometer):
        self.__brand = brand
        self.__model = model
        self.__year = year
        self.__kilometer = kilometer

    def start(self):
        if self.__check_full() >= 5:
            self.__running = True
            print("vroum vroum")
        else:
            return print("no fuel to start")

    def stop(self):
        print("stop car")
        self.__running = False

    def running(self):
        self.__tank = 0

    def __check_full(self):
        return self.__tank


car = Car()
car.set_car("Volvo","C30",2010,10000)

car.start()
car.running()
car.stop()
car.start()