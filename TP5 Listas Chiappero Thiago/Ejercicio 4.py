datos = [1, 3, 5, 3, 7, 1, 9, 5, 3]
sin_repetidos = []

for item in datos:
    if item not in sin_repetidos:
        sin_repetidos.append(item)

print("Lista sin elementos repetidos:")
for item in sin_repetidos:
    print(item, end=" ")
print()
