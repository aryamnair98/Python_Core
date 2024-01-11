class BankAccount:
    def __init__(self,accountno,accountholder,balance):
        self.accountno=accountno
        self.accountholder=accountholder
        self.balance=balance
    
    def deposit(self,amount):
        self.balance += amount
    
    def withdraw(self,amount):
        if amount<=self.balance:
            self.balance -= amount
        else:
            print("Insufficient balance")
    def displaybalance(self):
        print("Account number:",self.accountno)
        print("Account Holder:",self.accountholder)
        print("Balance:",self.balance)
    
class SavingsAccount(BankAccount):
    def __init__(self, accountno, accountholder, balance,interestrate):
        super().__init__(accountno, accountholder, balance)
        self.interestrate=interestrate
    def deposit(self, amount):
        super().deposit(amount)
        self.calculateinterest()
    def calculateinterest(self):
        interest=self.balance * (self.interestrate / 100)
        super().deposit(interest)

class CurrentAccount(BankAccount):
    def __init__(self, accountno, accountholder, balance,overdraftlimit):
        super().__init__(accountno, accountholder, balance)
        self.overdraftlimit=overdraftlimit
    def withdraw(self, amount):
        if amount <= self.balance + self.overdraftlimit:
            self.balance -= amount
        else:
            print("Exceeds overdraft limit")


sa=SavingsAccount("AC123","Arya",1000,2)
sa.deposit(500)
sa.calculateinterest()
sa.withdraw(200)
sa.displaybalance()

ca=CurrentAccount("AC456","Amal",2000,500)
ca.withdraw(1500)
ca.displaybalance()
    