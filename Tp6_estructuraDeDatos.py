#Ejercicio 1 
precios_frutas = {
    'Banana': 1200,
    'Ananá': 2500,
    'Melón': 3000,
    'Uva': 1450
}
#agregamos 
precios_frutas['Naranja'] = 1200
precios_frutas['Manzana'] = 1500
precios_frutas['Pera'] = 2300

#Ejercicio 2 
precios_frutas['Banana'] = 1330
precios_frutas['Manzana'] = 1700
precios_frutas['Melón'] = 2800

# Ejercicio  
lista_frutas = list(precios_frutas.keys()) 

# Ejercicio 4 
# # Crear diccionario vacío
agenda = {}

# Cargar 5 contactos
print("Cargá 5 contactos telefónicos:")
for i in range(5):
    nombre = input(f"Ingresá el nombre del contacto {i+1}: ")
    numero = input(f"Ingresá el número de {nombre}: ")
    agenda[nombre] = numero  # Guardamos nombre → número
    print()

# Consultar un número
buscado = input("Ingresá el nombre que querés buscar: ")

if buscado in agenda:
    print(f"El número de {buscado} es: {agenda[buscado]}")
else:
    print(f"No se encontró el contacto '{buscado}'.")


#Ejercicio 5  

frase = input("Ingresá una frase: ")


palabras = frase.split()


palabras_unicas = set(palabras)
print("\nPalabras únicas:")
print(palabras_unicas)


conteo = {}

for palabra in palabras:
    if palabra in conteo:
        conteo[palabra] += 1
    else:
        conteo[palabra] = 1

print("\nCantidad de apariciones de cada palabra:")
print(conteo)

# Ejercicio 6 
alumnos = {}


for i in range(3):
    nombre = input(f"Ingresá el nombre del alumno {i+1}: ")
    
    print(f"Ingresá las 3 notas de {nombre}:")
    n1 = float(input("Nota 1: "))
    n2 = float(input("Nota 2: "))
    n3 = float(input("Nota 3: "))
    
    alumnos[nombre] = (n1, n2, n3) 
    print()


print("Promedios de cada alumno:")
for nombre, notas in alumnos.items():
    promedio = sum(notas) / 3
    print(f"{nombre}: {promedio:.2f}")

#Ejercicio 7

# Ejemplo de sets de estudiantes (podés reemplazar por los que quieras)
parcial1 = {101, 102, 103, 104, 105}
parcial2 = {103, 104, 106, 107}

# 1) Estudiantes que aprobaron ambos parciales (intersección)
ambos = parcial1 & parcial2
print("Aprobaron ambos parciales:", ambos)

# 2) Estudiantes que aprobaron solo uno (diferencia simétrica)
solo_uno = parcial1 ^ parcial2
print("Aprobaron solo uno:", solo_uno)

# 3) Estudiantes que aprobaron al menos un parcial (unión)
al_menos_uno = parcial1 | parcial2
print("Aprobaron al menos un parcial:", al_menos_uno)


#Ejercicio 8

stock = {
    "leche": 20,
    "pan": 50,
    "huevos": 30,
    "arroz": 15
}

producto = input("Ingresá el producto que querés consultar o agregar: ").lower()

if producto in stock:
    print(f"El stock actual de {producto} es: {stock[producto]} unidades")
    
    agregar = input("¿Querés agregar unidades a este producto? (si/no): ").lower()
    
    if agregar == "si":
        cantidad = int(input("¿Cuántas unidades querés agregar?: "))
        stock[producto] += cantidad
        print(f"Nuevo stock de {producto}: {stock[producto]} unidades")

else:
    print(f"El producto '{producto}' no existe.")
    agregar_nuevo = input("¿Querés agregarlo al stock? (si/no): ").lower()
    
    if agregar_nuevo == "si":
        cantidad = int(input("Ingresá la cantidad inicial de stock: "))
        stock[producto] = cantidad
        print(f"Producto agregado: {producto} → {cantidad} unidades")

print("\nStock final:")
print(stock)

#Ejercicio 9 
agenda = {}


for i in range(3):
    dia = input("Ingresá el día (por ejemplo 'Lunes'): ")
    hora = input("Ingresá la hora (por ejemplo '14:00'): ")
    evento = input("Ingresá el evento: ")
    
    clave = (dia, hora)      
    agenda[clave] = evento

    print()


print("Agenda cargada:")
for clave, evento in agenda.items():
    dia, hora = clave
    print(f"{dia} a las {hora}: {evento}")

 #Ejercio 10 

paises = {
    "Argentina": "Buenos Aires",
    "Chile": "Santiago",
    "Brasil": "Brasilia",
    "Uruguay": "Montevideo"
}

paises_invertido = {}

for pais, capital in paises.items():
    paises_invertido[capital] = pais

