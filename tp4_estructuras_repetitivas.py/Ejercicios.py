#Ejercicio1
for i in range(101):
    print(i)

#Ejercicio2
num = int(input("Ingrese un número: "))
print("Cantidad de dígitos:", len(str(abs(num))))

#Ejercicio3
a = int(input("Ingrese el primer número: "))
b = int(input("Ingrese el segundo número: "))
suma = 0
for i in range(a+1, b):
    suma += i
print("La suma es:", suma)

#Ejercicio4
suma = 0
while True:
    num = int(input("Ingrese un número (0 para terminar): "))
    if num == 0:
        break
    suma += num
print("Total acumulado:", suma)

#Ejercicio5
import random

secreto = random.randint(0, 9)
intentos = 0

while True:
    num = int(input("Adivine el número (0-9): "))
    intentos += 1
    if num == secreto:
        print(f"¡Correcto! Lo lograste en {intentos} intentos.")
        break


#Ejercicio6
for i in range(100, -1, -2):
    print(i)

#Ejercicio7
n = int(input("Ingrese un número positivo: "))
suma = 0
for i in range(n+1):
    suma += i
print("La suma es:", suma)

#Ejercicio8
n = 100
pares = impares = positivos = negativos = 0

for _ in range(n):
    num = int(input("Ingrese un número: "))
    if num % 2 == 0:
        pares += 1
    else:
        impares += 1
    if num > 0:
        positivos += 1
    elif num < 0:
        negativos += 1

print("Pares:", pares)
print("Impares:", impares)
print("Positivos:", positivos)
print("Negativos:", negativos)

#Ejercicio9

n = 100
suma = 0

for _ in range(n):
    num = int(input("Ingrese un número: "))
    suma += num

media = suma / n
print("La media es:", media)

#Ejercicio10
num = input("Ingrese un número: ")
invertido = num[::-1]
print("Número invertido:", invertido)