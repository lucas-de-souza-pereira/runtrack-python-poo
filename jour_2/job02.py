class Book:

    def __init__(self):
        self.__title = "Sous l'ombre des tropiques"
        self.__autor = "Pierre"
        self.__pages = 50

    def set_title(self,title,autor,pages):

        if pages >= 0:
            self.__pages = pages
            self.__title = title
            self.__autor = autor
        else:
            print("error on pages number")


    def get_info(self):
        return print(f"title :{self.__title} autor : {self.__autor} pages : {self.__pages}")


new_book = Book()

new_book.get_info()

new_book.set_title("Romeo et Juiletta","Bernard",20)
new_book.get_info()

new_book.set_title("Bernard et Bianca","JOJO",-1)
new_book.get_info()
