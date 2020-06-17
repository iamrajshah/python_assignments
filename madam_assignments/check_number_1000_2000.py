def checkNumberIn1000(inputNumber):
    return (abs(1000 - inputNumber) <= 100) or (abs(2000 - inputNumber) <= 100)

print(checkNumberIn1000(int(input('Enter number:'))))