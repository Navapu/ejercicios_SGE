num = int(input("Introduzca un numero: "))

for i in range(num + 1):
    if i % 2 != 0:
        if num == i:
            print(i)
        else:
            print(i, end=", ")