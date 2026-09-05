dias = ["Lunes", "Martes", "Miércoles", "Jueves", "Viernes", "Sábado", "Domingo"]

temperaturas = [
    [10, 22],
    [12, 28],
    [9, 20],
    [11, 24],
    [15, 27],
    [13, 21],
    [8, 19]
]

suma_min, suma_max = 0, 0
max_amplitud = -1
dia_max_amplitud = ""

for i in range(len(temperaturas)):
    minima, maxima = temperaturas[i]
    suma_min += minima
    suma_max += maxima
    
    amplitud = maxima - minima
    if amplitud > max_amplitud:
        max_amplitud = amplitud
        dia_max_amplitud = dias[i]

print(f"Promedio de mínimas: {suma_min / 7:.2f}°C")
print(f"Promedio de máximas: {suma_max / 7:.2f}°C")
print(f"El día con mayor amplitud térmica fue el {dia_max_amplitud} ({max_amplitud}°C de diferencia).")