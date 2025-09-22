#Ejercicio1
edad = int(input("Ingrese su edad: "))
if edad > 18:
    print("Es mayor de edad")

#Ejercicio2 
nota = float(input("Ingrese su nota: "))
if nota >= 6:
    print("Aprobado")
else:
    print("Desaprobado")

#ejercicio3
numero = int(input("Ingrese un número: "))
if numero % 2 == 0:
    print("Ha ingresado un número par")
else:
    print("Por favor, ingrese un número par")

#ejercio4 
edad = int(input("Ingrese su edad: "))

if edad < 12:
    print("Niño/a")
elif 12 <= edad < 18:
    print("Adolescente")
elif 18 <= edad < 30:
    print("Adulto/a joven")
else:
    print("Adulto/a")

#ejercicio5 
contraseña = input("Ingrese una contraseña: ")

if 8 <= len(contraseña) <= 14:
    print("Ha ingresado una contraseña correcta")
else:
    print("Por favor, ingrese una contraseña de entre 8 y 14 caracteres")

#Ejercicios6
import random
from statistics import mode, median, mean

numeros_aleatorios = [random.randint(1, 100) for _ in range(50)]

moda = mode(numeros_aleatorios)
mediana = median(numeros_aleatorios)
media = mean(numeros_aleatorios)

print(f"Moda: {moda}, Mediana: {mediana}, Media: {media}")

if media > mediana > moda:
    print("Sesgo positivo o a la derecha")
elif media < mediana < moda:
    print("Sesgo negativo o a la izquierda")
elif media == mediana == moda:
    print("Sin sesgo")
else:
    print("Distribución no categorizada")

#ejercio7
frase = input("Ingrese una frase o palabra: ")

if frase[-1].lower() in "aeiou":
    frase += "!"
print(frase)

#ejercio8 
nombre = input("Ingrese su nombre: ")
opcion = int(input("Elija una opción (1: mayúsculas, 2: minúsculas, 3: primera letra mayúscula): "))

if opcion == 1:
    print(nombre.upper())
elif opcion == 2:
    print(nombre.lower())
elif opcion == 3:
    print(nombre.title())
else:
    print("Opción inválida")

#Ejercicio9
magnitud = float(input("Ingrese la magnitud del terremoto: "))

if magnitud < 3:
    print("Muy leve (imperceptible)")
elif 3 <= magnitud < 4:
    print("Leve (ligeramente perceptible)")
elif 4 <= magnitud < 5:
    print("Moderado (sentido por personas, pero generalmente no causa daños)")
elif 5 <= magnitud < 6:
    print("Fuerte (puede causar daños en estructuras débiles)")
elif 6 <= magnitud < 7:
    print("Muy fuerte (puede causar daños significativos)")
else:
    print("Extremo (puede causar graves daños a gran escala)")

#Ejercicio10
hemisferio = input("Ingrese su hemisferio (N/S): ").upper()
mes = int(input("Ingrese el mes (número): "))
dia = int(input("Ingrese el día: "))

def es_fecha_entre(dia, mes, inicio_dia, inicio_mes, fin_dia, fin_mes):
    if inicio_mes < fin_mes:
        return (mes == inicio_mes and dia >= inicio_dia) or (mes == fin_mes and dia <= fin_dia) or (inicio_mes < mes < fin_mes)
    else:
        # Para periodos que cruzan fin de año
        return (mes == inicio_mes and dia >= inicio_dia) or (mes == fin_mes and dia <= fin_dia) or (mes > inicio_mes or mes < fin_mes)

if hemisferio == "N":
    if es_fecha_entre(dia, mes, 21, 12, 20, 3):
        print("Invierno")
    elif es_fecha_entre(dia, mes, 21, 3, 20, 6):
        print("Primavera")
    elif es_fecha_entre(dia, mes, 21, 6, 20, 9):
        print("Verano")
    elif es_fecha_entre(dia, mes, 21, 9, 20, 12):
        print("Otoño")
    else:
        print("Fecha no válida")
elif hemisferio == "S":
    if es_fecha_entre(dia, mes, 21, 12, 20, 3):
        print("Verano")
    elif es_fecha_entre(dia, mes, 21, 3, 20, 6):
        print("Otoño")
    elif es_fecha_entre(dia, mes, 21, 6, 20, 9):
        print("Invierno")
    elif es_fecha_entre(dia, mes, 21, 9, 20, 12):
        print("Primavera")
    else:
        print("Fecha no válida")
else:
    print("Hemisferio inválido")