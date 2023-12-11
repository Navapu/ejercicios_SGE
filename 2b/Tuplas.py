calle = input("Introduzca el nombre de su calle: ")
num = int(input("Introduzca el numero de su puerta: "))
piso = int(input("Introduzca el numero de su piso: "))

persona = calle, num, piso

for i in persona:
    print(i)