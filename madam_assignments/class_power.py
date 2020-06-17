class customPowerOfN:
    def __init__(self, number, power):
        self.number = number
        self.power = power
    def findpower(self):
        return self.number**self.power
number = int(input('Enter the number:'))
power = int(input('Enter the power:'))
custom = customPowerOfN(number, power)
print(custom.findpower())