#Ejercicio 1

edad = int(input("Ingrese su edad: "))
if edad > 18:
    print("Es mayor de edad")

#Ejercicio 2
nota = int(input("Ingrese su nota: "))
if nota >= 6:
    print("Aprobado")
else:
    print("Desaprobado")

#Ejercicio 3
numero = int(input("Ingrese un numero: "))
if numero % 2 == 0:
    print("Ha ingresado un numero par")
else:
    print("Por favor, ingrese un numero par")

#Ejercicio 4
edad = int(input("Ingrese su edad: "))
if edad < 12:
    print("Eres un niño/a")
elif edad >= 12 and edad < 18:
    print("Eres un adolescente")
elif edad >= 18 and edad < 30:
    print("Eres un adulto/a joven")
elif edad >= 30:
    print("Eres un adulto/a")

#Ejercicio 5
contraseña = input("Ingrese una contraseña de entre 8 y 14 caracteres: ")
if 8 <= len(contraseña) <= 14:
    print("Ha ingresado una contraseña correcta")
else:
    print("Por favor, ingrese una contraseña de entre 8 y 14 caracteres")

#Ejercicio 6
consumo = int(input("Ingrese su consumo mensual en kWh: "))
if consumo < 150:
    print("Consumo bajo.")
elif consumo >= 150 and consumo <= 300:
    print("Consumo medio.")
else:
    print("Consumo alto.")

if consumo > 500:
    print("Considere medidas de ahorro energético.")

#Ejercicio 7
frase = input("Por favor, ingrese una frase o palabra: ")
if frase[-1] in "aeiouAEIOU":
    print(f"{frase}!")
else:
    print(f"{frase}")

#Ejercicio 8
nombre = input("Ingrese su nombre: ")

print("""Este programa puede realizar las siguientes operaciones: 
1. Si quiere su nombre en mayusculas.
2. Si quiere su nombre en minusculas.
3. Si quiere su nombre con la primer letra en mayuscula.""")

opcion = int(input("Ingrese la opcion que desea realizar: "))

if opcion == 1:
    print(nombre.upper())
elif opcion == 2:
    print(nombre.lower())
elif opcion == 3:
    print(nombre.title())

#Ejercicio 9
magnitud = float(input("Ingrese la magnitud de un terremoto: "))
if magnitud < 3.0:
    print("Muy leve")
elif magnitud >= 3.0 and magnitud < 4.0:
    print("Leve")
elif magnitud >= 4.0 and magnitud < 5.0:
    print("Moderado")
elif magnitud >= 5.0 and magnitud < 6.0:
    print("Fuerte")
elif magnitud >= 6.0 and magnitud < 7.0:
    print("Muy fuerte")
elif magnitud >= 7.0:
    print("Extremo")

#Ejercicio 10
hemisferio = input("Por favor, ingrese el hemisferio (N/S): ")
hemisferio = hemisferio.lower()

mes = int(input("Por favor, ingrese el mes del año en números: "))

dia = int(input("Por favor, ingrese el día del mes en números: "))


if hemisferio == "s":
  if (mes == 12 and dia >= 21) or (mes in (1,2)) or (mes == 3 and dia <= 20):
    print("Verano")
  elif (mes == 3 and dia >= 21) or (mes in (4,5)) or (mes == 6 and dia <= 20):
    print("Otoño")
  elif (mes == 6 and dia >= 21) or (mes in (7,8)) or (mes == 9 and dia <= 20):
    print("Invierno")
  elif (mes == 9 and dia >= 21) or (mes in (10,11)) or (mes == 12 and dia <= 20):
    print("Primavera")

elif hemisferio == "n":
  if (mes == 12 and dia >= 21) or (mes in (1,2)) or (mes == 3 and dia <= 20):
    print("Invierno")
  elif (mes == 3 and dia >= 21) or (mes in (4,5)) or (mes == 6 and dia <= 20):
    print("Primavera")
  elif (mes == 6 and dia >= 21) or (mes in (7,8)) or (mes == 9 and dia <= 20):
    print("Verano")
  elif (mes == 9 and dia >= 21) or (mes in (10,11)) or (mes == 12 and dia <= 20):
    print("Otoño")