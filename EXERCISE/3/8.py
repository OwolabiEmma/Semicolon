numbers = []

for num in range(4):
    number = int(input(f'Enter an Integer {num + 1}: '))
    numbers.append(number)
    
total = sum(numbers)
average = total / len(numbers)
product = 1
for number in numbers:
    product *= number
maximum = max(numbers)
minimum = min(numbers)


print('\n\nSum:', total)
print('Average:', average)
print('Product:', product)
print('Largest:', maximum)
print('Smallest:', minimum)