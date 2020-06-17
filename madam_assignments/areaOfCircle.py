class Circle:
    def __init__(self, radius):
        self.radius = radius
        self.piValue = 3.14
    def areaOfCircle(self):
        return self.piValue * self.radius ** 2
    def perimeterOfCircle(self):
        return 2 * self.piValue * self.radius

radiusOfCircle = float(input('Enter the radius of circle:'))
circleInstance = Circle(radiusOfCircle)
print(circleInstance.areaOfCircle())
print(circleInstance.perimeterOfCircle())

# class Circle(object):
#     def __init__(self, radius):
#         self.radius = radius

#     def area(self):
#         return float(3.14  self.radius * 2)

#     def parameter(self):
#         return float(2*.14*self.radius)


# radius = float(input('Enter radius: '))
# print('Area and parameter of circle of radius', radius, 'is',
#       Circle(radius).area(), Circle(radius).parameter())