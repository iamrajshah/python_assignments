def printReverseWithSpace(firstName, lastName):
    return (' ').join([firstName[::-1], lastName[::-1]])

firstName = input('Enter first name:')
lastName = input('Enter last name:')
print(printReverseWithSpace(firstName, lastName))