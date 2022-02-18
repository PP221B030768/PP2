import math
class Point:
    x = y = 0
    def __init__(self,x,y):
        self.x = x
        self.y = y
    def show(self):
        print(self.x,self.y)
    def move(self,x,y):
        self.x += x
        self.y += y
        print(self.x,self.y)
    def dist(self,b):
        return math.sqrt((self.x-b.x)**2+ (self.y-b.y)**2)
a = Point(int(input()), int(input()))
a1 = Point(1, 1)
a.show()
a1.move(1, 1)
print(a.dist(a1))