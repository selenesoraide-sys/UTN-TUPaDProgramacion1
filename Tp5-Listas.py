#Ejercicio1 
notas = [7.5, 8.0, 9.1, 6.8, 5.5, 10.0, 4.7, 8.5, 9.8, 7.3]

print("Notas de los estudiantes:")
for n in notas:
    print(n)

# Calculo de promedio
suma = 0
for n in notas:
    suma += n
promedio = suma / len(notas)

# Máxima y mínima
nota_max = max(notas)
nota_min = min(notas)

print("\nPromedio:", promedio)
print("Nota más alta:", nota_max)
print("Nota más baja:", nota_min)

#Ejercicio2 
productos = []
for i in range(5):
    prod = input(f"Ingrese el producto {i+1}: ")
    productos.append(prod)

print("\nLista ordenada:", sorted(productos))

eliminar = input("¿Qué producto desea eliminar?: ")
if eliminar in productos:
    productos.remove(eliminar)
else:
    print("Ese producto no está en la lista.")

print("Lista actualizada:", productos)

#Ejercicio3 
numeros = [random.randint(1, 100) for _ in range(15)]
pares = []
impares = []

for n in numeros:
    if n % 2 == 0:
        pares.append(n)
    else:
        impares.append(n)

print("Lista completa:", numeros)
print("Pares:", pares, "Cantidad:", len(pares))
print("Impares:", impares, "Cantidad:", len(impares))

#Ejercicio4 
valores = [1, 2, 2, 3, 4, 4, 5, 1, 6, 3]

sin_repetidos = []
for v in valores:
    if v not in sin_repetidos:
        sin_repetidos.append(v)

print("Lista original:", valores)
print("Lista sin repetidos:", sin_repetidos) 

#Ejercio5 

estudiantes = ["Julian", "Marcos", "Carolina", "Martín", "Valeria", "Pedro", "Micaela", "Juan"]

print("Lista actual:", estudiantes)
accion = input("¿Desea 'agregar' o 'eliminar' un estudiante?: ")

if accion.lower() == "agregar":
    nuevo = input("Ingrese el nombre del estudiante a agregar: ")
    estudiantes.append(nuevo)
elif accion.lower() == "eliminar":
    borrar = input("Ingrese el nombre del estudiante a eliminar: ")
    if borrar in estudiantes:
        estudiantes.remove(borrar)
    else:
        print("Ese estudiante no está en la lista.")
else:
    print("Acción no reconocida.")

print("Lista final:", estudiantes)

#Ejercicio6 

numeros = [1, 2, 3, 4, 5, 6, 7]
print("Lista original:", numeros)

ultimo = numeros[-1]
for i in range(len(numeros)-1, 0, -1):
    numeros[i] = numeros[i-1]
numeros[0] = ultimo

print("Lista rotada:", numeros)

#Ejercicio7 

temperaturas = [
    [10, 20],
    [12, 25],
    [8, 18],
    [14, 28],
    [11, 22],
    [9, 19],
    [13, 27]
]

suma_min, suma_max = 0, 0
amplitudes = []

for dia in temperaturas:
    suma_min += dia[0]
    suma_max += dia[1]
    amplitudes.append(dia[1] - dia[0])

prom_min = suma_min / len(temperaturas)
prom_max = suma_max / len(temperaturas)
dia_max_amp = amplitudes.index(max(amplitudes)) + 1

print("Promedio mínimas:", prom_min)
print("Promedio máximas:", prom_max)
print("Día con mayor amplitud térmica:", dia_max_amp)

#Ejercicio8 

notas = [
    [7, 8, 9],
    [6, 5, 7],
    [9, 9, 10],
    [4, 6, 5],
    [8, 7, 6]
]

#Promedio por estudiante
print("Promedio por estudiante:")
for i, fila in enumerate(notas):
    prom = sum(fila) / len(fila)
    print(f"Estudiante {i+1}: {prom:.2f}")

#Promedio por materia
print("\nPromedio por materia:")
for col in range(3):
    suma = 0
    for fila in notas:
        suma += fila[col]
    prom = suma / len(notas)
    print(f"Materia {col+1}: {prom:.2f}")

#Ejercicio9 

tablero = [["-" for _ in range(3)] for _ in range(3)]

def mostrar_tablero():
    for fila in tablero:
        print(" ".join(fila))
    print()

turno = "X"
for _ in range(5):  # máximo 5 turnos X y O (ejemplo corto)
    mostrar_tablero()
    fila = int(input(f"Jugador {turno}, ingrese fila (0-2): "))
    col = int(input(f"Jugador {turno}, ingrese columna (0-2): "))
    if tablero[fila][col] == "-":
        tablero[fila][col] = turno
        turno = "O" if turno == "X" else "X"
    else:
        print("Casilla ocupada. Intente de nuevo.")

#Ejercicio10 

ventas = [
    [5, 7, 3, 4, 6, 8, 2],   # Producto1
    [2, 3, 4, 1, 5, 6, 7],   # Producto2
    [10, 8, 6, 4, 7, 9, 5],  # Producto3
    [1, 2, 3, 2, 4, 3, 2]    # Producto4
]

# Total por producto
print("Total vendido por producto:")
for i, fila in enumerate(ventas):
    print(f"Producto {i+1}: {sum(fila)}")

# Día con mas ventas
totales_dias = [sum(col) for col in zip(*ventas)]
dia_max = totales_dias.index(max(totales_dias)) + 1
print("\nDía con mayores ventas:", dia_max)

# Producto más vendido en la semana
totales_productos = [sum(fila) for fila in ventas]
prod_max = totales_productos.index(max(totales_productos)) + 1
print("Producto más vendido:", prod_max)