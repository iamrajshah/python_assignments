def isPalindrome(number):
    numberToPerformed = number
    reminder = 0
    sumOfNumber = 0
    while(numberToPerformed > 0):
        reminder = numberToPerformed % 10
        sumOfNumber = sumOfNumber*10 + reminder
        numberToPerformed=int(numberToPerformed/10)
    if (sumOfNumber == number):
        print(number,' is palindrome')
    else:
        print(number,' is not palindrome')

isPalindrome(int(input('Enter a number to check palindrome:')))