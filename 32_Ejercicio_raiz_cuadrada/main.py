print()
print(" ________________")
print("|                |")
print("|   Square root  |")
print("|________________|")
print()

number = int(input("enter an integer=>"))
result = 0

while result ** 2 < number:
    print(result)
    result += 1

if result ** 2 == number:
    print(f"The square root of {number} is {result}")
else:
    print(f"The number {number} doesn't have a square root")
