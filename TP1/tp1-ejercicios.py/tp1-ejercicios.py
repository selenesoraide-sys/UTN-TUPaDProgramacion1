# ejercicio 1 
print("Hola Mundo!")
#ejercicio 2
nombre = input("¿Cuál es tu nombre? ")
print(f"Hola {nombre}!")
#ejercicio 3
nombre = input("¿Cuál es tu nombre? ")
apellido = input("¿Cuál es tu apellido? ")
edad = input("¿Cuántos años tienes? ")
residencia = input("¿Dónde vives? ")
print(f"Soy {nombre} {apellido}, tengo {edad} años y vivo en {residencia}.")
#ejercicio 4
import math
radio = float(input("Ingrese el radio del círculo: "))
area = math.pi * radio ** 2
perimetro = 2 * math.pi * radio
print(f"El área del círculo es: {area:.2f}")
print(f"El perímetro del círculo es: {perimetro:.2f}")
# ejercicio 5 
segundos = int(input("Ingrese una cantidad de segundos: "))
horas = segundos / 3600
print(f"{segundos} segundos equivalen a {horas:.2f} horas.")
#ejercicio 6
numero = int(input("Ingrese un número para ver su tabla de multiplicar: "))
print(f"\nTabla de multiplicar del {numero}:\n")
for i in range(1, 11):
 resultado = numero * i
 print(f"{numero} x {i} = {resultado}")
#ejercicio 7
num2 = int(input("Ingrese el segundo número (distinto de 0): "))
# Verificamos que ninguno sea cero
if num1 != 0 and num2 != 0:
 suma = num1 + num2
 resta = num1 - num2
 multiplicacion = num1 * num2
 division = num1 / num2
 print(f"\nResultados entre {num1} y {num2}:")
 print(f"Suma: {suma}")
 print(f"Resta: {resta}")
 print(f"Multiplicación: {multiplicacion}")
 print(f"División: {division:.2f}")
else:
 print("Error: ambos números deben ser distintos de 0.")
 #ejercicio 8
 # Solicitar altura y peso al usuario
peso = float(input("Ingrese su peso en kilogramos (kg): "))
altura = float(input("Ingrese su altura en metros (m): "))
# Calcular el índice de masa corporal
imc = peso / (altura ** 2)
print(f"\nSu índice de masa corporal (IMC) es: {imc:.2f}")
#ejercicio 9
# Solicitar temperatura en grados Celsius
celsius = float(input("Ingrese la temperatura en grados Celsius: "))
# Convertir a Fahrenheit
fahrenheit = (9 / 5) * celsius + 32
# Mostrar resultado
print(f"{celsius}°C equivalen a {fahrenheit:.2f}°F.")
#ejercicio10 
num1 = float(input("Ingrese el primer número: "))
num2 = float(input("Ingrese el segundo número: "))
num3 = float(input("Ingrese el tercer número: "))
# Calcular el promedio
promedio = (num1 + num2 + num3) / 3
print(f"El promedio de los tres números es: {promedio:.2f}")