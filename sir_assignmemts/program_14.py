# special program

def factorial(number):
    if (number == 0):
        return 1
    else:
        return number * factorial(number - 1)

def checkIfItIsSpecialNumber(number):
    tempNumber = number
    sumOfFactorial = 0
    reminder = 0
    while(tempNumber > 0):
        reminder = tempNumber % 10
        sumOfFactorial += factorial(reminder)
        tempNumber //= 10
    if(number == sumOfFactorial):
        print(number, ' is special')
    else:
        print(number, ' is not special')


checkIfItIsSpecialNumber(int(input('Enter number to check special number:')))

