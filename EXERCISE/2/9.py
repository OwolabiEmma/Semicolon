civ = ['B', 'C', 'D', 'b', 'c', 'd', '0', '1', '2', '$', '*', '+', ' ']
for char in civ:
    print(f"\n'{char}' = {ord(char)}")


civ = [66, 67, 68, 98, 99, 100, 48, 49, 50, 36, 42, 43, 32]
for char in civ:
    print(f"\n{char} = '{chr(char)}'")