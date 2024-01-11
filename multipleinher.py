class Calc1:
    def sum(self,a,b):
        return a+b
class Calc2:
    def multiplication(self,a,b):
        return a*b
class Calc3(Calc1,Calc2):
    def division(self,a,b):
        return a/b
    
c=Calc3()
print(c.sum(10,20))
print(c.multiplication(10,20))
print(c.division(10,20))