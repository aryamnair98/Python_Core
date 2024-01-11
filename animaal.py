class Animal:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display(self):
        print("Name:",self.name)
        print("Age: ",self.age,"years")


class Mammal(Animal):
    def __init__(self, name, age, fur_color):
        super().__init__(name, age)
        self.fur_color = fur_color

    def give_birth(self):
        print("Fur color is:",self.fur_color)
        print(self.name,"is giving birth to live offsprings")


class Bird(Animal):
    def __init__(self, name, age, feather_color):
        super().__init__(name, age)
        self.feather_color = feather_color

    def bird_birth(self):
        print("Feather Color is:",self.feather_color)
        print(self.name,"is laying eggs for giving birth to new birds")


class Fish(Animal):
    def __init__(self, name, age,color):
        super().__init__(name, age)
        self.color = color

    def swim(self):
        print("Color is:",self.color)
        print(self.name," is aquatic oraganisms and swimming in fresh water")


m=Mammal("Lion",2,"Orange")
m.display()
m.give_birth()

print(".......................................")
b=Bird("Crow",1,"Black")
b.display()
b.bird_birth()

print(".......................................")
f=Fish("White moly",1.5,"White")
f.display()
f.swim()