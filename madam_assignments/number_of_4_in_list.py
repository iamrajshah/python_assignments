def countNumberOf4InList(listOfNumbers):
    count = 0
    listOfNumbersAfterConversion = listOfNumbers.split(',')
    for element in listOfNumbersAfterConversion:
        if (int(element) == 4):
            count +=1
    print ('count:', count)

countNumberOf4InList(input('Enter list of integers seperated by comma:'))
