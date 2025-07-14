num1 = int(input('Enter the First Integer: '))
num2 = int(input('Enter the Second Integer: '))
num3 = int(input('Enter the Third Integer: '))

numbers = [num1, num2, num3]

total = sum(numbers)
average = total / 3
product = num1 * num2 * num3
minimum = min(numbers)
maximum = max(numbers)

print('\nSum:', total)
print('Average:', average)
print('Product:', product)
print('Largest:', maximum)
print('Smallest:', minimum)
