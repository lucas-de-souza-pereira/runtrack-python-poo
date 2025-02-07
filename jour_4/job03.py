class Rectangle:
    def __init__(self,length,width):
        self.__length = length
        self.__width = width

    def get_perimeter(self):
        return (self.__length+self.__width)*2
    
    def get_surface(self):
        return (self.__length*self.__width)
    
    def get_length(self):
        return self.__length
    
    def get_width(self):
        return self.__width   


class Parallepiped(Rectangle):
    def __init__(self,rectangle : Rectangle,height):
        super().__init__(rectangle.get_length(),rectangle.get_width())
        self.__height = height

    def get_volume(self):
        return ( self.get_width() *self.get_length() * self.__height )

rectangle = Rectangle(10,5)
print(rectangle.get_perimeter())
print(rectangle.get_surface())
parallepiped = Parallepiped(rectangle,3)
print(parallepiped.get_volume())