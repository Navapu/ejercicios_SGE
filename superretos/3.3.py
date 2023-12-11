n = int(input("Numero de enteros a leer: "))
numeros = []
for i in range(0, n):
    num = int(input("Introduzca un numero: "))
    numeros.append(num)

numeros_invertidos = list(reversed(numeros))

print(numeros_invertidos)