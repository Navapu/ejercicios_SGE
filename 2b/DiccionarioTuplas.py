personas = {}
for i in range(1, 3):
    print("\nNUEVA PERSONA: ")
    dni = input("Introduzca el dni de esta persona: ")
    calle = input("Introduzca el nombre de la calle de este: ")
    puerta = int(input("Introduzca el numero de la puerta: "))
    piso = int(input("Introduzca el numero del piso: "))
    personas[dni] = (calle, puerta, piso)

peticion = input("Introduzca el dni de una persona: ")

if peticion in personas:
    print("El nombre de la calle es", personas[peticion][0], "el numero de la puerta es", personas[peticion][1] ,"el numero del piso es", personas[peticion][2])
else:
    print("El dni introducido no existe")