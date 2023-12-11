a = True
numtotal = 0
while(a == True):
    num = float(input("Introduzca un numero: "))
    if(num == 0):
        break
    numtotal += num

print("La factura es de: %.2f" % numtotal)
