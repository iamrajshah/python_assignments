def replaceSubstring(string1, string2):
    print(' '.join([string2[0:2] + string1[2:], string1[0:2] + string2[2:]]))

string1 = input('Enter first string:')
string2 = input('Enter second string:')
replaceSubstring(string1, string2)