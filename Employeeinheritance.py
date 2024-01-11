class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def display(self):
        print("Name:",self.name)
        print("Salary:",self.salary)
class Manager(Employee):
    def __init__(self, name, salary, num_subordinates):
        super().__init__(name, salary)
        self.num_subordinates = num_subordinates

    def m_display(self):
        print("Number of Subordinates:",self.num_subordinates)

class Developer(Employee):
    def __init__(self, name, salary, programming_languages):
        super().__init__(name, salary)
        self.programming_languages = programming_languages

    def d_display(self):
        print("Programming Languages:")
        for i in self.programming_languages:
            print(i)

m = Manager("Arya M Nair", 80000, 5)
m.display()
m.m_display()

d=Developer("Arya Amal",56000,["Python","java","DBMS"])
d.display()
d.d_display()
