numeros = []
for i in range(8):
    n = int(input(f"Ingrese el número {i + 1}: "))
    numeros.append(n)

print("\nLista original:")
for num in numeros:
    print(num, end=" ")
print()

ascendente = sorted(numeros)
print("Lista de menor a mayor:")
for num in ascendente:
    print(num, end=" ")
print()

descendente = sorted(numeros, reverse=True)
print("Lista de mayor a menor:")
for num in descendente:
    print(num, end=" ")
print()
