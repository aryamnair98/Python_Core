class Shape:
    def calc_area(self):
        pass
class Circle(Shape):
    def calc_area(self,radius):
        self.radius=radius
        print("Area of circle is:",(3.14*self.radius**2))
class Rectangle(Shape):
    def calc_area(self,length,width):
        self.length=length
        self.width=width
        print("Area of rectangle is:",(self.length*self.width))

c=Circle()
c.calc_area(3.4)
r=Rectangle()
r.calc_area(5,6)
