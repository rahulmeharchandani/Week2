import math
class rectangle():
    def __init__(self,length,breadth):
        self.length=length
        self.breadth=breadth
        
    def area(self):
        return self.length * self.breadth
        
class circle():
    def __init__(self,radius):
        self.radius=radius
        
    def area(self):
        return 3.14*self.radius**2
        
        
rect=rectangle(7,14)
circ=circle(9)
print(f"Area of rectangle = ",rect.area())
print(f"Area of circle = ",circ.area())
                    
            