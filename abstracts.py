from abc import ABC,abstractmethod

class Shape(ABC):
    def area(self):
        print("Area of shape")

    def perimeter(self):
        print("Perimeter of shape")

class Circle(Shape):
  def __init__(self,radius):
    self.radius=radius

  def area(self):
    return 3.14*self.radius*self.radius
  def perimeter(self):
    return 2*3.14*self.radius

class Square(Shape):
  def __init__(self,side):
    self.side=side

  def area(self):
    return self.side*self.side
  
  def perimeter(self):
    return 4*self.side
  
c=Circle(2)
s=Square(4)

print("Area of circle:",c.area())
print("Perimeter of circle:",c.perimeter())

print("......................")

print("Area of square:",s.area())
print("Perimeter of square:",s.perimeter())