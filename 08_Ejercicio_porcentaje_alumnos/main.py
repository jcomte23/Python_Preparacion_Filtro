#Un colegio desea saber qué porcentaje de niños y que porcentaje de niñas hay en el curso actual. 
#Diseñar un algoritmo para este proposito.

# Pedir la cantidad de niños y niñas en el curso
num_ninos = int(input("Ingrese la cantidad de niños en el curso: "))
num_ninas = int(input("Ingrese la cantidad de niñas en el curso: "))

# Calcular el total de estudiantes en el curso
total_estudiantes = num_ninos + num_ninas

# Calcular el porcentaje de niños y niñas
porcentaje_ninos = (num_ninos / total_estudiantes) * 100
porcentaje_ninas = (num_ninas / total_estudiantes) * 100

# Imprimir los resultados
print ("Porcentaje de niños en el curso:", porcentaje_ninos, "%")
print ("Porcentaje de niñas en el curso:", porcentaje_ninas, "%")