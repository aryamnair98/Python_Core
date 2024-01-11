class BankAccount:
    def __init__(self,accno,bal):
        self.accno=accno
        self.bal=bal
    def display(self):
         print("Account number:",self.accno)
    def deposit(self,amount):
            print("Current balance:",self.bal)
            self.bal=self.bal+amount
            
            print("Depositing amount:",amount)
            print("After Depositing amount,current bal is:",self.bal)
    def withdraw(self, amount):
        if amount <= self.bal:
            self.bal=self.bal- amount
            print("withdrawed",amount,"and the balance  is:",self.bal)
        else:
            print("Insufficient balance")
        
class SavingsAccount(BankAccount):
    def __init__(self, accno, bal, interest):
        super().__init__(accno, bal)
        self.interest= interest

    def add_interest(self):
        s_interest = self.bal * self.interest
        self.bal += s_interest
        print("Added",s_interest ,"interest and new bal is:",self.bal)

class CheckingAccount(BankAccount):
    def __init__(self, accno, bal, overdraft_limit=100):
        super().__init__(accno, bal)
        self.overdraft_limit = overdraft_limit

    def withdraw(self, amount):
        if amount <= self.bal + self.overdraft_limit:
            super().withdraw(amount)
        else:
            print("Crosses overdraft limit")

s=SavingsAccount(12345,500,2)
s.deposit(200)
s.withdraw(100)
s.add_interest()

c=CheckingAccount(5678,800)
c.deposit(200)
c.withdraw(300)