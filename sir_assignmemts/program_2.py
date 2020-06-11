def turnOffGivenBit(number, bit):
    modifiedNumber = 1<<bit-1
    print(number & ~modifiedNumber)


number = int(input('Enter the number:'))
bitPosition = int(input('Enter the bit-position to turned off:'))
turnOffGivenBit(number, bitPosition)