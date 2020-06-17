class ProductOrSum:
    def __init__(self, number1, number2):
        self.number2 = number2
        self.number1 = number1
    def returnProductOrSum(self,number1, number2):
        productResult = self.number1 * self.number2
        if productResult > 100:
            return self.number2 + self.number1
        else:
            return productResult

number1 = int(input('Enter number1:'))
number2 = int(input('Enter number2:'))
print(ProductOrSum(number1, number2).returnProductOrSum(number1, number2))