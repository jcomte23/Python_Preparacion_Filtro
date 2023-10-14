print("*"*30)
print("|       Metodos para alterar textos    |")
print("*"*30)
print()

print("Python también nos provee de métodos para trabajar con los strings, estos son los mas comunes:")
print("in: valida si un texto esta dentro de otro texto.")

print()
texto="hola mundo como estas"
if("mundo" in texto):
    print("la palabra clave esta dentro del texto")

print()
print("len: cuenta la cantidad de caracteres de un texto, tomando en cuenta los espacios")
texto="hola mundo como estas"
print(len(texto))

print()
print("upper: transforma el texto a mayúsculas")
texto="hola mundo como estas"
print(texto.upper())

print()
print("lower: transforma el texto a minúsculas")
texto="HOLA MUNDO"
print(texto.lower())

print()
print("capitalize: transforma la primera letra de un string en mayúscula")
texto="hola mundo"
print(texto.capitalize())

print()
print("title: transforma la primera letra de cada palabra en mayúscula dentro de un string")
texto="hola mundo"
print(texto.title())

print()
print("count: cuenta la cantidad de apariciones de un texto dentro de otro")
texto="anita lava la tina"
print(texto.count("la"))

print()
print("swapcase: intercambia los texto de mayúscula a minúscula de acuerdo a su estado")
texto="HoLa MuNdO"
print(texto.swapcase())

print()
print("startswith: pregunta si un texto empieza con una palabra clave")
texto="hola mundo"
print(texto.startswith("hol"))

print()
print("endswith: pregunta si un texto termina con una palabra clave")
texto="hola mundo"
print(texto.endswith("do"))

print()
print("replace: remplaza un texto por otro dentro de un string")
texto="hola mundo"
print(texto.replace("mundo","familia"))

print()
print("isdigit: verifica si un string es potencialmente un numero")
texto="2455"
print(texto.isdigit())

print()
print("strip: elimina los espacios accidentales al comienzo y final de un string")
cadena = "   ¡Hola, mundo!   "
cadena_sin_espacios = cadena.strip()
print(cadena_sin_espacios)
