print()
print(" _______________________")
print("|                       |")
print("|   Calculadora basica  |")
print("|_______________________|")
print()

try:
    numero1=int(input("Ingresa el primer numero =>"))
    numero2=int(input("Ingresa el segundo numero =>"))

    print("Elige la operacion")
    print(" [1] Sumar")
    print(" [2] Restar")
    print(" [3] Multiplicar")
    print(" [4] Dividir")

    opcion=int(input("OPCION=> "))

    if(opcion==1):
        print(f"{numero1} + {numero2} = {numero1+numero2}")
    elif(opcion==2):
        print(f"{numero1} - {numero2} = {numero1-numero2}")
    elif(opcion==3):
        print(f"{numero1} * {numero2} = {numero1*numero2}")
    elif(opcion==4):
        print(f"{numero1} / {numero2} = {numero1/numero2}")
    else:
        print("Ingresate una opcion incorrecta")
except:
    print(" ________________________________________________")
    print("|                                                |")
    print("|    / \                                         |")
    print("|   / | \    Ingresate un dato no permitido      |")
    print("|  /  *  \                                       |")
    print("| /_______\                                      |")
    print("|________________________________________________|") 