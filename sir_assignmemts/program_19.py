def replaceMiddlePart(stringInput):
    print(''.join([stringInput[0:len(stringInput) // 2 - 1], stringInput[len(stringInput) // 2 + 1:] ]))

replaceMiddlePart(input('Enter String:'))