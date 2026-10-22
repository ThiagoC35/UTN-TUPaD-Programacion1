#Ejercicio 1

a = 10
b = input("Introduce un número: ")

# Error: TypeError. 'b' es un string devuelto por input() y no se puede 
# dividir directamente un entero ('a') entre una cadena de texto sin convertirlo.
result = a / b  

print(f"Resultado: {result}")

numbers = [1, 2, 3]

# Error: IndexError. Se intenta acceder al índice 5 de la lista 'numbers', 
# pero la lista solo tiene elementos en los índices 0, 1 y 2.
print(numbers[5])

#Ejercicio 2

a = 10
b = input("Introduce un número: ")

# Convertimos 'b' a entero (o float) para evitar el TypeError
result = a / int(b)  
print(f"Resultado: {result}")

numbers = [1, 2, 3]

# Corregimos el índice para que esté dentro de los límites de la lista (ej: índice 2)
print(numbers[2])

#Ejercicio 3

try:
    a = 10
    b = input("Introduce un número: ")
    
    # Mantenemos el código propenso a error (TypeError si b es string)
    result = a / b  
    print(f"Resultado: {result}")

    numbers = [1, 2, 3]
    print(numbers[5])  # IndexError
    
except:
    print("¡Atención! Ocurrió un error durante la ejecución del programa.")

#Ejercicio 4
try:
    a = 10
    b = input("Introduce un número: ")
    
    result = a / b  # Provoca TypeError si ingresas texto
    print(f"Resultado: {result}")

    numbers = [1, 2, 3]
    print(numbers[5])  # Provoca IndexError

except TypeError:
    print("Error: Operación entre tipos de datos incompatibles (intentaste operar con un string).")
except IndexError:
    print("Error: Se intentó acceder a un índice que no existe en la lista.")
except Exception as e:
    print(f"Ocurrió otro error inesperado: {type(e).__name__}")

#Ejercicio 5
try:
    a = 10
    # Para probar el flujo sin error en este ejercicio, convertimos b correctamente
    b = int(input("Introduce un número entero distinto de cero: "))
    result = a / b  
    print(f"Resultado: {result}")

    numbers = [1, 2, 3]
    print(numbers[2])  # Índice válido

except TypeError:
    print("Error: Operación entre tipos de datos incompatibles.")
except ZeroDivisionError:
    print("Error: No se puede dividir un número entre cero.")
except IndexError:
    print("Error: Índice fuera de los límites de la lista.")
else:
    print("¡Éxito! El código se ejecutó completamente sin registrar ningún error.")
finally:
    print("Proceso finalizado (Bloque finally ejecutado).")

#Ejercicio 6
try:
    # Intentamos convertir la entrada directamente a float
    numero = float(input("Ingrese un número: "))
    print(f"El valor ingresado es válido: {numero}")
    
except ValueError:
    print("Debe ingresar un número válido")
except Exception as e:
    print(f"Se produjo un error inesperado: {type(e).__name__}")

#Ejercicio 7
while True:
    try:
        numero = float(input("Ingrese un número: "))
        print(f"¡Número ingresado correctamente!: {numero}")
        break  # Rompe el bucle si la entrada fue exitosa
        
    except ValueError:
        print("Debe ingresar un número válido. Intente nuevamente.")
    except Exception as e:
        print(f"Se produjo un error inesperado: {type(e).__name__}. Intente nuevamente.")

