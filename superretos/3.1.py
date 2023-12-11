while True:
    cantidad = int(input("Introduce una cantidad de dinero (múltiplo de 5): "))
    if cantidad % 5 == 0:
        break
    else:
        print("La cantidad ingresada no es un múltiplo de 5. Inténtalo de nuevo.")

billetes_500 = cantidad // 500
cantidad %= 500

billetes_200 = cantidad // 200
cantidad %= 200

billetes_100 = cantidad // 100
cantidad %= 100

billetes_50 = cantidad // 50
cantidad %= 50

billetes_20 = cantidad // 20
cantidad %= 20

billetes_10 = cantidad // 10
cantidad %= 10

billetes_5 = cantidad // 5

print(f"Desglose de cambio para {cantidad} euros:")
print(f"Billetes de 500 euros: {billetes_500}")
print(f"Billetes de 200 euros: {billetes_200}")
print(f"Billetes de 100 euros: {billetes_100}")
print(f"Billetes de 50 euros: {billetes_50}")
print(f"Billetes de 20 euros: {billetes_20}")
print(f"Billetes de 10 euros: {billetes_10}")
print(f"Billetes de 5 euros: {billetes_5}")