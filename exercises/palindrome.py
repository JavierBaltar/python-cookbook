#checks if given string is a palindrome

def palindrome(string):
    reverseString = string[::-1]
    if string == reverseString:
        print('String is a palindrome')
    else:
        print('String is not a palindrome')

if __name__ == '__main__':
    userInput = str(input('Enter a string to check for Palindrome: '))
    palindrome(userInput)
