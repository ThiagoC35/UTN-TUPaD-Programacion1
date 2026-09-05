import random

numeros = [random.randint(1, 100) for _ in range(15)]
pares = []
impares = []

for num in numeros:
    if num % 2 == 0:
        pares.append(num)
    else:
        impares.append(num)

print("Lista original:")
for num in numeros:
    print(num, end=" ")
print()

print(f"Cantidad de números pares: {len(pares)}")
print(f"Cantidad de números impares: {len(impares)}")
