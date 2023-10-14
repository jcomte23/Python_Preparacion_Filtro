#Algoritmo que nos diga si una persona puede acceder a cursar un ciclo formativo de grado superior o no. 
#Para acceder a un grado superior. si se tiene un titulo de bachiller, en caso de no tenerlo. 
#se puede acceder si hemos superado una prueba de acceso.

# Pedir al usuario si tiene título de bachiller o ha superado la prueba de acceso
titulo_bachiller = input("¿Tiene título de bachiller? (Sí/No): ")
prueba_acceso = input("¿Ha superado la prueba de acceso? (Sí/No): ")

# Verificar si la persona puede acceder a un ciclo formativo de grado superior
if titulo_bachiller.lower() == "si":
    print("La persona puede acceder a un ciclo formativo de grado superior.")
elif prueba_acceso.lower() == "si":
    print("La persona puede acceder a un ciclo formativo de grado superior.")
else:
    print("La persona no puede acceder a un ciclo formativo de grado superior.")