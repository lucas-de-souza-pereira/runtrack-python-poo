class Vehicle():

    def __init__(self,brand,model,year,price):
        self.brand = brand
        self.model = model
        self.year = year
        self.price = price
    
    def getVehiculeInformation(self):
        return f"""
Brand : {self.brand}
Model : {self.model}
Year : {self.year}
Price : {self.price} €"""
    
    def getStart(self):
        return f"Be careful, I'm driving with "

class Car(Vehicle):

    def __init__(self, brand, model, year, price):
        super().__init__(brand, model, year, price)
        self.door = 4

    def getVehiculeInformation(self):
        return super().getVehiculeInformation() +f"""
Number of door : {self.door}"""
    
    def getStart(self):
        return super().getStart()+f"my {self.model}"


yaris = Car("Toyata","Yaris",2010,12000)
print(yaris.getVehiculeInformation())
print(yaris.getStart())

class Motorbike(Vehicle):

    def __init__(self, brand, model, year, price):
        super().__init__(brand, model, year, price)
        self.wheel = 2

    def getVehiculeInformation(self):
        return super().getVehiculeInformation() +f"""
Number of wheel : {self.wheel}"""
    
    def getStart(self):
        return super().getStart()+f"my {self.model}"


yamaha = Motorbike ("Yamaha","1200 Vmax",1987,4500)
print(yamaha.getVehiculeInformation())
print(yamaha.getStart())