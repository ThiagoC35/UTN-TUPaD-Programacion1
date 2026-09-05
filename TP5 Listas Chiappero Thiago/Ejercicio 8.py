notas_estudiantes = [
    [8, 7, 9],
    [6, 5, 7],
    [9, 9, 10],
    [4, 6, 5],
    [7, 8, 8]
]


for i in range(len(notas_estudiantes)):
    suma_est = 0
    for nota in notas_estudiantes[i]:
        suma_est += nota
    print(f"Promedio Estudiante {i + 1}: {suma_est / 3:.2f}")

print("-" * 30)


for j in range(3):
    suma_mat = 0
    for i in range(len(notas_estudiantes)):
        suma_mat += notas_estudiantes[i][j]
    print(f"Promedio Materia {j + 1}: {suma_mat / 5:.2f}")