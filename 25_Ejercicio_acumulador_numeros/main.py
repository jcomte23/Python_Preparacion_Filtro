print()
print(" ________________________")
print("|                        |")
print("|   Sumador de Numeros   |")
print("|________________________|")
print()

try:
    tope=int(input("Indica hasta que numero quieres imprimir => "))
    
    if tope<=0:
        print("El numero debe ser superior a 0")
    acumulador=0
    for i in range(1,(tope+1)):
        acumulador=acumulador+i
    print(f"Sumando los numero da un acumulador de {acumulador}")    
except:
    print(" ________________________________________________")
    print("|                                                |")
    print("|    / \                                         |")
    print("|   / | \    Ingresate un dato no permitido      |")
    print("|  /  *  \                                       |")
    print("| /_______\                                      |")
    print("|________________________________________________|")    