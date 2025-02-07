

class BankAccount:

    def __init__(self, account_number, name, first_name, balance, overdraft : bool ):
        self.__account_number = account_number
        self.__name = name
        self.__first_name = first_name
        self.__balance = balance
        self.__overdraft = overdraft

    def get_account(self):
        return f"""
Account numer : {self.__account_number}
Name : {self.__name}
First name : {self.__first_name}
                """

    def get_balance(self):
        if self.get_overdraft_charge() >= 0:
            return f"""
    Account numer : {self.__account_number}
    Name : {self.__name}
    First name : {self.__first_name}
    Balance : {self.__balance}
                    """
        else : 
            return f"""
    Account number : {self.__account_number}
    Name : {self.__name}
    First name : {self.__first_name}
    Balance : {self.set_overdraft_charge()}
    Overdraft_charge : {round(abs(self.get_overdraft_charge()),2)}
                    """

    def set_depot_it(self, depot_it):
        self.__balance += depot_it
        return self.__balance

    def set_withdrawal(self, withdrawal :int):
            self.__balance -= withdrawal
            if self.__balance >= 0:
                print (f"New balance : {self.__balance}")
            elif self.__balance >= -600 and self.__balance <= 0 and self.__overdraft == True:
                print (f"""New balance : {self.__balance}
attention negative balance""")
            else: 
                print (f"withdrawal impossible")
                self.__balance += withdrawal
            return self.__balance

    def get_overdraft_charge(self):
        __charge = 0.07
        return (self.__balance*__charge)
    
    def set_overdraft_charge(self):
        self.__balance += self.get_overdraft_charge()
        return self.__balance
    
    def set_payment(self,account_number_in,payment):
        
        if account_number_in == self.__account_number:
            paul.__balance -= payment
            self.__balance += payment
            print("\n payment done.")
            return self.__balance
        else : 
            print("\nthis account don't exists")

paul = BankAccount(125,"Ricard","Paul",10000,True)
paul2 = BankAccount(126,"Ricard","Paul",-500,True)
# paul.set_depot_it(500)

# print(paul.get_balance())

# paul.set_withdrawal(1050)
# print(paul.get_balance())

paul2.set_payment(126,500)
print(paul.get_balance())
print(paul2.get_balance())

