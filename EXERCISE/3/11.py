
total_miles = 0.0
total_gallons = 0.0


while True:
    gallons = float(input("\nEnter the gallons used (-1 to end): "))
    
    if gallons == -1:
        break
    

    miles = float(input("\nEnter the miles driven: "))
    
    mpg = miles / gallons
    print(f"\nThe miles/gallon for this tank was {mpg:.6f}")
    
    
    total_miles += miles
    total_gallons += gallons

if total_gallons > 0:
    overall_mpg = total_miles / total_gallons
    print(f"\nThe overall average miles/gallon was {overall_mpg:.6f}")
else:
    print("No fuel usage data entered.")