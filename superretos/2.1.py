# Entrada de datos
horas_trabajadas = float(input("Introduce el número de horas trabajadas: "))
precio_por_hora = float(input("Introduce el precio por hora: "))

# Definir tarifas
tarifa_normal = precio_por_hora
tarifa_extra = 1.5 * precio_por_hora

horas_normales = min(horas_trabajadas, 35)
horas_extra = max(0, horas_trabajadas - 35)

sueldo_bruto = (horas_normales * tarifa_normal) + (horas_extra * tarifa_extra)

impuestos_1 = min(sueldo_bruto, 500) * 0  # Los primeros 500 euros son libres de impuestos
impuestos_2 = max(0, min(sueldo_bruto - 500, 400)) * 0.25  # Los siguientes 400 euros tienen un 25% de impuestos
impuestos_3 = max(0, sueldo_bruto - 900) * 0.45  # El resto tiene un 45% de impuestos

impuestos_totales = impuestos_1 + impuestos_2 + impuestos_3

salario_neto = sueldo_bruto - impuestos_totales

print(f"El salario neto semanal es: {salario_neto:.2f} euros")
