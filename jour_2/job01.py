class Rectangle:
    
    def __init__(self, lenght, width):
        self.__lenght = lenght
        self.__width = width

    def set_lenght(self, lenght):
        self.__lenght = lenght

    def set_width(self, width):
        self.__width = width

    def get_dimension(self):
        return f"lenght {self.__lenght} width {self.__width}"
    
    
rectangle = Rectangle(10,5)
print(rectangle.get_dimension())
rectangle.set_lenght(18)
rectangle.set_width(19)
print(rectangle.get_dimension())