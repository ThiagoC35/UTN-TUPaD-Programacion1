#Ejercicio 1

print("Hola Mundo!")

#Ejercicio 2
nombre = input("Ingrese su nombre: ")
print(f"¡Hola, {nombre}!")

#Ejercicio 3
nombre = input("Ingrese su nombre: ")
apellido = input("Ingrese su apellido: ")
edad = int(input("Ingrese su edad: "))
residencia = input("Ingrese su lugar de residencia: ")
print(f"Soy {nombre} {apellido}, tengo {edad} años y vivo en {residencia}.")

#Ejercicio 4
radio = float(input("Ingrese el radio de un circulo: "))
area = 3.14159 * radio ** 2
perimetro = 2 * 3.14159 * radio
print(f"El area del circulo es: {area} y el perimetro del circulo es: {perimetro}")

#Ejercicio 5
segundos = int(input("Ingrese una cantidad de segundos: "))
horas = segundos / 3600
print(f"Cantidad de horas: {horas}")

#Ejercicio 6
numero = int(input("Ingrese un numero: "))
for i in range(1, 11):
    resultado = numero * i
    print(f"{numero} x {i} = {resultado}")

#Ejercicio 7
numero1 = int(input("Ingrese el primer numero: "))
numero2 = int(input("Ingrese el segundo numero: "))
suma = numero1 + numero2
resta = numero1 - numero2
multiplicacion = numero1 * numero2
division = numero1 / numero2
print("Suma:", suma)
print("Resta:", resta)
print("Multiplicacion:", multiplicacion)
print("Division:", division)

#Ejercicio 8
altura = float(input("Ingrese su altura en metros: "))
peso = float(input("Ingrese su peso en kg: "))
imc = peso / (altura ** 2)
print(f"Su indice de masa corporal (IMC) es: {imc}")

#Ejercicio 9 
celsius = float(input("Ingrese la temperatura en grados Celsius: "))
fahrenheit = (celsius * 9/5) + 32
print(f"{celsius} grados Celsius son {fahrenheit} grados Fahrenheit.")

#Ejercicio 10
numero1 = int(input("Ingrese el primer numero: "))
numero2 = int(input("Ingrese el segundo numero: "))
numero3 = int(input("Ingrese el tercer numero: "))
promedio = (numero1 + numero2 + numero3) / 3
print(f"El promedio de los tres numeros es: {promedio}")


