ventas = [
    [10, 12, 15, 8, 20, 25, 18],  
    [5, 7, 6, 9, 10, 12, 11],     
    [20, 22, 25, 19, 30, 35, 40], 
    [15, 10, 8, 12, 14, 16, 15]   
]


totales_producto = []
for i in range(4):
    suma_prod = 0
    for v in ventas[i]:
        suma_prod += v
    totales_producto.append(suma_prod)
    print(f"Total vendido Producto {i + 1}: {suma_prod}")


totales_dia = []
for j in range(7):
    suma_dia = 0
    for i in range(4):
        suma_dia += ventas[i][j]
    totales_dia.append(suma_dia)

dia_max = totales_dia.index(max(totales_dia)) + 1
print(f"El día con mayores ventas totales fue el día {dia_max} ({max(totales_dia)} unidades).")


prod_max = totales_producto.index(max(totales_producto)) + 1
print(f"El producto más vendido fue el Producto {prod_max} ({max(totales_producto)} unidades).")