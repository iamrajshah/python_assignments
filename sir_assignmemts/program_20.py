def replaceStartForConsective(string1, character):
    print(string1[0] + string1[1:].replace(character, '*'))

string1 = input('Enter string:')
character = input('Enter character:')
replaceStartForConsective(string1, character)