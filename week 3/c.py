class Shape():
    def __init__(self):
        pass
    def Area(self):
        return 0
class Rectangle(Shape):
    def __init__(self, length, width):
        Shape.__init__(self)
        self.length = length
        self.width = width
    def Area(self, length, width):
        return self.length*self.width
    
a = int(input())
b = int(input())
rect = Rectangle(a,b)
print(rect.Area(a, b))