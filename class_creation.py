class Person:
    def __init__(self,name,age): #parameterized constructor
        self.name=name
        self.age=age
    def display(self):
        print("Name is",self.name,"Age is",self.age)

p1=Person("Arya",25) #object creation by passing parameters
p1.display() #function call



class Person:
    def __init__(self): #non-parameterized constrctor
        print("Welcome to python")
    def display(self,name,age):
        self.name=name
        self.age=age
        print("My name is",self.name,"and my age is",self.age)

p1=Person() #object creation
p1.display("Idhitri",1) #function calling with parameters


class Person: #here it creates default constructor
    def display(self,name,age):
        self.name=name
        self.age=age
        print("My name is",self.name,"and my age is",self.age)

p1=Person() #object creation
p1.display("Amal",31) #function calling with parameters
        