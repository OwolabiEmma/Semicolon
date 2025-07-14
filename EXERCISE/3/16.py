
largest = second_largest = float('-inf')

for i in range(1, 11):
    number = float(input(f"Enter number {i}: "))

    if number > largest:
        second_largest = largest
        largest = number
    elif number > second_largest:
        second_largest = number

print(f"The largest number is: {largest}")
print(f"The second largest number is: {second_largest}")