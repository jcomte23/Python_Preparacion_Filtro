print()
print(" ___________________________")
print("|                           |")
print("|   Cantidad pares 4 a 200  |")
print("|___________________________|")
print()
cantidad=0
for i in range(4,201):
    if(i%2==0):
        cantidad+=1
print(f"Entre 4 y 200 hay {cantidad} numeros pares")