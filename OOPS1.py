
# for declaring private variable -> self.__variable
# for declaring protected variable -> self._variable
# for declaring public variable -> self.variable
from collections import defaultdict
from abc import ABC , abstractmethod
class BankAccount (ABC):
    def __init__(self , holder  , amount ):
        self.holder = holder
        self.amount = amount
    @abstractmethod
    def deposit(self , x ):
        pass
    @abstractmethod
    def withdraw(self , x ):
        pass

    def Details(self ):
        print("name: " , self.holder )
        print("Amount: " , self.amount)
    
        
        
class CurrentAccount (BankAccount): # inheritance
    def __init__(self , amount , owner , overdraft ) :
        super().__init__(owner ,amount)
        self.overdraft = overdraft

    def withdraw(self,  x): #method overriding
        if( x <= self.amount + self.overdraft):
            self.amount -= x
    def deposit(self , amount):
        self.amount += amount

    def view_account_details(self , holder_name ):
        print("Current Account Details: ")
        if(self.holder == holder_name):
            self.Details()
        else:
            print("No Account under this holder name")

    def __add__(self , other): # Method overloading
        if(self.holder == other.holder):
            print(self.amount + other.amount)
        else:
            print(self.holder , " not having both accounts")




class SavingsAccount(BankAccount):
    def __init__(self , amount  , owner  , interest ):
        super().__init__(owner , amount)
        self.interest = interest
        self.amount += self.amount * interest / 100

    def withdraw(self,  x): #method overriding and abstraction 
        if( x <= self.amount):
            self.amount -= x
    def deposit(self , amount):
        self.amount += amount

    def view_account_details(self , holder_name ):
        print("Savings Account Details: ")
        if(self.holder == holder_name):
            self.Details()
            print("interset given: ", self.interest , "%")
        else:
            print("No Account under this holder name")
    

            
sList =[]
cList = []
s = SavingsAccount(24000 , "Nikhil Bhati" , 8)
c1 = CurrentAccount(784052, "Nikhil Bhati" , 2400)
c2 = CurrentAccount(100000, "Rishab Kumar" , 10000)
sList.append(s)
cList.append(c1)
cList.append(c2)

name = "Nikhil Bhati"
s.view_account_detials(name)
c2.view_account_detials("Rishab Kumar")

c2.__add__(s)



    
    



