n = int(input("Numero de enteros a leer: "))  
max_numero = float('-inf')  
min_numero = float('inf')  

for _ in range(n):
    numero = int(input("Introduzca un numero"))
    max_numero = max(max_numero, numero)
    min_numero = min(min_numero, numero)

print(f"{max_numero} {min_numero}")