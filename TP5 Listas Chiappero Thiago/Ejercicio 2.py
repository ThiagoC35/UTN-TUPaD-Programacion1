productos = []
for i in range(5):
    prod = input(f"Ingrese el producto {i + 1}: ")
    productos.append(prod)

productos_ordenados = sorted(productos)
print("\nProductos ordenados alfabéticamente:")
for prod in productos_ordenados:
    print(f"- {prod}")

eliminar = input("\n¿Qué producto desea eliminar?: ")
if eliminar in productos:
    productos.remove(eliminar)
    print(f"'{eliminar}' ha sido eliminado.")
else:
    print("El producto no se encuentra en la lista.")

print("\nLista actualizada de productos:")
for prod in productos:
    print(f"- {prod}")
    