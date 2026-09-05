puntajes = [450, 1200, 875, 990, 300, 1500, 640]

print(f"Puntaje más alto: {max(puntajes)}")
print(f"Puntaje más bajo: {min(puntajes)}")

ranking = sorted(puntajes, reverse=True)

print("\nRanking (de mayor a menor):")
for pos, p in enumerate(ranking, start=1):
    print(f"{pos}° lugar: {p}")

pos_990 = ranking.index(990) + 1
print(f"\nEl puntaje 990 se encuentra en la posición {pos_990} del ranking.")
