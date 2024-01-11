class Animal:
    def __init__(self,name):
        self.name=name

    def makesound(self):
        print(self.name,"makes generial animal sound")
class Dog(Animal):
    def makesound(self):
        print(self.name,"makes bow bow sound")

class Dog(Animal):
    def makesound(self):
        print(self.name,"makes meow meow sound")


myDog=Animal("Puppy")
myCat=Animal("Kathu")

def animalsound(animal):
    animal.makesound()

animalsound(myDog)
animalsound(myCat)
        
