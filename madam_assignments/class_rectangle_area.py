class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width
    def area(self):
        return self.length * self.width

length, width = input('Enter length & width of rectangle:').split(',')
print(Rectangle(int(length), int(width)).area())