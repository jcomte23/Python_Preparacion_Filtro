print()
print(" __________________________")
print("|                          |")
print("|   Multiplication tables  |")
print("|__________________________|")
print()

for k in range(0, 11):
    print()
    print("Multiplication table => ", k)
    print()
    for i in range(1, 11, 1):
        print(i, '*', k, '=', i * k)
    