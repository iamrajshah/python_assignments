def onlyVoewls(stringToCheck):
    countOfConsenent = 0
    vowels = ['a','e','i','o','u','A','E','I','O','U']
    for character in stringToCheck:
        if (character not in vowels):
            countOfConsenent+=1
    print('Number of consonent:', countOfConsenent)

onlyVoewls(input('Enter string:'))