#una tienda ofrece un descuento del 15% sobre el total de la compra durante el mes de octubre. 
#Dado  un mes y un importe, calcular es la cantidad que se debe cobrar al cliente.

# Pedir el mes y el importe de la compra al cliente
mes = input("Ingrese el mes de la compra: ")
importe = float(input("Ingrese el importe de la compra: "))

# Verificar si el mes es octubre
if mes.lower() == "octubre":
    # Calcular el descuento del 15%
    descuento = importe * 0.15
    total_a_pagar = importe - descuento
else:
    # No hay descuento
    total_a_pagar = importe

# Imprimir el total a pagar al cliente
print("Total a pagar:", total_a_pagar)