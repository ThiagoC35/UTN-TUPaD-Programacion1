estudiantes = ["Ana", "Carlos", "Elena", "Fernando", "Gabriel", "Laura", "Martin", "Natalia", "Pablo", "Sofia"]

buscar = input("Ingrese el nombre del estudiante a buscar: ")

encontrado = False
posicion = -1

for i in range(len(estudiantes)):
    if estudiantes[i].lower() == buscar.lower():
        encontrado = True
        posicion = i
        break

if encontrado:
    print(f"El estudiante '{buscar}' se encuentra en la posición {posicion}.")
else:
    print(f"El estudiante '{buscar}' no está en la lista.")
    