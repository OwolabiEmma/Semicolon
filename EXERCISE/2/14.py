# Target Heart-Rate calculator

age = int(input('Enter your age: '))

maximum_heart_rate = 220 - age

lower_heart_rate = 0.50 * maximum_heart_rate
upper_heart_rate = 0.85 * maximum_heart_rate

print('Your maximum heart rate is: ',maximum_heart_rate)
print(f"Range of the user's heart is: {lower_heart_rate} to {upper_heart_rate}")