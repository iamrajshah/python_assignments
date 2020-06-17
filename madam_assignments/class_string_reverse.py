class strin_reverse:
    def __init__(self, stringValue):
        self.stringValue = stringValue
    def stringReverse(self):
        return (' ').join((self.stringValue.split(' '))[::-1])

print(strin_reverse(input('Enter the string:')).stringReverse())