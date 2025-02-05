class Cercle:
    def __init__(self):
        self.radius = 0

    def changeRadius(self,radius):
        self.radius = radius

    def circumference(self):
        return (self.radius*2)*3.14

    def diameter(self):
        return self.radius*2
    
    def aera(self):
        return 3.14*(self.radius*self.radius) 

    def printInfos(self):
        return f"radius : {self.radius} \nDiameter  {self.diameter()} \nCircumference {self.circumference()}\nAera {self.aera()}"

cercle = Cercle()

cercle.changeRadius(4)

print(cercle.printInfos())

cercle.changeRadius(7)
print(cercle.printInfos())
