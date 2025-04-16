
### Task 6:
#Create a `BankAccount` class that has deposit and withdraw methods with balance check.
class Bankaccount:
  
    def __init__(self,cash,balance):
        self.cash=cash
        self.balance=balance
    def deposit(self):

        print(f"please enter a cash to deposit {self.cash}")
        return self.balance + self.cash
    def widthdraw(self):
        print(f"please enter the case widthdraw {self.cash}")    
        return self.balance - self.cash
accountbalance=Bankaccount(1000,5000)
print("after deposit ",accountbalance.deposit())
print("after wwidthdraw",accountbalance.widthdraw())
   
   