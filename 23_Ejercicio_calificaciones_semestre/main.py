print()
print(" _____________________________")
print("|                             |")
print("|   Calificaciones semestre   |")
print("|_____________________________|")
print()

try:
    # Pedir al estudiante que ingrese sus calificaciones del parcial y del trabajo
    calificacion_parcial = float(input("Ingresa la calificación del parcial (0.0 - 5.0): "))
    calificacion_trabajo = float(input("Ingresa la calificación del trabajo (0.0 - 5.0): "))

    # Verificar si las calificaciones ingresadas están en el rango correcto (0.0 - 5.0)
    if 0.0 <= calificacion_parcial <= 5.0 and 0.0 <= calificacion_trabajo <= 5.0:
        # Calcular el promedio ponderado
        promedio_ponderado = (calificacion_parcial * 0.8) + (calificacion_trabajo * 0.2)

        # Verificar si el estudiante aprueba o no el semestre
        if promedio_ponderado >= 3.0:
            print(f"El estudiante aprueba el semestre con un promedio ponderado de {promedio_ponderado:.2f}")
        else:
            print(f"El estudiante no aprueba el semestre con un promedio ponderado de {promedio_ponderado:.2f}")
    else:
        print("Por favor, ingresa calificaciones válidas en el rango de 0.0 a 5.0.")
except:
    print(" ________________________________________________")
    print("|                                                |")
    print("|    / \                                         |")
    print("|   / | \    Ingresate un dato no permitido      |")
    print("|  /  *  \                                       |")
    print("| /_______\                                      |")
    print("|________________________________________________|")


