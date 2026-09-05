numeros = [10, 20, 30, 40, 50, 60, 70]

ultimo = numeros[-1]
numeros_rotados = [ultimo] + numeros[:-1]

print("Lista original:", numeros)
print("Lista rotada a la derecha:")
for num in numeros_rotados:
    print(num, end=" ")
print()
