num = int(input("Introduzca la cantidad de veces que se repetirá: "))
mayor = 0
for i in range(num):
    num1 = int(input("Introduzca un numero: "))
    if mayor == 0:
        menor = num1
    if num1 > mayor:
        mayor = num1
    if num1 < menor:
        menor = num1
print("El mayor es:", mayor)
print("El menor es:", menor)