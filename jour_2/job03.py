class Book:

    def __init__(self):
        self.__title = "Sous l'ombre des tropiques"
        self.__autor = "Pierre"
        self.__pages = 50
        self.__available = True

    def set_title(self,title,autor,pages):

        if pages >= 0:
            self.__pages = pages
            self.__title = title
            self.__autor = autor
        else:
            print("error on pages number")

    def get_check(self):
        if  self.__available == True:
            return True
        else:
            return False

    def set_borrow(self):
        if self.get_check() == True:
            print(f"the book {self.__title} is avaible")
            print("here your book")
            self.__available = False
        else:
            print(f"the book {self.__title} is not avaible")

    def set_return(self):
        if self.get_check() == False:
            print("Thanks you, have a good day !")
            self.__available = True

    def get_info(self):
        return print(f"title :{self.__title} autor : {self.__autor} pages : {self.__pages}")


borrow_book = Book()
borrow_book.set_borrow()
borrow_book.set_borrow()
borrow_book.set_return()
