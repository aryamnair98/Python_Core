class Bank:
    def rate_of_interest(self):
        return 10
    
class SBI(Bank):
    def rate_of_interest(self):
        return 7
    
class ICICI(Bank):
    def rate_of_interest(self):
        return 8
    
b1=Bank()
b2=SBI()
b3=ICICI()

print("Bank interest rate:",b1.rate_of_interest())
print("SBI interest rate:",b2.rate_of_interest())
print("ICICI interest rate:",b3.rate_of_interest())