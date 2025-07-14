p = 1000
r = 0.07

print(f'\n{"Year":<5}{"Amount":>15}')
for year in range(1,31):
    amount = p * (1 + r) ** year
    print(f"{year:<5} {amount:>15.2f}")


