print()
print(" ___________________________")
print("|                           |")
print("|   Imprimidor de Numeros   |")
print("|___________________________|")
print()

try:
    tope=int(input("Indica hasta que numero quieres imprimir => "))
    
    if tope<=0:
        print("El numero debe ser superior a 0")

    for i in range(1,tope):
        print(f" - {i}")
except:
    print(" ________________________________________________")
    print("|                                                |")
    print("|    / \                                         |")
    print("|   / | \    Ingresate un dato no permitido      |")
    print("|  /  *  \                                       |")
    print("| /_______\                                      |")
    print("|________________________________________________|")    
        
