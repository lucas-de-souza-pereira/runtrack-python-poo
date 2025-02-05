class Point:

    def __init__(self):
        self.x = 0
        self.y = 0

    def printPoints(self):
        x = self.x
        y = self.y
        return f"x position : {x} / y position : {y}"
    
    def changeX(self,x):
        self.x = x

    def changeY(self,y):
        self.y = y

    def printX(self):
        x = self.x
        return f'x position : {x}'
    
    def printY(self):
        y = self.y
        return f"y position : {y}"

p1 = Point()

print(p1.printPoints())
print(p1.printX())
print(p1.printY())

p1.changeX(2)
p1.changeY(3)

print(p1.printPoints())
print(p1.printX())
print(p1.printY())