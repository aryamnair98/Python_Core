class Person:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def display(self):
        print("Name:",self.name)
        print("Age:",self.age)
class Employee(Person):
    def __init__(self, name, age,empid):
        super().__init__(name, age)
        self.empid=empid
    def display(self):
        print("Name:",self.name)
        print("Age:",self.age)
        print("Employee id:",self.empid)

n=input("Enter employee name:")
a=int(input("Enter age:"))
eid=int(input("Enter employee id:"))
p=Person(n,a)
p.display()
em=Employee(n,a,eid)
em.display()

