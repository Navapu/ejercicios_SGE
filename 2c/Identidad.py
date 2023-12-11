lista = []
num = int(input("Introduzca el tamaño de la tabla: "))
for i in range(0, num):
    print("\nIntroduzca los datos de la fila", i)
    columna = []
    for j in range(0, num):
        num1 = int(input("Introduzca un numero: "))
        columna.append(num1)
    lista.append(columna)

