class Shape():
    def __init__(self):
        pass
    def Area(self):
        return 0
class Square(Shape):
    def __init__(self, length):
        Shape.__init__(self)
        self.length = length
    def Area(self):
        return self.length*self.length

s = Square(int(input()))
print(s.Area())