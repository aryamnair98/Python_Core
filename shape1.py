class Shape:
  def __init__(self,name,color):
    self.name=name
    self.color=color

  def display(self):
    print("Shape is:",self.name)
    print("Color of",self.name,"is:",self.color)

class Circle(Shape):
  def __init__(self,name,color,radius):
    super().__init__(name, color)
    self.radius=radius

  def area_perimeter(self):
    print("Area of circle is:",(3.14*self.radius**2))
    print("Perimeter of circle is:",(2*3.14*self.radius))

class Square(Shape):
  def __init__(self,name,color,side):
    super().__init__(name, color)
    self.side=side

  def area_perimeter(self):
    print("Area of square is:",(self.side**2))
    print("Perimeter of square is:",(4*self.side))

class Rectangle(Shape):
  def __init__(self,name,color,length,width):
    super().__init__(name, color)
    self.length=length
    self.width=width

  def area_perimeter(self):
    print("Area of rectangle is:",(self.length*self.width))
    print("Perimeter of rectangle is:",(2*(self.length+self.width)))

c=Circle("Circle","Red",2.5)
c.display()
c.area_perimeter()

print("................................................")
s=Square("Square","Yellow",5)
s.display()
s.area_perimeter()

print("................................................")
r=Rectangle("Rectangle","Black",8,6)
r.display()
r.area_perimeter()

