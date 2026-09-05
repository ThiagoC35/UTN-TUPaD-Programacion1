estudiantes = ["Ana", "Bruno", "Carlos", "Daniela", "Esteban", "Sofia", "Mateo", "Lucia"]

print("Lista de estudiantes presentes:")
for e in estudiantes:
    print(f"- {e}")

opcion = input("\n¿Desea agregar (A) o eliminar (E) un estudiante?: ").strip().upper()

if opcion == "A":
    nuevo = input("Ingrese el nombre del estudiante a agregar: ")
    estudiantes.append(nuevo)
elif opcion == "E":
    eliminar = input("Ingrese el nombre del estudiante a eliminar: ")
    if eliminar in estudiantes:
        estudiantes.remove(eliminar)
    else:
        print("Estudiante no encontrado.")

print("\nLista final actualizada:")
for e in estudiantes:
    print(f"- {e}")
    