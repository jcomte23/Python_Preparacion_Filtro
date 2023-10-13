print()
print(" ___________________________________")
print("|                                   |")
print("|   Calculadora de calificaciones   |")
print("|___________________________________|")
print()

try:
    calificacion=float(input("Ingrese la calification => "))
    if(calificacion>=0 and calificacion<=20):
        print("Sacaste una F")
    elif(calificacion>20 and calificacion<=40):
        print("Sacaste una D")
    elif(calificacion>40 and calificacion<=60):
        print("Sacaste una C")
    elif(calificacion>60 and calificacion<=80):
        print("Sacaste una B")
    elif(calificacion>80 and calificacion<=100):
        print("Sacaste una A")
    else:
        print("la calificacion supera el rango de  min:0 y max:100")    
except:    
    print("A ocurrido una exepcion, Reintenta por favor")   

print()
print("#"*5)
print("FIN")
print("#"*5)
print()