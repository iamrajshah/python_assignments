def add(*params):
    sumOfNumber = 0
    for element in params:
        sumOfNumber += element
    print('sumOfNumber:', sumOfNumber)

print('Enter two number for addition')
number1 = int(input())
number2 = int(input())
add(number1, number2)

print('Enter three number for addition')
number1 = int(input())
number2 = int(input())
number3 = int(input())
add(number1, number2, number3)

print('Enter four number for addition')
number1 = int(input())
number2 = int(input())
number3 = int(input())
number4 = int(input())
add(number1, number2, number3, number4)

print('Enter five number for addition')
number1 = int(input())
number2 = int(input())
number3 = int(input())
number4 = int(input())
number5 = int(input())
add(number1, number2, number3, number4, number5)
