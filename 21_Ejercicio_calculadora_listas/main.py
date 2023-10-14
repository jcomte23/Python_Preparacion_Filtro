def sumar(numeros):
    suma_total = sum(numeros)
    return suma_total

def restar(numeros):
    resta_total = numeros[0]
    for num in numeros[1:]:
        resta_total -= num
    return resta_total

def multiplicar(numeros):
    producto_total = 1
    for num in numeros:
        producto_total *= num
    return producto_total

def dividir(numeros):
    if 0 in numeros[1:]:
        return "Error: No se puede dividir por cero."
    else:
        resultado = numeros[0]
        for num in numeros[1:]:
            resultado /= num
        return resultado

flag = True
while flag:
    print("===========================")
    print("=========CALCULADORA=======")
    print("===========================")
    print("1. Sumar")
    print("2. Restar")
    print("3. Multiplicar")
    print("4. Dividir")
    print("5. Salir")

    opcion = input("Ingresa el número de la opción que deseas: ")

    if opcion == '5':
        break

    if opcion in ('1', '2', '3', '4'):
        numeros = []
        while True:
            try:
                num = float(input("Ingresa un número (o ingresa 0 para terminar): "))
                if num == 0:
                    break
                numeros.append(num)
            except ValueError:
                print("Ingresa un número válido.")
        
        if opcion == '1':
            resultado = sumar(numeros)
            print(f"El resultado de la suma es: {resultado}")
        elif opcion == '2':
            resultado = restar(numeros)
            print(f"El resultado de la resta es: {resultado}")
        elif opcion == '3':
            resultado = multiplicar(numeros)
            print(f"El resultado de la multiplicación es: {resultado}")
        elif opcion == '4':
            resultado = dividir(numeros)
            print(f"El resultado de la división es: {resultado}")
    else:
        print("Opción no válida. Por favor, selecciona una opción válida (1-5).")
        
    break