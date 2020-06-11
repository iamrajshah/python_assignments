def patternA(numberOfLines):
    for i in range(numberOfLines+1):
        j=1
        while(j<=i):
            print(j, end='\t')
            j=j+1
        print()

def patternB(numberOfLines):
    for i in range(numberOfLines+1):
        character = 97
        j=1
        while(j<=i):
            print(chr(character), end='\t')
            character=character+1
            j=j+1
        print()

def patternC(numberOfLines):
    for i in range(numberOfLines+1):
        j=numberOfLines - i
        k=i    
        while(k>0):
            print(end='\t')
            k=k-1
        while(j > 0):
            print(end='\t')
            print('*', end='\t')
            j=j-1
        print()

def patternD(numberOfLines):
    for i in range(numberOfLines +1):
        j=i
        while (j>=0):
            print('*', end='\t')
            j=j-1
        print()

def patternE(numberOfLines):
    for i in range(numberOfLines):
        j=numberOfLines - i
        while(j>=0):
            print(end='\t')
            j=j-1
        k=i
        while(k>=0):
            print('*', end='\t\t')
            k=k-1
        print()


# patternA(4)
# print()
# patternB(3)
# print()
# patternC(4)
# print()
# patternD(4)
# print()
# patternE(4)