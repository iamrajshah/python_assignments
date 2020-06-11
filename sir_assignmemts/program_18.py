# WaP to accept string from user and perform the below operation:
# Ex:	Input: aabbbbbcccddaaaaa
# 	Output: a2b5c3d2a5

def printCharacterAndOccurance(inputString):
    stringOfCharacter = ''
    previousCharacter=''
    count = 0
    for character in inputString:
        if previousCharacter == '':
            previousCharacter = character
        if previousCharacter != character:
            stringOfCharacter=stringOfCharacter + previousCharacter +str(count)
            count = 1
            previousCharacter = character
        else:
            count=count+1
    stringOfCharacter=stringOfCharacter + previousCharacter +str(count)
    print(stringOfCharacter)   

printCharacterAndOccurance('aabbbbbcccddaaaaa')