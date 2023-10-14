def promedio_notas():
    cantidad_notas = int(input("Ingrese la cantidad de notas: "))
    
    total_notas = 0
    for i in range(cantidad_notas):
        nota = float(input(f"Ingrese la nota {i+1}: "))
        total_notas += nota
    
    promedio = total_notas / cantidad_notas
    print("El promedio de las notas es:", promedio)

promedio_notas()