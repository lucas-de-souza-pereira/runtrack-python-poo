class Form:

    def get_aera(self):
        return 0
    
class Rectangle(Form):
    def __init__(self,length,width):
        super().__init__()
        self.length = length
        self.width = width

    def get_aera(self):
        return (self.length*self.width)
    
class Circle(Form):
    def __init__(self,radius):
        super().__init__()
        self.radius = radius

    def get_aera(self):
        return 3.14*(self.radius*self.radius)

rectangle = Rectangle(10,5)
print(rectangle.get_aera())

circle = Circle(5)
print(circle.get_aera())