notas = [7.5, 8.0, 4.5, 9.0, 10.0, 6.0, 5.5, 8.5, 7.0, 3.5]

print("Notas cargadas:")
for nota in notas:
    print(nota, end=" ")
print()

suma = 0
for nota in notas:
    suma += nota
promedio = suma / len(notas)

nota_max = notas[0]
nota_min = notas[0]
for nota in notas:
    if nota > nota_max:
        nota_max = nota
    if nota < nota_min:
        nota_min = nota

print(f"Promedio: {promedio:.2f}")
print(f"Nota más alta: {nota_max}")
print(f"Nota más baja: {nota_min}")