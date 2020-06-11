def toggleNBits(number, position, noOfBits):
    numberToMove = 2**noOfBits -1
    numberToMove = numberToMove << (position - noOfBits)
    print(number ^ numberToMove)

number = int(input('Enter number:'))
position = int(input('Enter position:'))
noOfBits = int(input('Enter no.of bits:'))
toggleNBits(number,position,noOfBits)


# Sample
# Input: 0000 1000 (8)
# Position: 4
# bits: 3
# 0000 0111
# 0000 1110
# Output: 0000 0110 (6)

# Input: 0001 0110 (22)
# Position: 4
# bits: 3
# 0000 0111
# 0000 1110
# Output: 0001 1000 (24)

# Input: 0001 1110 (30)
# Position: 4
# bits: 2
# (3) 0000 0011
# Left shift bu (2) 0000 1100
# XOR with original 0001 0010 (18)
