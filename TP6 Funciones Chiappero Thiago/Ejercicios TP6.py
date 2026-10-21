#Ejercicio 1
def imprimir_hola_mundo():
    print("Hola Mundo!")
imprimir_hola_mundo()

#Ejercicio 2
def saludar_usuario(nombre):
    return (f"Hola {nombre}! como estas?")

solicitar_nombre = input("Ingrese un nombre: ")
print(saludar_usuario(solicitar_nombre))

#Ejercicio 3
def informacion_personal(nombre, apellido, edad, residencia):
    return f"Soy {nombre} {apellido}, tengo {edad} años y vivo en {residencia}."

solicitar_nombre = input("Ingrese su nombre:" )
solicitar_apellido = input("Ingrese su apellido:" )
solicitar_edad = int(input("Ingrese su edad:" ))
solicitar_residencia = input("Ingrese su residencia:" )
print(informacion_personal(solicitar_nombre, solicitar_apellido, solicitar_edad, solicitar_residencia))

#Ejercicio 4
import math

def calcular_area_circulo(radio):
    area = math.pi * radio ** 2
    return area

def calcular_perimetro_circulo(radio):
    perimetro = 2 * math.pi * radio
    return perimetro

solicitar_radio = float(input("Ingrese el radio del circulo: "))

print("El área del círculo es:", calcular_area_circulo(solicitar_radio))
print("El perímetro del círculo es:", calcular_perimetro_circulo(solicitar_radio))

#Ejercicio 5
def segundos_a_horas(segundos):
    horas = segundos / 3600
    return horas

solicitar_segundos = int(input("Ingrese la cantidad de segundos: "))
resultado = segundos_a_horas(solicitar_segundos)
print(f"La cantidad de horas correspondientes es: {resultado:.2f}")

#Ejercicio 6
def tabla_multiplicar(numero):
    for i in range(1, 11):
        resultado = numero * i
        print(f"{numero} x {i} = {resultado}")

pedir_numero = int(input("Ingrese un numero para ver su tabla: "))
tabla_multiplicar(pedir_numero)


#Ejercicio 7
def operaciones_basicas(a, b):
    suma = a + b
    resta = a - b
    multiplicacion = a * b
    division = a / b
    if b != 0:
        division = a / b
    else:
        division = "No se puede dividir por cero."
    return (suma, resta, multiplicacion, division)

ingresar_numero1 = int(input("Ingrese el primer numero: "))
ingresar_numero2 = int(input("Ingrese el segundo numero: "))

resultados = operaciones_basicas(ingresar_numero1, ingresar_numero2)
print(f"Suma: {resultados[0]}")
print(f"Resta: {resultados[1]}")
print(f"Multiplicación: {resultados[2]}")
print(f"División: {resultados[3]}")

#Ejercicio 8
def calcular_imc(peso, altura):
    imc = peso / (altura ** 2)
    return imc

peso = float(input("Ingrese su peso en kilogramos: "))
altura = float(input("Ingrese su altura en metros: "))

resultado_imc = calcular_imc(peso,altura)

print(f"Su índice de masa corporal (IMC) es: {resultado_imc:.2f}")

#Ejercicio 9
def celsius_a_fahrenheit(celsius):
    fahrenheit = (celsius * 9/5) + 32
    return fahrenheit

ingresar_temperatura_celsius = float(input("Ingrese la temperatura en grados Celsius: "))

resultado_fahrenheit = celsius_a_fahrenheit(ingresar_temperatura_celsius)
print("La temperatura en grados Fahrenheit es: ", resultado_fahrenheit)

#Ejercicio 10
def calcular_promedio(a, b, c):
    promedio = (a + b+ c) / 3
    return promedio

ingresar_numero1 = float(input("Ingrese el primer numero: "))
ingresar_numero2 = float(input("Ingrese el segundo numero: "))
ingrese_numero3 = float(input("Ingrese el tercer numero: "))

resultado_promedio = calcular_promedio(ingresar_numero1, ingresar_numero2, ingrese_numero3)
print("El promedio de los tres números es: {:.2f}".format(resultado_promedio))