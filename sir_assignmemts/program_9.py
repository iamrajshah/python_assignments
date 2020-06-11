def countNumberOf1s(number):
    tempNumber = number
    count = 0
    while (tempNumber > 0):
        tempNumber = tempNumber >> 1
        if (tempNumber & 1):
            count+=1
    print(count)

countNumberOf1s(int(input('Enter the number to count no.of 1\'s:')))