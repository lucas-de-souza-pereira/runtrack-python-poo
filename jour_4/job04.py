class Form:

    def get_aera(self):
        return 0
    
class Rectangle(Form):
    def __init__(self):
        super().__init__()
        self.length = 10
        self.width = 5

    def get_aera(self):
        return (self.length*self.width)
    
rectangle = Rectangle()
print(rectangle.get_aera())