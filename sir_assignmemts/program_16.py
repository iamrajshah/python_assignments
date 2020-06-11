def printPrimeInRange(rangeOfPrime):
    isPrime = 0
    for number in range(2, rangeOfPrime+1):
        j = number//2
        isPrime = 0
        while(j>1):
            if number % j == 0:
                isPrime = 1
                break
            j-=1
            isPrime = 0
        if(isPrime == 0):
            print('prime:',number)
            isPrime = 1

def isPrime(number):
    compositor = number//2
    isPrime = 0
    while compositor > 1:
        if number == 1:
            return False
        elif number % compositor == 0:
            isPrime = 1
        break
        compositor -= 1
        isPrime = 0
    if isPrime == 0:
        isPrime = 1
    return True


def getPrimeNumbersInRange(lowerBound, upperBound):
    primeNumbers = []

    if lowerBound < upperBound:
        for number in range(lowerBound, upperBound, 1):
            if isPrime(number):
                primeNumbers.append(number)
                print('Prime numbers are: ', primeNumbers)
            else:
                print('Enter valid range!')


# printPrimeInRange(int(input('Enter range to print prime no:')))
getPrimeNumbersInRange(1,10)