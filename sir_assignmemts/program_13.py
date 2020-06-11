def printFibonacciSeries(number):
    sumation = 1
    secondPrevious = 0
    previous = 1
    if(number == 1):
        print('1')
    if(number == 2):
        print('1 \t 1')
    elif (number > 2):
        print(sumation, end='\t')
        for i in range(1,number,1):
            sumation = secondPrevious + previous
            print(sumation, end='\t')
            secondPrevious = previous
            previous = sumation

printFibonacciSeries(int(input('Enter the lenth you want for fibonacci series:')))