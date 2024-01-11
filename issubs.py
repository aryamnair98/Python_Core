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
print(issubclass(Calc3,Calc2))
print(issubclass(Calc3,Calc1))
print(issubclass(Calc1,Calc2))