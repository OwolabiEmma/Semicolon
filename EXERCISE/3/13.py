n = int(input('\nEnter a non-negative integer: '))

if n < 0:
    print('Factorial is not defined for negative integers.')
else:
    factorial = 1
    for i in range(1 , n + 1):
        factorial *= i
    print(f'\nThe factorial of {n} is {factorial}') 