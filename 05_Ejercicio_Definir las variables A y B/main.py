#Dados dos variables numéricas A y B, se pide realizar un algoritmo que intercambie los valores de ambas variables
#y muestre cuánto valen al final las dos variables.

# Definir las variables A y B
A = int(input("Ingresa el valor de A: "))
B = int(input("Ingresa el valor de B: "))

# Mostrar los valores iniciales
print("Valores iniciales:")
print("A =", A)
print("B =", B)

# Intercambiar los valores de A y B
temp = A
A = B
B = temp

# Mostrar los valores finales
print("Valores finales:")
print("A =", A)
print("B =", B)