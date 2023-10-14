def leer_datos(municipios):

    while True:
        
        nombre = input("Ingrese el nombre del municipio: ")
        toneladas = float(input("Ingrese la cantidad de toneladas de residuos/día: "))
        olor = float(input("Ingrese el porcentaje de influencia de olores ofensivos: "))
        asentamiento = float(input("Ingrese el porcentaje de creación de asentamientos ilegales: "))
        contaminacion = float(input("Ingrese el porcentaje de contaminación de corrientes hídricas: "))

        if olor + asentamiento + contaminacion != 100:
            print("Los porcentajes deben sumar 100.")
            return
        
        nuevo_municipio = [
            nombre, #[0]
            toneladas, #[1]
            olor,#[2]
            asentamiento, #[3]
            contaminacion #[4]
        ]

        municipios.append(nuevo_municipio)
        print("Municipio",nuevo_municipio[0]," agregado correctamente")

        seguir = input("Deseas agregar otro municipio?: (Si o No)").lower()

        if seguir == "si":
            continue
        else:
            break

def municipio_mas_toneladas(municipios):
    if not municipios:
        print("No hay datos disponibles.")
        return
    
    max_toneladas = 0
    nombre_max_toneladas = ''
    
    for municipio in municipios:
        if municipio[1] > max_toneladas:
            max_toneladas = municipio[1]
            nombre_max_toneladas = municipio[0]
            
    print("\nEl municipio que más toneladas/día genera es",nombre_max_toneladas,"con",max_toneladas,"toneladas.\n")


def municipio_menos_toneladas(municipios):
    if not municipios:
        print("No hay datos disponibles.")
        return
    
    min_toneladas = float('inf')# Usamos infinito para asegurarnos de encontrar el mínimo
    nombre_min_toneladas = ''
    
    for municipio in municipios:
        if municipio[1] < min_toneladas:
            min_toneladas = municipio[1]
            nombre_min_toneladas = municipio[0]
    
    print("\nEl municipio que menos toneladas/día genera es",nombre_min_toneladas,"con",min_toneladas,"toneladas.\n")

def promedio_toneladas_dia(municipios):
    if not municipios:
        print("No hay datos disponibles.")
        return
    
    total_toneladas = 0
    total_municipios = len(municipios)
    
    for municipio in municipios:
        total_toneladas += municipio[1]
        
    promedio = total_toneladas / total_municipios
    print("\nEl promedio de toneladas de basura por día en todos los municipios es",promedio, "toneladas.\n")


def promedio_toneladas_mes(municipios):
    if not municipios:
        print("No hay datos disponibles.")
        return
    
    total_toneladas = 0
    total_municipios = len(municipios)
    
    for municipio in municipios:
        total_toneladas += municipio[1]
        
    promedio_dia = total_toneladas / total_municipios
    promedio_mes = promedio_dia * 30  # Asumiendo un mes de 30 días
    
    print("\nEl promedio de toneladas de basura por mes en todos los municipios es",promedio_mes,"toneladas.\n")

def mayor_menor_problema_ambiental(municipios,tipo):
    if not municipios:
        print("No hay datos disponibles.")
        return
    
    total_olores = 0
    total_asentamientos = 0
    total_contaminacion = 0
    total_municipios = len(municipios)
    problema_nombre = ''
    
    for municipio in municipios:
        total_olores += municipio[2]
        total_asentamientos += municipio[3]
        total_contaminacion += municipio[4]
        
    promedio_olores = total_olores / total_municipios
    promedio_asentamientos = total_asentamientos / total_municipios
    promedio_contaminacion = total_contaminacion / total_municipios
    
    problemas = [
        promedio_olores,
        promedio_asentamientos,
        promedio_contaminacion
    ]

    if (tipo.upper() == "MAYOR"):
        mayor_problema = max(problemas)

        if mayor_problema == problemas[0]:
            problema_nombre = 'Olores ofensivos'
        elif mayor_problema == problemas[1]:
            problema_nombre = 'Creación de asentamientos ilegales'
        elif mayor_problema == problemas[2]:
            problema_nombre = 'Contaminación de corrientes hídricas'

        print("\nEl mayor problema ambiental es",problema_nombre,"con un promedio de", round(mayor_problema, 2) ,".\n")
    elif(tipo.upper() == "MENOR"):
        menor_problema = min(problemas)

        if menor_problema == problemas[0]:
            problema_nombre = 'Olores ofensivos'
        elif menor_problema == problemas[1]:
            problema_nombre = 'Creación de asentamientos ilegales'
        elif menor_problema == problemas[2]:
            problema_nombre = 'Contaminación de corrientes hídricas'

        print("\nEl menor problema ambiental es",problema_nombre,"con un promedio de", round(menor_problema, 2) ,".\n")


def promedio_olores(municipios):
    if not municipios:
        print("No hay datos disponibles.")
        return
    
    total_olores = 0
    total_municipios = len(municipios)
    
    for municipio in municipios:
        total_olores += municipio[2] #[2] = olores
        
    promedio_olores = total_olores / total_municipios
    
    print("\nEl promedio de olores ofensivos es",round(promedio_olores,2),"\n")


def promedio_asentamientos(municipios):
    if not municipios:
        print("No hay datos disponibles.")
        return
    
    total_asentamientos = 0
    total_municipios = len(municipios)
    
    for municipio in municipios:
        total_asentamientos += municipio[3] #[3] = asentamientos
        
    promedio_asentamientos = total_asentamientos / total_municipios
    
    print("\nEl promedio de la creación de asentamientos ilegales es",round(promedio_asentamientos,2),"\n")


def promedio_contaminacion(municipios):
    if not municipios:
        print("No hay datos disponibles.")
        return
    
    total_contaminacion = 0
    total_municipios = len(municipios)
    
    for municipio in municipios:
        total_contaminacion += municipio[4] #[4] =contaminacion
        
    promedio_contaminacion = total_contaminacion / total_municipios
    
    print("El promedio de contaminación de corrientes hídricas es", round(promedio_contaminacion),"\n")






def main():

    municipios = [
        ["Rionegro",1000,50,20,30],
        ["Puerto Berrio",2000,20,50,30],
        ["Guatape",6000,30,40,30],
        ["Envigado",2000,30,30,40],
    ]
    while True:

        input("Presione ENTER para continuar: ")
        print("========================")
        print("====MENU DE OPCIONES====")
        print("========================")
        print("1. Lectura de datos")
        print("2. Municipio que más toneladas/día genera")
        print("3. Municipio que menos toneladas/día genera")
        print("4. Promedio de toneladas de basura/día")
        print("5. Promedio de toneladas de basura/mes")
        print("6. Mayor problema ambiental")
        print("7. Menor problema ambiental")
        print("8. Promedio de olores ofensivos")
        print("9. Promedio de creación de asentamientos ilegales")
        print("10. Promedio de contaminación de corrientes hídricas")
        print("11. Terminar")

        opcion = input("Seleccione una opcion: ")

        if (opcion == "1"):
            leer_datos(municipios)

        elif(opcion == "2"):
            municipio_mas_toneladas(municipios)

        elif(opcion == "3"):
            municipio_menos_toneladas(municipios)

        elif(opcion == "4"):
            promedio_toneladas_dia(municipios)

        elif(opcion == "5"):
            promedio_toneladas_mes(municipios)

        elif(opcion == "6"):
            mayor_menor_problema_ambiental(municipios,"MAYOR")

        elif(opcion == "7"):
            mayor_menor_problema_ambiental(municipios,"MENOR")

        elif(opcion == "8"):
            promedio_olores(municipios)

        elif(opcion == "9"):
            promedio_asentamientos(municipios)

        elif(opcion == "10"):
            promedio_contaminacion(municipios)

        elif(opcion == "11"):
            print("Hasta pronto!")
            break


main()