#Ejercicio 1
nombre = input("Cliente: ").strip()
while not nombre.isalpha():
    print("Error: Ingrese un nombre válido (solo letras, sin espacio ni vacío).")
    nombre = input("Cliente: ").strip()


cant_str = input("Cantidad de productos: ").strip()
while not cant_str.isdigit() or int(cant_str) == 0:
    print("Error: Ingrese un número entero positivo mayor a 0.")
    cant_str = input("Cantidad de productos: ").strip()

cant_productos = int(cant_str)

total_sin_descuento = 0.0
total_con_descuento = 0.0


for i in range(1, cant_productos + 1):
    print(f"\nProducto {i}")
    
    
    precio_str = input("Precio: ").strip()
    while not precio_str.isdigit():
        print("Error: Ingrese un precio entero válido.")
        precio_str = input("Precio: ").strip()
        
    precio = int(precio_str)
    
  
    tiene_descuento = input("Descuento (S/N): ").strip().lower()
    while tiene_descuento not in ["s", "n"]:
        print("Error: Ingrese únicamente 's' o 'n'.")
        tiene_descuento = input("Descuento (S/N): ").strip().lower()
        
   
    total_sin_descuento += precio
    
    if tiene_descuento == "s":
        total_con_descuento += precio * 0.90
    else:
        total_con_descuento += precio


ahorro = total_sin_descuento - total_con_descuento
promedio = total_con_descuento / cant_productos


print(f"\nCliente: {nombre}")
print(f"Cantidad de productos: {cant_productos}")
print("\n--- RESUMEN DE COMPRA ---")
print(f"Total sin descuentos: ${total_sin_descuento:.0f}")
print(f"Total con descuentos: ${total_con_descuento:.2f}")
print(f"Ahorro: ${ahorro:.2f}")
print(f"Promedio por producto: ${promedio:.2f}")

#Ejercicio 2
usuario_correcto = "alumno"
clave_correcta = "python123"

intentos = 1
max_intentos = 3
acceso_concedido = False

while intentos <= max_intentos and not acceso_concedido:
    print(f"Intento {intentos} de {max_intentos}")
    usuario = input("Usuario: ").strip()
    clave = input("Clave: ").strip()

    if usuario == usuario_correcto and clave == clave_correcta:
        acceso_concedido = True
        print("\nAcceso concedido. Bienvenido!")

    else:
        print("Error, credenciales invalidas. \n")
        intentos += 1

if not acceso_concedido:
    print("Cuenta bloqueada.")

else:
    opcion = ""
    while opcion != "4":
        print("\n 1) Estado 2) Cambiar clave 3) Mensaje 4) Salir")
        opcion = input("Opcion: ").strip()

        if not opcion.isdigit():
            print("Error, ingrese un numero valido.")
        elif int(opcion) <1 or int(opcion) > 4:
            print("Error, opcion fuera de rango.")
        else:
            if opcion == "1":
                print("Inscripto")
            elif opcion == "2":
                nueva_clave = input("Nueva clave: ").strip()
                while len(nueva_clave) < 6:
                    print("Error, la clave debe tener al menos 6 caracteres.")
                    nueva_clave = input("Nueva clave: ").strip()

                confirmacion = input("Confirmar nueva clave: ").strip()
                if nueva_clave == confirmacion:
                    clave_correcta = nueva_clave
                    print("Clave actualizada correctamente.")
                else:
                    print("Error, las claves no coinciden. No se actualizó la clave.")

            elif opcion == "3":
                print("Como dijo Fangio, la carrera no se gana en la primera curva, sino cuando se baja la bandera a cuadros.")


#Ejercicio 3
lunes1 = ""
lunes2 = ""
lunes3 = ""
lunes4 = ""

martes1 = ""
martes2 = ""
martes3 = ""


operador = input("Nombre del operador: ").strip()
while not operador.isalpha():
    print("Error: Solo se permiten letras.")
    operador = input("Nombre del operador: ").strip()


opcion = ""
while opcion != "5":
    print(f"\n=== SISTEMA DE TURNOS (Operador: {operador}) ===")
    print("1) Reservar turno")
    print("2) Cancelar turno")
    print("3) Ver agenda del día")
    print("4) Ver resumen general")
    print("5) Cerrar sistema")
    
    opcion = input("Opción: ").strip()
    
    if not opcion.isdigit() or int(opcion) < 1 or int(opcion) > 5:
        print("Error: Opción inválida. Ingrese un número entre 1 y 5.")
        continue


    if opcion == "1":
        dia = input("Elegir día (1 = Lunes, 2 = Martes): ").strip()
        while dia not in ["1", "2"]:
            print("Error: Ingrese 1 para Lunes o 2 para Martes.")
            dia = input("Elegir día (1 = Lunes, 2 = Martes): ").strip()
            
        paciente = input("Nombre del paciente: ").strip()
        while not paciente.isalpha():
            print("Error: Solo se permiten letras.")
            paciente = input("Nombre del paciente: ").strip()
            
        if dia == "1": 
            if paciente in [lunes1, lunes2, lunes3, lunes4]:
                print(f"Error: El paciente '{paciente}' ya tiene un turno asignado el Lunes.")
            elif lunes1 == "":
                lunes1 = paciente
                print("Turno reservado con éxito para el Lunes (Turno 1).")
            elif lunes2 == "":
                lunes2 = paciente
                print("Turno reservado con éxito para el Lunes (Turno 2).")
            elif lunes3 == "":
                lunes3 = paciente
                print("Turno reservado con éxito para el Lunes (Turno 3).")
            elif lunes4 == "":
                lunes4 = paciente
                print("Turno reservado con éxito para el Lunes (Turno 4).")
            else:
                print("Error: No hay cupos disponibles para el Lunes.")
                
        elif dia == "2": 
            if paciente in [martes1, martes2, martes3]:
                print(f"Error: El paciente '{paciente}' ya tiene un turno asignado el Martes.")
            elif martes1 == "":
                martes1 = paciente
                print("Turno reservado con éxito para el Martes (Turno 1).")
            elif martes2 == "":
                martes2 = paciente
                print("Turno reservado con éxito para el Martes (Turno 2).")
            elif martes3 == "":
                martes3 = paciente
                print("Turno reservado con éxito para el Martes (Turno 3).")
            else:
                print("Error: No hay cupos disponibles para el Martes.")

    
    elif opcion == "2":
        dia = input("Elegir día (1 = Lunes, 2 = Martes): ").strip()
        while dia not in ["1", "2"]:
            print("Error: Ingrese 1 para Lunes o 2 para Martes.")
            dia = input("Elegir día (1 = Lunes, 2 = Martes): ").strip()
            
        paciente = input("Nombre del paciente a cancelar: ").strip()
        while not paciente.isalpha():
            print("Error: Solo se permiten letras.")
            paciente = input("Nombre del paciente a cancelar: ").strip()
            
        encontrado = False
        if dia == "1":
            if lunes1.lower() == paciente.lower(): lunes1 = ""; encontrado = True
            elif lunes2.lower() == paciente.lower(): lunes2 = ""; encontrado = True
            elif lunes3.lower() == paciente.lower(): lunes3 = ""; encontrado = True
            elif lunes4.lower() == paciente.lower(): lunes4 = ""; encontrado = True
        elif dia == "2":
            if martes1.lower() == paciente.lower(): martes1 = ""; encontrado = True
            elif martes2.lower() == paciente.lower(): martes2 = ""; encontrado = True
            elif martes3.lower() == paciente.lower(): martes3 = ""; encontrado = True

        if encontrado:
            print(f"Turno de '{paciente}' cancelado exitosamente.")
        else:
            print(f"Error: No se encontró a '{paciente}' en ese día.")

    
    elif opcion == "3":
        dia = input("Elegir día (1 = Lunes, 2 = Martes): ").strip()
        while dia not in ["1", "2"]:
            print("Error: Ingrese 1 para Lunes o 2 para Martes.")
            dia = input("Elegir día (1 = Lunes, 2 = Martes): ").strip()

        if dia == "1":
            print("\n--- AGENDA LUNES ---")
            print(f"Turno 1: {lunes1 if lunes1 != '' else '(libre)'}")
            print(f"Turno 2: {lunes2 if lunes2 != '' else '(libre)'}")
            print(f"Turno 3: {lunes3 if lunes3 != '' else '(libre)'}")
            print(f"Turno 4: {lunes4 if lunes4 != '' else '(libre)'}")
        else:
            print("\n--- AGENDA MARTES ---")
            print(f"Turno 1: {martes1 if martes1 != '' else '(libre)'}")
            print(f"Turno 2: {martes2 if martes2 != '' else '(libre)'}")
            print(f"Turno 3: {martes3 if martes3 != '' else '(libre)'}")

    
    elif opcion == "4":
        ocupados_lunes = (1 if lunes1 != "" else 0) + (1 if lunes2 != "" else 0) + \
                         (1 if lunes3 != "" else 0) + (1 if lunes4 != "" else 0)
                         
        ocupados_martes = (1 if martes1 != "" else 0) + (1 if martes2 != "" else 0) + \
                          (1 if martes3 != "" else 0)

        disp_lunes = 4 - ocupados_lunes
        disp_martes = 3 - ocupados_martes

        print("\n--- RESUMEN GENERAL ---")
        print(f"Lunes: {ocupados_lunes} ocupados | {disp_lunes} disponibles")
        print(f"Martes: {ocupados_martes} ocupados | {disp_martes} disponibles")

        if ocupados_lunes > ocupados_martes:
            print("Día con más turnos ocupados: Lunes")
        elif ocupados_martes > ocupados_lunes:
            print("Día con más turnos ocupados: Martes")
        else:
            print("Día con más turnos ocupados: Empate entre Lunes y Martes")

print("\nSistema cerrado correctamente.")

#Ejercicio 4
energia = 100
tiempo = 12
cerraduras_abiertas = 0
alarma = False
codigo_parcial = ""

forzar_seguidas = 0

agente = input("Nombre del agente: ").strip()
while not agente.isalpha():
    print("Error: El nombre solo puede contener letras.")
    agente = input("Nombre del agente: ").strip()

print(f"\n¡Bienvenido Agente {agente}! La misión ha comenzado.")

while energia > 0 and tiempo > 0 and cerraduras_abiertas < 3 and not alarma:
    print("\n----------------------------------------")
    print(f"ESTADO: Energía: {energia} | Tiempo: {tiempo} | Cerraduras: {cerraduras_abiertas}/3 | Alarma: {alarma}")
    print("----------------------------------------")
    print("1. Forzar cerradura (costo: -20 energía, -2 tiempo)")
    print("2. Hackear panel (costo: -10 energía, -3 tiempo)")
    print("3. Descansar (costo: +15 energía, -1 tiempo)")
    
    opcion = input("Elija una acción (1-3): ").strip()
    
    while not opcion.isdigit() or int(opcion) < 1 or int(opcion) > 3:
        print("Error: Elija una opción válida (1, 2 o 3).")
        opcion = input("Elija una acción (1-3): ").strip()
        
    opcion_num = int(opcion)
    
    if opcion_num == 1:
        forzar_seguidas += 1
        
        energia -= 20
        tiempo -= 2
        
        if forzar_seguidas == 3:
            print("\n¡La cerradura se trabó por forzar 3 veces seguidas! La alarma se ha activado.")
            alarma = True
        else:
            riesgo = False
            if energia < 40:
                num_riesgo = input("¡Riesgo de alarma! Elija un número entre 1 y 3: ").strip()
                while not num_riesgo.isdigit() or int(num_riesgo) < 1 or int(num_riesgo) > 3:
                    print("Error: Elija un número entre 1 y 3.")
                    num_riesgo = input("Elija un número entre 1 y 3: ").strip()
                
                if int(num_riesgo) == 3:
                    riesgo = True
                    alarma = True
                    print("\n¡Elegiste el número equivocado! Alarma activada.")
            
            if not riesgo:
                cerraduras_abiertas += 1
                print(f"\n¡Éxito! Has abierto una cerradura ({cerraduras_abiertas}/3).")

    elif opcion_num == 2:
        forzar_seguidas = 0
        
        energia -= 10
        tiempo -= 3
        
        print("\nHackeando panel...")
        for paso in range(1, 5):
            codigo_parcial += "A"
            print(f"> Progreso {paso}/4: Código parcial = {codigo_parcial}")
            
        if len(codigo_parcial) >= 8:
            if cerraduras_abiertas < 3:
                cerraduras_abiertas += 1
                print("¡Código descifrado! Se abrió automáticamente 1 cerradura.")

    elif opcion_num == 3:
        forzar_seguidas = 0
        
        tiempo -= 1
        energia = min(100, energia + 15)
        
        if alarma:
            energia -= 10
            print("\nDescansaste, pero la alarma te causa tensión (-10 energía extra).")
        else:
            print("\nDescansaste y recuperaste energía.")

    if alarma and tiempo <= 3 and cerraduras_abiertas < 3:
        print("\n¡SISTEMA BLOQUEADO! La alarma bloqueó la bóveda por falta de tiempo.")
        break

print("\n================ FINAL DEL JUEGO ================")
if cerraduras_abiertas == 3:
    print(f"¡VICTORIA! El agente {agente} ha abierto la bóveda con éxito.")
elif alarma and tiempo <= 3:
    print("DERROTA: El sistema se ha bloqueado totalmente por la alarma.")
elif energia <= 0:
    print("DERROTA: Te has quedado sin energía.")
elif tiempo <= 0:
    print("DERROTA: Te has quedado sin tiempo.")
else:
    print("DERROTA: Misión fallida.")

#Ejercicio 5
nombre = input("Nombre del Gladiador: ").strip()
while not nombre.isalpha():
    print("Error: Solo se permiten letras.")
    nombre = input("Nombre del Gladiador: ").strip()

vida_jugador = 100
vida_enemigo = 100
pociones = 3
ataque_pesado_base = 15
ataque_enemigo_base = 12
turno_gladiador = True

print("\n=== INICIO DEL COMBATE ===")

while vida_jugador > 0 and vida_enemigo > 0:
    print(f"\n{nombre} (HP: {vida_jugador}) vs Enemigo (HP: {vida_enemigo}) | Pociones: {pociones}")
    print("Elige acción:")
    print("1. Ataque Pesado")
    print("2. Ráfaga Veloz")
    print("3. Curar")
    
    opcion = input("Opción: ").strip()
    while not opcion.isdigit() or int(opcion) not in [1, 2, 3]:
        print("Error: Ingrese un número válido (1, 2 o 3).")
        opcion = input("Opción: ").strip()
        
    opcion_num = int(opcion)
    
    if opcion_num == 1:
        if vida_enemigo < 20:
            dano_final = float(ataque_pesado_base * 1.5)
            print("¡Golpe Crítico!")
        else:
            dano_final = float(ataque_pesado_base)
            
        vida_enemigo -= int(dano_final)
        print(f"¡Atacaste al enemigo por {dano_final} puntos de daño!")
        
    elif opcion_num == 2:
        print(">> ¡Inicias una ráfaga de golpes!")
        for golpe in range(3):
            vida_enemigo -= 5
            print("> Golpe conectado por 5 de daño")
            
    elif opcion_num == 3:
        if pociones > 0:
            vida_jugador += 30
            pociones -= 1
            print(f"Te has curado 30 HP. Te quedan {pociones} pociones.")
        else:
            print("¡No quedan pociones!")

    if vida_enemigo > 0:
        vida_jugador -= ataque_enemigo_base
        print(f">> ¡El enemigo te atacó por {ataque_enemigo_base} puntos de daño!")

print("\n=== FIN DEL COMBATE ===")
if vida_jugador > 0:
    print(f"¡VICTORIA! {nombre} ha ganado la batalla.")
else:
    print("DERROTA. Has caído en combate.")