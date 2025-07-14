palindrome = int(input('Enter a five-digit Integer: '))

if 10000 <= palindrome <= 99999:
    
    num1 = palindrome // 10000
    num2 = (palindrome % 10000) // 1000
    num3 = (palindrome % 1000) // 100
    num4 = (palindrome % 100) // 10
    num5 = (palindrome % 10)
    
    if num1 == num5 and num2 == num4:
        print(f'\n{palindrome} is a Palindrome.')
    else:
        print(f'\n{palindrome} is not a Palindrome.')
else:
    print('\nPlease enter a valid five-digit Integer.')