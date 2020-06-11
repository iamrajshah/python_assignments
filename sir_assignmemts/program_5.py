def turnOnGivenBit(number, bit, numberOfBit):
    modifiedNumber = 1<<bit-1
    numberOfBitToChange= 2**numberOfBit - 1
    numberToCheck = numberOfBitToChange << (bit - numberOfBit)
    print(number | numberToCheck)


number = int(input('Enter the number:'))
bitPosition = int(input('Enter the bit-position to turned on:'))
numberOfBits = int(input('Enter the number of bit:'))
turnOnGivenBit(number, bitPosition, numberOfBits)
