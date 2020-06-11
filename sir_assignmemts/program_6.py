def toggleBit(number, position):
    modifiedNumber = 1<< position -1
    print(number ^ modifiedNumber)


number = int(input('Enter number:'))
position = int(input('Enter bit position to toggle:'))

toggleBit(number, position)


# Sample
# Input 0000 1010 (10)
# Bit to toggle: 2
# Output: 0000 1000 (8)

# Input 0000 1010 (10)
# Bit to toggle: 3
# Output: 0000 1110 (14)