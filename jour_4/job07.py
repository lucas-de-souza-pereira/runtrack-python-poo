import random

class Card:
    """init cards"""
    def __init__(self):
        self.value = ""
        self.color = ""
        self.cardpack = []

    def GetCreateCardPack(self):
        """Create a list of 52 carts in int"""
        for createcard in range(1,53):
            self.cardpack.append(createcard)
        return self.cardpack

    def GetAssignValueCard(self,value):
            """Attribute valor AS, number, figure in str"""
            self.value = value
            if self.cardpack[self.value-1] <= 4:
                self.value = "AS"
                return self.value
            elif self.cardpack[self.value-1] >= 5 and self.cardpack[self.value-1] <= 14 :
                self.value = str(self.cardpack[self.value-1]-4)
                return self.value
            elif self.cardpack[self.value-1] >= 15 and self.cardpack[self.value-1] <= 24 :
                self.value = str(self.cardpack[self.value-1]-14)
                return self.value
            elif self.cardpack[self.value-1] >= 25 and self.cardpack[self.value-1] <= 35 :
                self.value = str(self.cardpack[self.value-1]-24)
                return self.value
            elif self.cardpack[self.value-1] >= 35 and self.cardpack[self.value-1] <= 45 :
                self.value = str(self.cardpack[self.value-1]-34)
                return self.value
            else:
                self.value = "Figure"
                return self.value

    def GetAssignColorCard(self,value):
        """Asign color --> if even color = RED"""
        self.value = value
        if self.cardpack[self.value-1] <= 4:
            if self.cardpack[self.value-1] %2 == 0 :
                self.color = "Red"
                return self.color
            else:
                self.color = "Back"
                return self.color
        elif self.cardpack[self.value-1] >= 5 and self.cardpack[self.value-1] <= 14 :
            self.color = "Red"
            return self.color
        elif self.cardpack[self.value-1] >= 15 and self.cardpack[self.value-1] <= 24 :
            self.color = "Back"
            return self.color
        elif self.cardpack[self.value-1] >= 25 and self.cardpack[self.value-1] <= 35 :
            self.color = "Red"
            return self.color
        elif self.cardpack[self.value-1] >= 35 and self.cardpack[self.value-1] <= 45 :
            self.color = "Back"
            return self.color
        else:
            if self.cardpack[self.value-1] %2 == 0 :
                self.color = "Red"
                return self.color
            else:
                self.color = "Back"
                return self.color

    def getRandomCard(self,value):
        """Return value and color to print"""
        
        self.GetAssignColorCard(value)
        self.GetAssignValueCard(value)
        return f"{self.value} {self.color}"

    def getValue(self): 
        value = random.choice(self.GetCreateCardPack())
        return value
    
class Game(Card):
    def __init__(self):
        super().__init__()
        self.player = "" #player or dealer
        self.number_card = "" # =number_card -> how card distribude

    def setPlayer(self):
        if self.player == "player":
            self.player = "dealer"
        else: 
            self.player = "player"

    def setDrawcard(self):

        return self.getValue()

    # def play(self):
    #     i=0
    #     if self.player == "player":
    #         while i < 3:
    #             print(self.setDrawcard())
    #             i +=1


# L'as : 1 ou 11. Sa valeur est de 11 lorsque ce 11 ne vous fait pas dépasser 21. Autrement, l'as vaut 1.
# le couprier s'arrete a 17 mini

# test = Card()
# print(test.getRandomCard())

test2= Game()
print(test2.setDrawcard())