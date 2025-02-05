class Command:

    def __init__(self):    
        self.__command_id = 0
        self.__ordered_dishes = []
        self.__oder_status = ["progress","completed","canceled"]
        self.__command_dict = {}
        self.__price = {"poulet":10,"coucous":20,"fromage":5}
        self.__VAT = 0.2

    def add_order(self, *dish):
        self.__command_id +=1
        self.__ordered_dishes.append(dish)
        self.__command_dict[self.__command_id] = {"dish" :list(dish), "status" :self.__oder_status[0], "price" : 0}
        
        self.calculation()

    def cancel_order(self, command_id):
        self.__command_id = command_id
        self.__command_dict[self.__command_id]["status"] = self.__oder_status[2]

        self.calculation()

    def calculation(self):
        
        for order_id, command_detail in self.__command_dict.items():        
            total_ET = 0

            if command_detail["status"] == "progress":
                for dishs in command_detail["dish"]:
                    total_ET += self.__price[dishs]

            total_IT = total_ET + (total_ET*self.__VAT)
            self.__command_dict[order_id]["price"] = total_IT

    def print_order(self):

        for order_id, dishs in self.__command_dict.items():
                    print(f"Command {order_id} : {dishs}")

client = Command()

client.add_order("poulet","fromage")
client.add_order("coucous")
client.print_order()
client.cancel_order(2)
client.print_order()
client.add_order("fromage")
client.print_order()

# référence copie de la valeur pour que la valeur d'origine ne soit pas modifié 
# import copy() attention copy ne prendre en compte que le premier niveau (exemple que le premier nibeau d'une liste)

#  ou deepcopy() pour tout attention deepcopy est bien plus long et terme de lecture
