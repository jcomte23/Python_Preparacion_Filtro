# Realizar un algoritmo que dado un número entero, visualice en pantalla si es par o impar.
# En el caso de ser 0. debe visualizar "el numero no es par ni impar"

# Pedir un número entero al usuario
numero = int(input("Ingrese un número entero: "))

# Verificar si el número es cero
if numero == 0:
    print("El número no es par ni impar")
# Verificar si el número es par
elif numero % 2 == 0:
    print("El número es par")
# Si no es cero y no es par, entonces es impar
else:
    print("El número es impar")
