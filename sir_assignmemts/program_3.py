def turnOffGivenBit(number, bit, numberOfBit):
    modifiedNumber = 1<<bit-1
    numberOfBitToChange= 1<<bit - numberOfBit
    numberToCheck = modifiedNumber | numberOfBitToChange
    print(number & ~numberToCheck)


number = int(input('Enter the number:'))
bitPosition = int(input('Enter the bit-position to turned off:'))
numberOfBits = int(input('Enter the number of bit:'))
turnOffGivenBit(number, bitPosition, numberOfBits)

#number:0000 1101 (13)
#bit position: 4
#no.of bits: 2

#O/P:
#0000 0001 (1)