tablero = [["-" for _ in range(3)] for _ in range(3)]

def mostrar_tablero(t):
    for fila in t:
        for casilla in fila:
            print(casilla, end=" ")
        print()

turnos = 0
jugadores = ["X", "O"]

while turnos < 9:
    mostrar_tablero(tablero)
    jugador_actual = jugadores[turnos % 2]
    print(f"Turno del jugador {jugador_actual}")
    
    f = int(input("Ingrese fila (0, 1, 2): "))
    c = int(input("Ingrese columna (0, 1, 2): "))
    
    if 0 <= f < 3 and 0 <= c < 3 and tablero[f][c] == "-":
        tablero[f][c] = jugador_actual
        turnos += 1
    else:
        print("Posición inválida o ocupada. Intente nuevamente.")

mostrar_tablero(tablero)
