import os

# Nombre del archivo donde se guardarán los datos
ARCHIVO_PRODUCTOS = "productos.txt"

def crear_archivo_inicial():
    if not os.path.exists(ARCHIVO_PRODUCTOS):
        datos_iniciales = [
            "Lapicera,120.5,30\n",
            "Cuaderno,450.0,15\n",
            "Gorra,850.75,20\n"
        ]
        with open(ARCHIVO_PRODUCTOS, "w", encoding="utf-8") as archivo:
            archivo.writelines(datos_iniciales)

def leer_y_mostrar_productos():
    print("--- LISTADO DE PRODUCTOS ---")
    try:
        with open(ARCHIVO_PRODUCTOS, "r", encoding="utf-8") as archivo:
            for linea in archivo:
                linea = linea.strip()
                if linea:  # Evitar líneas vacías
                    nombre, precio, cantidad = linea.split(",")
                    print(f"Producto: {nombre} | Precio: ${precio} | Cantidad: {cantidad}")
    except FileNotFoundError:
        print("El archivo aún no existe.")
    print("-" * 30)

def cargar_en_lista_diccionarios():
    lista_productos = []
    try:
        with open(ARCHIVO_PRODUCTOS, "r", encoding="utf-8") as archivo:
            for linea in archivo:
                linea = linea.strip()
                if linea:
                    nombre, precio, cantidad = linea.split(",")
                    producto = {
                        "nombre": nombre,
                        "precio": float(precio),
                        "cantidad": int(cantidad)
                    } 
                    lista_productos.append(producto)
    except FileNotFoundError:
        pass
    return lista_productos

def agregar_producto(lista_productos):
    print("\n--- AGREGAR NUEVO PRODUCTO ---")
    nombre = input("Ingrese el nombre del producto: ").strip()
    
    # Validaciones básicas de entrada numérica
    try:
        precio = float(input("Ingrese el precio del producto: "))
        cantidad = int(input("Ingrese la cantidad: "))
        
        nuevo_producto = {
            "nombre": nombre,
            "precio": precio,
            "cantidad": cantidad
        }
        
        lista_productos.append(nuevo_producto)
        guardar_en_archivo(lista_productos)
        print("¡Producto agregado y guardado con éxito!")
    except ValueError:
        print("Error: Ingrese un valor numérico válido para el precio y la cantidad.")

def buscar_producto(lista_productos):
    print("\n--- BUSCAR PRODUCTO ---")
    buscado = input("Ingrese el nombre del producto que desea buscar: ").strip().lower()
    
    encontrado = False
    for prod in lista_productos:
        if prod["nombre"].lower() == buscado:
            print(f"\n¡Producto encontrado!")
            print(f"-> Producto: {prod['nombre']} | Precio: ${prod['precio']} | Cantidad: {prod['cantidad']}")
            encontrado = True
            break
            
    if not encontrado:
        print("Error: El producto buscado no existe en el registro.")

def guardar_en_archivo(lista_productos):
    with open(ARCHIVO_PRODUCTOS, "w", encoding="utf-8") as archivo:
        for prod in lista_productos:
            linea = f"{prod['nombre']},{prod['precio']},{prod['cantidad']}\n"
            archivo.write(linea)

def main():
    # Asegurar que el archivo base esté creado
    crear_archivo_inicial()
    
    while True:
        print("\n=== MENÚ PRINCIPAL - GESTIÓN DE ARCHIVOS ===")
        print("1. Mostrar productos")
        print("2. Agregar un nuevo producto")
        print("3. Buscar un producto por nombre")
        print("4. Salir")
        
        opcion = input("Seleccione una opción (1-4): ").strip()
        productos = cargar_en_lista_diccionarios()
        
        if opcion == "1":
            leer_y_mostrar_productos()
        elif opcion == "2":
            agregar_producto(productos)
        elif opcion == "3":
            buscar_producto(productos)
        elif opcion == "4":
            print("Saliendo del programa. ¡Hasta luego!")
            break
        else:
            print("Opción inválida. Por favor, elija un número entre 1 y 4.")

if __name__ == "__main__":
    main()