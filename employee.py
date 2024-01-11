class Employee:
    def __init__(self,name,code,salary):
        self.name=name
        self.code=code
        self.salary=salary
    def display(self):
        print("-----------------------")
        print("Employee Name:",self.name,"\n","Employee code:",self.code,"\n","Employee salary:",self.salary)


n=input("Enter the name of employee:")
c=input("Enter the employee code:")
s=int(input("Enter the salary:"))

e1=Employee(n,c,s)
e1.display()