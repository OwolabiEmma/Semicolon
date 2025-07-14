num = int(input('Enter a five-digit Integer: '))

if 10000 <= num <= 99999:
    divisor = 10000
    
    while divisor >= 1:
        digit = num // divisor
        print(digit, end = ' ')
        num %= divisor
        divisor //= 10
        
else:
    print('Please enter a valid five-digit integer.')