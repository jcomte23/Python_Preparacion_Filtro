print()
print(" ________________________")
print("|                        |")
print("|   Contador de vocales  |")
print("|________________________|")
print()

cadena = input("Ingresa un texto cualquiera =>").lower()
cantidadDeAparicionesA = cadena.count('a')
cantidadDeAparicionesE = cadena.count('e')
cantidadDeAparicionesI = cadena.count('i')
cantidadDeAparicionesO = cadena.count('o')
cantidadDeAparicionesU = cadena.count('u')

totalVocales = cantidadDeAparicionesA + cantidadDeAparicionesE + cantidadDeAparicionesI + cantidadDeAparicionesO + cantidadDeAparicionesU

print(f"La oración tiene {totalVocales} vocales en total:")
print(f"- 'a' aparece {cantidadDeAparicionesA} veces.")
print(f"- 'e' aparece {cantidadDeAparicionesE} veces.")
print(f"- 'i' aparece {cantidadDeAparicionesI} veces.")
print(f"- 'o' aparece {cantidadDeAparicionesO} veces.")
print(f"- 'u' aparece {cantidadDeAparicionesU} veces.")
