def numberThreeSum(number1,number2,number3):
    if (number1 == number2 or number2 == number3 or number1 == number3):
        print('Sum is:', 0)
    else:
        print('Sum is:', number1 + number2 + number3)

number1 = int(input('Enter number1:'))
number2 = int(input('Enter number2:'))
number3 = int(input('Enter number3:'))
numberThreeSum(number1, number2, number3)