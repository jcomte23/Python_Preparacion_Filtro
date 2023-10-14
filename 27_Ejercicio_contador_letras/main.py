print()
print(" _______________________")
print("|                       |")
print("|   Contador de letras  |")
print("|_______________________|")
print()


cadena=input("Ingresa un texto cualquiera =>").lower()
letra=input("Ingresa la letra o fraccion de texto que quiere buscar =>").lower()
cantidadDeApiriciones=cadena.count(letra)
print(f"La fraccion '{letra}' aparece {cantidadDeApiriciones} veces")