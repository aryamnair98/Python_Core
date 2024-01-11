class Animal:
  def speak(self):
    print("Animal speaking")
class Dog(Animal):
  def bark(self):
    print("Dog barking")
class Puppy(Dog):
  def eat(self):
    print("Eating bread...")

d=Dog()
d.speak()
d.bark()

print("..........................")
p=Puppy()
p.speak()
p.bark()
p.eat()