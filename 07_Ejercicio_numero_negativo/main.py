#Diseñar un algoritmo que pida por teclado tres números;
#Si el primero es negatico, debe imprimir el producto de los tres y si no lo es,
#Imprimirá la suma

# Pedir tres números por teclado
num1 = int(input("Ingrese el primer número: "))
num2 = int(input("Ingrese el segundo número: "))
num3 = int(input("Ingrese el tercer número: "))

# Verificar si el primer número es negativo
if num1 < 0:
    # Calcular el producto de los tres números
    producto = num1 * num2 * num3
    print("El producto de los tres números es:", producto)
else:
    # Calcular la suma de los tres números
    suma = num1 + num2 + num3
    print("La suma de los tres números es:", suma)