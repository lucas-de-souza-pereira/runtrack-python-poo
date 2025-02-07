class Part():
    def __init__(self,name,material):
        self.name = name
        self.material = material

    def changeMaterial(self,new_material):
        self.material = new_material
        return self.material

    def __str__(self):
        return f"""
Part's name : {self.name}
Material : {self.material}"""


class Ship():

    def __init__(self,boat_name):
        self.boat_name = boat_name
        self.__parts = {"Mat": Part("Mat","Bois"),
                        "Voile" : Part("Voile","Tissu"),
                        "Gouvernail": Part("Gouvernail","Bois")}

    def diplayState(self):
        print(f"Ship's name : {self.boat_name}")
        for part in self.__parts.values():
            print(f"{part}")

    def remplacePart(self,part_name,new_part):
        self.__parts[part_name] = new_part
        return self.__parts

    def changePart(self,part_name,new_material):
        self.__parts[part_name].changeMaterial(new_material)
        return self.__parts

class RacingShip(Ship):
    def __init__(self, boat_name, max_speed):
        super().__init__(boat_name)
        self.max_speed = max_speed

    def diplaySpeed(self):
        return f"""Speed max : {self.max_speed} miles/hour"""


# baracouda = Ship("Baracouda")
# new_mat = Part("New Mat","Bois")

# baracouda.remplacePart("Mat",new_mat)
# baracouda.changePart("Mat","Carbone")
# baracouda.diplayState()

baracouda = RacingShip("Baracouda",100)
# print(baracouda.diplaySpeed())


while True :

    choice = input("""
                   Ship menu : 
    1. remplace parts
    2. edit materials
    3. show ship's composants
    4. exit
                """)

    if choice == "1" :
        print("Name parts : Mat, Voile, Gouvernail")
        part = input("What parts do you want to change ? ")
        new_name_part = input("New name part : ")
        material = input("Material: ")
        new_part = Part(new_name_part,material)
        baracouda.remplacePart(part,new_part)

    elif choice == "2":
        print("Name parts : Mat, Voile, Gouvernail")
        part = input("What material do you want to change ? ")
        material = input("Material: ")
        baracouda.changePart(part,material)


    elif choice == "3":
        print(baracouda.diplayState())
        print(baracouda.diplaySpeed())

    elif choice == "4":
        exit()