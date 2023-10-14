#Simulacro filtro RIWI 2023

def agregar_coder(grupo_a,grupo_b,grupo_c):
    #Pido la informacion al usuario
    nombre_coder = input("Ingrese el nombre del coder: ")
    ingreso_coder = input("Ingrese el mes de ingreso del coder: ")
    edad_coder = int(input("Ingrese la edad del coder: "))
    grupo_coder = input("Ingrese el grupo del coder (A,B,C): ")
    inasistencias = int(input("Ingrese las inasistencias del estudiante: "))
    participaciones = int(input("Ingrese las participaciones en clase del estudiante: "))
    participaciones_monitor = int(input("Ingrese el numero de las participaciones como monitor en clase del estudiante: "))
    talleres = int(input("Ingrese el numero de talleres realizados por el estudiante: "))
    colaboraciones = int(input("Ingrese el numero de colaboraciones del coder en clase: "))
    test_nivelacion = int(input("Ingrese la nota de test de nivelacion del coder: "))

    #guardo la informacion en una lista donde:
    # posicion[0] = nombre, posicion[1] = fecha_ingreso, posicion[2] = edad,posicion[3] = grupo, 
    # inasistencias[4], participaciones[5],participaciones_monitor[6], talleres_entregados[7]
    #colaboraciones[8], [nota_nivelacion9]
    nuevo_coder = {
        "nombre_coder": nombre_coder,
        "ingreso_coder": ingreso_coder,
        "edad_coder":edad_coder,
        "grupo_coder":grupo_coder,
        "inasistencias":inasistencias,
        "participaciones":participaciones,
        "participaciones_monitor":participaciones_monitor,
        "talleres":talleres,
        "colaboraciones":colaboraciones,
        "test_nivelacion":test_nivelacion
    }

    list_info_coder = [
        nombre_coder,
        ingreso_coder,
        edad_coder,
        grupo_coder,
        inasistencias,
        participaciones,
        participaciones_monitor,
        talleres,
        colaboraciones,
        test_nivelacion
    ]

    def mensaje_coder_agregado():
        print("\nCoder agregado correctamente... \n")

    #Valido a que grupo pertenece y lo agrego
    if (grupo_coder.lower() == "a"):
        grupo_a.append(list_info_coder)
        mensaje_coder_agregado()
    elif(grupo_coder.lower() == "b"):
        grupo_b.append(list_info_coder)
        mensaje_coder_agregado()
    elif(grupo_coder.lower() == "c"):
        grupo_c.append(list_info_coder)
        mensaje_coder_agregado()
    else:
        print("El grupo ingresado es incorrecto pruebe nuevamente \n")

def recorrer_lista_estudiantes(lista, grupo):
    #Valido si no hay elementos en la lista
    if not lista:
        print("No hay coders en el grupo",grupo,":")
        return
            
    print("\nLista de coders grupo",grupo,":")
    indice = 0 
    for coder in lista:
        print(indice,'; - Nombre:',coder[0],'Fecha de ingreso:',coder[1],'Edad:',coder[2],'Grupo',coder[3],'Inasistencias',coder[4])
        indice += indice

def listar_coders(grupo_a,grupo_b,grupo_c):
    grupo_listar = input("\n Cual grupo de coders quieres listar? (A,B,C) ")

    if (grupo_listar.lower() == "a"):
        recorrer_lista_estudiantes(grupo_a, "A")
    elif(grupo_listar.lower() == "b"):
        recorrer_lista_estudiantes(grupo_b, "B")
    elif(grupo_listar.lower() == "c"):
        recorrer_lista_estudiantes(grupo_c, "C")
    else:
        print("El grupo ingresado es incorrecto pruebe nuevamente \n")


def encontrar_duplicados(grupo_a,grupo_b,grupo_c):
    coders_duplicados = []
    primer_grupo = input("Ingrese el primer grupo a evaluar (A,B,C): ").upper()
    segundo_grupo = input("Ingrese el segundo grupo a evaluar (A,B,C)   : ").upper()

    if (primer_grupo != "A" and primer_grupo !="B"  and primer_grupo != "C" ):
        print("El primer grupo ingresado no es valido.")
        return
    
    if (segundo_grupo != "A" and segundo_grupo !="B"  and segundo_grupo != "C" ):
        print("El segundo grupo ingresado no es valido.")
        return

    if(primer_grupo == "A" or segundo_grupo == "A" ):
        if(primer_grupo == "B" or segundo_grupo == "B" ):
            for coder1 in grupo_a:
                for coder2 in grupo_b:
                    if coder1[0].lower() == coder2[0].lower():
                        coders_duplicados.append(coder1)

    elif(primer_grupo == "B" or segundo_grupo == "B" ):
        if(primer_grupo == "C" or segundo_grupo == "C" ):
            for coder1 in grupo_b:
                for coder2 in grupo_c:
                    if coder1[0].lower() == coder2[0].lower():
                        coders_duplicados.append(coder1)
    
    elif(primer_grupo == "A" or segundo_grupo == "A" ):
        if(primer_grupo == "C" or segundo_grupo == "C" ):
            for coder1 in grupo_a:
                for coder2 in grupo_c:
                    if coder1[0].lower() == coder2[0].lower():
                        coders_duplicados.append(coder1)

    if coders_duplicados:
        print("Coders duplicados")
    for coder in coders_duplicados:
        if coder:
            print('*',coder[0])
      
def eliminar_coders_inasistencias(grupo_a,grupo_b,grupo_c):
     
    for coder in grupo_a:
        if coder[4] >= 15:  # Si el coder tiene mas de 14 inasistencias
            print("* Se elimino el coder",coder[0]," ya que tiene un total de:" ,coder[4],"inasistencias.")
            grupo_a.remove(coder)


    for coder in grupo_b:
        if coder[4] >= 15:  # Si el coder tiene mas de 14 inasistencias
            print("* Se elimino el coder",coder[0]," ya que tiene un total de:" ,coder[4],"inasistencias.")
            grupo_b.remove(coder)


    for coder in grupo_c:
        if coder[4] >= 15:  # Si el coder tiene mas de 14 inasistencias
            print("* Se elimino el coder",coder[0]," ya que tiene un total de:" ,coder[4],"inasistencias.")
            grupo_c.remove(coder)


def trasladar_coder_lista(lista,opcion,grupo_a,grupo_b,grupo_c,mensaje_satisfactorio):
    for coder in lista:
        print("Cual estudiante quieres trasladar ")
        print(indice,coder[0])
        indice =+ indice
    indice_coder1 =int(input("Ingresa el indice del estudiante a transladar: "))

    if(opcion == "B"):
        grupo_b.append(lista[indice_coder1])
        mensaje_satisfactorio(lista[indice_coder1][0])
        lista.pop(indice_coder1)
    if(opcion == "C"):
        grupo_c.append(lista[indice_coder1])
        mensaje_satisfactorio(lista[indice_coder1][0])
        lista.pop(indice_coder1)




def trasladar_coder(grupo_a,grupo_b,grupo_c):

    def mensaje_satisfactorio(name):
        print("El coder",name,"fue traslado correctamente")

    primer_grupo = input("Trasladar del grupo (A,B,C): ").upper()
    segundo_grupo = input("Al grupo (A,B,C): ").upper()

    if primer_grupo != "A" and primer_grupo != "B" and primer_grupo != "C":
        print("El grupo", primer_grupo, "Es invalido.")
        return
    if segundo_grupo != "A" and segundo_grupo != "B" and segundo_grupo != "C":
        print("El grupo", segundo_grupo, "Es invalido.")
        return
    indice = 0
    
    if primer_grupo == "A":
        for coder in grupo_a:
            print("Cual estudiante quieres trasladar ")
            print(indice,coder[0])
            indice =+ indice
        indice_coder1 =int(input("Ingresa el indice del estudiante a transladar: "))

        if(segundo_grupo == "B"):
            grupo_b.append(grupo_a[indice_coder1])
            mensaje_satisfactorio(grupo_a[indice_coder1][0])
            grupo_a.pop(indice_coder1)
        if(segundo_grupo == "C"):
            grupo_c.append(grupo_a[indice_coder1])
            mensaje_satisfactorio(grupo_a[indice_coder1][0])
            grupo_a.pop(indice_coder1)
    
    if primer_grupo == "B":
        for coder in grupo_b:
            print("Cual estudiante quieres trasladar ")
            print(indice,coder[0])
            indice =+ indice
        indice_coder1 =int(input("Ingresa el indice del estudiante a transladar: "))

        if(segundo_grupo == "A"):
            grupo_a.append(grupo_b[indice_coder1])
            mensaje_satisfactorio(grupo_b[indice_coder1][0])
            grupo_b.pop(indice_coder1)
        if(segundo_grupo == "C"):
            grupo_c.append(grupo_b[indice_coder1])
            mensaje_satisfactorio(grupo_b[indice_coder1][0])
            grupo_b.pop(indice_coder1)

    if primer_grupo == "C":
        for coder in grupo_c:
            print("Cual estudiante quieres trasladar ")
            print(indice,coder[0])
            indice =+ indice
        indice_coder1 =int(input("Ingresa el indice del estudiante a transladar: "))

        if(segundo_grupo == "A"):
            grupo_a.append(grupo_c[indice_coder1])
            mensaje_satisfactorio(grupo_c[indice_coder1][0])
            grupo_c.pop(indice_coder1)

        if(segundo_grupo == "B"):
            grupo_b.append(grupo_c[indice_coder1])
            mensaje_satisfactorio(grupo_c[indice_coder1][0])
            grupo_c.pop(indice_coder1)


def coders_mayores_menores(grupo_a,grupo_b,grupo_c):
    print("\nCoders Mayores de edad: \n")
    print("\nGrupo A: \n")
    for coder in grupo_a:
        if coder[2] >= 18:
            print('*',coder[0],coder[2],"años")

    print("\nGrupo B: \n")
    for coder in grupo_b:
        if coder[2] >= 18:
            print('*',coder[0],coder[2],"años")
    
    print("\nGrupo C: \n")
    for coder in grupo_c:
        if coder[2] >= 18:
            print('*',coder[0],coder[2],"años")

    print("\nCoders Menores de edad: \n")
    print("\nGrupo A: \n")
    for coder in grupo_a:
        if coder[2] < 18:
            print('*',coder[0],coder[2],"años")

    print("\nGrupo B: \n")
    for coder in grupo_b:
        if coder[2] < 18:
            print('*',coder[0],coder[2],"años")
    
    print("\nGrupo C: \n")
    for coder in grupo_c:
        if coder[2] < 18:
            print('*',coder[0],coder[2],"años")
        
def monitores_clase(grupo_a,grupo_b,grupo_c):
    monitor_max_puntaje = 0
    nombre_monitor_max_puntaje = ''

    if grupo_a: 
        for coder in grupo_a:
            if coder[6] > monitor_max_puntaje:
                monitor_max_puntaje = coder[6]
                nombre_monitor_max_puntaje = coder[0]
    if grupo_b: 
        for coder in grupo_b:
            if coder[6] > monitor_max_puntaje:
                monitor_max_puntaje = coder[6]
                nombre_monitor_max_puntaje = coder[0]


    if grupo_c: 
        for coder in grupo_c:
            if coder[6] > monitor_max_puntaje:
                monitor_max_puntaje = coder[6]
                nombre_monitor_max_puntaje = coder[0]
    
    if monitor_max_puntaje > 0 and nombre_monitor_max_puntaje != "" :
        print("\nEl coder",nombre_monitor_max_puntaje.upper(),"Es el mejor monitor de clase,con un puntaje de",monitor_max_puntaje,"puntos\n")
    else:
        print("No hay ningun coder para este premio")


def coders_sin_inasistencias(grupo_a,grupo_b,grupo_c):
    coders_premiados = []
    if grupo_a: 
        for coder in grupo_a:
            if coder[4] == 0:
               coders_premiados.append(coder)
    if grupo_b: 
        for coder in grupo_b:
            if coder[4] == 0:
               coders_premiados.append(coder)


    if grupo_c: 
        for coder in grupo_c:
            if coder[4] == 0:
               coders_premiados.append(coder)
    if coders_premiados:
        print("\nCoders premiados por no tener ninguna inasistencia: \n")
        for coder in coders_premiados:
            print('*',coder[0],'del grupo',coder[3])
    else:
        print("No hay ningun coder para este premio")
     

def coders_max_talleres(grupo_a,grupo_b,grupo_c):
    taller_max = 0
    nombre_max_talleres = ''

    if grupo_a: 
        for coder in grupo_a:
            if coder[7] > taller_max:
                taller_max = coder[7]
                nombre_max_talleres = coder[0]
    if grupo_b: 
        for coder in grupo_b:
            if coder[7] > taller_max:
                taller_max = coder[7]
                nombre_max_talleres = coder[0]

    if grupo_c: 
        for coder in grupo_c:
            if coder[7] > taller_max:
                taller_max = coder[7]
                nombre_max_talleres = coder[0]
    
    if taller_max > 0 and nombre_max_talleres != "" :
        print("\nEl coder",nombre_max_talleres.upper(),"Es el coder con mas talleres realizados,con un puntaje de",taller_max,"talleres realizados\n")
    else:
        print("No hay ningun coder para este premio")
    
def coders_max_colaboraciones(grupo_a,grupo_b,grupo_c):
    colaboraciones_max = 0
    nombre_max_colaboraciones = ''

    if grupo_a: 
        for coder in grupo_a:
            if coder[8] > colaboraciones_max:
                colaboraciones_max = coder[8]
                nombre_max_colaboraciones = coder[0]
    if grupo_b: 
        for coder in grupo_b:
            if coder[8] > colaboraciones_max:
                colaboraciones_max = coder[8]
                nombre_max_colaboraciones = coder[0]

    if grupo_c: 
        for coder in grupo_c:
            if coder[8] > colaboraciones_max:
                colaboraciones_max = coder[8]
                nombre_max_colaboraciones = coder[0]
    
    if colaboraciones_max > 0 and nombre_max_colaboraciones != "" :
        print("\nEl coder",nombre_max_colaboraciones.upper(),"Es el coder con mas colaboraciones realizados,con un puntaje de",colaboraciones_max,"colaboraciones\n")
    else:
        print("No hay ningun coder para este premio")

def coder_max_test_nivelacion(grupo_a,grupo_b,grupo_c):
    test_nivelacion_max = 0
    test_nivelacion_max_name = ''

    if grupo_a: 
        for coder in grupo_a:
            if coder[9] > test_nivelacion_max:
                test_nivelacion_max = coder[9]
                test_nivelacion_max_name = coder[0]
    if grupo_b: 
        for coder in grupo_b:
            if coder[9] > test_nivelacion_max:
                test_nivelacion_max = coder[9]
                test_nivelacion_max_name = coder[0]

    if grupo_c: 
        for coder in grupo_c:
            if coder[9] > test_nivelacion_max:
                test_nivelacion_max = coder[9]
                test_nivelacion_max_name = coder[0]
    
    if test_nivelacion_max > 0 and test_nivelacion_max != "" :
        print("\nEl coder",test_nivelacion_max_name.upper(),"Es el coder con mas colaboraciones realizados,con un puntaje de",test_nivelacion_max,"colaboraciones\n")
    else:
        print("No hay ningun coder para este premio")    

def coder_max_participativo(grupo_a,grupo_b,grupo_c):
    participativo_max = 0
    nombre_max_participativo = ''

    if grupo_a: 
        for coder in grupo_a:
            if coder[5] > participativo_max:
                participativo_max = coder[5]
                nombre_max_participativo = coder[0]
    if grupo_b: 
        for coder in grupo_b:
            if coder[5] > participativo_max:
                participativo_max = coder[5]
                nombre_max_participativo = coder[0]

    if grupo_c: 
        for coder in grupo_c:
            if coder[5] > participativo_max:
                participativo_max = coder[5]
                nombre_max_participativo = coder[0]
    
    if participativo_max > 0 and nombre_max_participativo != "" :
        print("\nEl coder",nombre_max_participativo.upper(),"Es el coder con mas participaciones en clase,con un puntaje de",participativo_max,"participaciones\n")
    else:
        print("No hay ningun coder para este premio")

def coders_max_nota_nivelacion(grupo_a,grupo_b,grupo_c):
    nota_nivelacion_max = 0
    nombre_nivelacion_max = ''
    ganadores = []

    if grupo_a: 
        for coder in grupo_a:
            if coder[9] > nota_nivelacion_max:
                if coder[9] == nota_nivelacion_max:
                    ganadores.append(coder)
                else:
                    nota_nivelacion_max = coder[9]
                    nombre_nivelacion_max = coder[0]
    if grupo_b: 
        for coder in grupo_b:
            if coder[9] > nota_nivelacion_max:
                nota_nivelacion_max = coder[9]
                nombre_nivelacion_max = coder[0]

    if grupo_c: 
        for coder in grupo_c:
            if coder[9] > nota_nivelacion_max:
                nota_nivelacion_max = coder[9]
                nombre_nivelacion_max = coder[0]
    
    if nota_nivelacion_max > 0 and nombre_nivelacion_max != "" :
        if ganadores:
            for coder in ganadores:
                print("\nEl coder",nombre_nivelacion_max.upper(),"Es el coder con mas participaciones en clase,con un puntaje de",nota_nivelacion_max,"participaciones\n")
        else:
            print("\nEl coder",nombre_nivelacion_max.upper(),"Es el coder con mas participaciones en clase,con un puntaje de",nota_nivelacion_max,"participaciones\n")

    else:
        print("No hay ningun coder para este premio")

def main():

    #Inicializo mis grupos
    grupo_a = []
    grupo_b = []
    grupo_c = []

    #Trainer grupo A
    trainer_a = ""


    while True:
        #Defino mi menu de opciones
        input("Presione ENTER para continuar: ")
        print("\n\n==========================")
        print("==== MENÚ DE OPCIONES ====")
        print("==========================\n")
        print("1. Ingresar Coder")
        print("1.1 Registrar Trainer grupo A")
        print("1.2 Buscar Coders duplicados en 2 grupos.")
        print("1.3 Eliminar coders por inasistencias.")
        print("1.4 Listar Coders por grupo")
        print("1.5 Trasladar Coder")
        print("1.7 Coders mayores y menores de edad.")
        print("2. Coder con el mayor número de veces en que se ha desempeñado como monitor de clase.")
        print("2.1 Coders con 0 inasistencia.")
        print("2.2 Coders con más entregas de talleres en Aula.")
        print("2.3 Coders mas colaborador")
        print("2.4 Coder con la mayor nota en Test de nivelación.")
        print("2.5 Coder más participativo.")
        print("3. Salir.")

        #Pido la opcion al usuario
        opcion = input("\nIngrese una opción: ")
        
        if (opcion == "1"):
            agregar_coder(grupo_a,grupo_b,grupo_c)

        elif(opcion == "1.1"):
            trainer_a = input("Ingresa el nombre del Trainer del grupo A")
            print("El Trainer",trainer_a,"fue agregado correctamente")

        elif(opcion == "1.2"):
            encontrar_duplicados(grupo_a,grupo_b,grupo_c)

        elif(opcion == "1.3"):
            eliminar_coders_inasistencias(grupo_a,grupo_b,grupo_c)
            
        elif(opcion == "1.4"):
            listar_coders(grupo_a,grupo_b,grupo_c)

        elif(opcion == "1.5"):
            trasladar_coder(grupo_a,grupo_b,grupo_c)
      
        elif(opcion == "1.7"):
            coders_mayores_menores(grupo_a,grupo_b,grupo_c)
        
        elif(opcion == "2"):
            monitores_clase(grupo_a,grupo_b,grupo_c)

        elif(opcion == "2.1"):
            coders_sin_inasistencias(grupo_a,grupo_b,grupo_c)

        elif(opcion == "2.2"):
            coders_max_talleres(grupo_a,grupo_b,grupo_c)      

        elif(opcion == "2.3"):
            coders_max_colaboraciones(grupo_a,grupo_b,grupo_c)  

        elif(opcion == "2.4"):
            coders_max_nota_nivelacion(grupo_a,grupo_b,grupo_c)     

        elif(opcion == "2.5"):
            coder_max_participativo(grupo_a,grupo_b,grupo_c)      

        elif(opcion == "3"):
            print("Hasta pronto")
            break
        else:
            print("Opcion no valida")
      

main()