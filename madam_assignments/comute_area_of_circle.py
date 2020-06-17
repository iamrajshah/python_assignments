def computeAreaOfCircle(radius):
    piValue = 3.14
    areaOfCircle = radius**2 * piValue
    return areaOfCircle

print(computeAreaOfCircle(float(input('Enter radius of circle:'))))