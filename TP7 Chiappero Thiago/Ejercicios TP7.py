#Ejercicio 1

precios_frutas = {
    'Banana': 1200, 
    'Ananá': 2500, 
    'Melón': 3000, 
    'Uva': 1450}

precios_frutas['Naranja'] = 1200
precios_frutas['Manzana'] = 1500
precios_frutas['Pera'] = 2300

print(precios_frutas)

#Ejercicio 2

precios_frutas['Banana'] = 1330
precios_frutas['Manzana'] = 1700
precios_frutas['Melón'] = 2800

print(precios_frutas)

#Ejercicio 3

lista_frutas = list(precios_frutas.keys())
print(lista_frutas)

#Ejercicio 4
contactos = {}

print("--- Carga de Contactos ---")
for i in range(5):
    nombre = input(f"Ingrese el nombre del contacto {i+1}: ")
    numero = input(f"Ingrese el número de {nombre}: ")
    contactos[nombre] = numero

consulta = input("\nIngrese el nombre del contacto que desea buscar: ")
if consulta in contactos:
    print(f"El número de {consulta} es: {contactos[consulta]}")
else:
    print(f"El contacto '{consulta}' no se encuentra en la agenda.")

#Ejercicio 5
frase = input("Ingrese una frase: ")
palabras = frase.lower().split()

palabras_unicas = set(palabras)

recuento = {}
for palabra in palabras:
    recuento[palabra] = recuento.get(palabra, 0) + 1

print("Palabras únicas:", palabras_unicas)
print("Recuento:", recuento)

#Ejercicio 6
alumnos = {}

for i in range(3):
    nombre = input(f"Ingrese el nombre del alumno {i+1}: ")

    notas_input = input(f"Ingrese 3 notas de {nombre} separadas por espacio: ")
    notas = tuple(map(int, notas_input.split()))
    alumnos[nombre] = notas

print("\n--- Promedios de Alumnos ---")
for alumno, notas in alumnos.items():
    promedio = sum(notas) / len(notas)
    print(f"{alumno}: Notas {notas} -> Promedio: {promedio:.2f}")

#Ejercicio 7
asistencias = ["Ana", "Luis", "Ana", "María", "Luis", "Pedro", "Ana"]

print("Lista original de asistencias:", asistencias)

asistentes_unicos = set(asistencias)
print("Asistentes únicos (sin repetir):", asistentes_unicos)

conteo_asistencias = {}
for persona in asistencias:
    conteo_asistencias[persona] = conteo_asistencias.get(persona, 0) + 1

print("Veces que asistió cada persona:", conteo_asistencias)

#Ejercicio 8
stock = {"lapiz": 10, "cuaderno": 5, "goma": 3}

while True:
    print("\n--- Menú Stock ---")
    print("1. Consultar stock")
    print("2. Agregar/Actualizar stock de un producto")
    print("3. Salir")
    opcion = input("Seleccione una opción: ")
    
    if opcion == "1":
        producto = input("Ingrese el producto a consultar: ")
        if producto in stock:
            print(f"Stock de {producto}: {stock[producto]}")
        else:
            print("El producto no existe en el inventario.")
            
    elif opcion == "2":
        producto = input("Ingrese el nombre del producto: ")
        cantidad = int(input("Ingrese la cantidad a sumar/establecer: "))
        if producto in stock:
            stock[producto] += cantidad
            print(f"Stock actualizado. Nuevo stock de {producto}: {stock[producto]}")
        else:
            stock[producto] = cantidad
            print(f"Nuevo producto '{producto}' agregado con stock {cantidad}.")
            
    elif opcion == "3":
        break
    else:
        print("Opción inválida.")

print("Stock final:", stock)

#Ejercicio 9
agenda = {
    ("lunes", "10:00"): "Reunión",
    ("martes", "15:00"): "Clase de inglés",
    ("viernes", "18:00"): "Fútbol"
}

dia_consulta = input("Ingrese el día a consultar (ej. lunes): ").lower()
hora_consulta = input("Ingrese la hora a consultar (ej. 10:00): ")

clave = (dia_consulta, hora_consulta)

if clave in agenda:
    print(f"Actividad programada: {agenda[clave]}")
else:
    print("No hay ninguna actividad registrada en ese día y horario.")

#Ejercicio 10
original = {"Argentina": "Buenos Aires", "Chile": "Santiago", "Uruguay": "Montevideo"}

invertido = {}
for pais, capital in original.items():
    invertido[capital] = pais

print("Diccionario original:", original)
print("Diccionario invertido:", invertido)
