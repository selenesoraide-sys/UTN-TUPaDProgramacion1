#Ejercicio 1
# 1. Nombre del cliente
while True:
    nombre = input("Ingrese nombre del cliente: ")
    if nombre != "" and nombre.isalpha():
        break
    else:
        print("Error: solo letras y no vacío.")

# 2. Cantidad de productos
while True:
    cantidad = input("Ingrese cantidad de productos: ")
    if cantidad.isdigit() and int(cantidad) > 0:
        cantidad = int(cantidad)
        break
    else:
        print("Error: debe ser un número entero mayor a 0.")

total_sin_descuento = 0
total_con_descuento = 0

# 3. Cargar productos
for i in range(cantidad):
    print(f"\nProducto {i+1}")
    
    # Precio
    while True:
        precio = input("Ingrese precio: ")
        if precio.isdigit():
            precio = int(precio)
            break
        else:
            print("Error: debe ser un número entero.")
    
    total_sin_descuento += precio

    # Descuento
    while True:
        descuento = input("¿Tiene descuento? (S/N): ").lower()
        if descuento == "s" or descuento == "n":
            break
        else:
            print("Error: ingresar S o N.")
    
    if descuento == "s":
        precio_con_desc = precio * 0.9
    else:
        precio_con_desc = precio

    total_con_descuento += precio_con_desc

# 4. Resultados
ahorro = total_sin_descuento - total_con_descuento
promedio = total_con_descuento / cantidad

print("\n--- RESULTADOS ---")
print(f"Cliente: {nombre}")
print(f"Total sin descuentos: ${total_sin_descuento}")
print(f"Total con descuentos: ${total_con_descuento:.2f}")
print(f"Ahorro: ${ahorro:.2f}")
print(f"Promedio por producto: ${promedio:.2f}")

#Ejercicio 2

# Credenciales fijas
usuario_correcto = "alumno"
clave_correcta = "python123"

intentos = 0
acceso = False

# 1,2,3. Login con máximo 3 intentos
while intentos < 3:
    print(f"\nIntento {intentos + 1}/3")
    usuario = input("Usuario: ")
    clave = input("Clave: ")

    if usuario == usuario_correcto and clave == clave_correcta:
        print("Acceso concedido.")
        acceso = True
        break
    else:
        print("Error: credenciales inválidas.")
        intentos += 1

# Si falla 3 veces
if not acceso:
    print("Cuenta bloqueada.")
else:
    # 4. Menú repetitivo
    while True:
        print("\n1) Estado  2) Cambiar clave  3) Mensaje  4) Salir")
        
        opcion = input("Opción: ")

        # 5. Validación del menú
        if not opcion.isdigit():
            print("Error: ingrese un número válido.")
            continue

        opcion = int(opcion)

        if opcion < 1 or opcion > 4:
            print("Error: opción fuera de rango.")
            continue

        # Opciones
        if opcion == 1:
            print("Estado: Inscripto")

        elif opcion == 2:
            # Cambio de clave
            while True:
                nueva = input("Nueva clave: ")
                
                if len(nueva) < 6:
                    print("Error: mínimo 6 caracteres.")
                    continue

                confirmacion = input("Confirmar clave: ")

                if nueva != confirmacion:
                    print("Error: las claves no coinciden.")
                else:
                    clave_correcta = nueva
                    print("Clave cambiada con éxito.")
                    break

        elif opcion == 3:
            print("¡Seguí adelante, estás aprendiendo Python!")

        elif opcion == 4:
            print("Saliendo del sistema...")
            break



#Ejercicio 3 
# 1. Nombre del operador
while True:
    operador = input("Ingrese nombre del operador: ")
    if operador != "" and operador.isalpha():
        break
    else:
        print("Error: solo letras y no vacío.")

# Turnos (sin listas)
lunes1 = ""
lunes2 = ""
lunes3 = ""
lunes4 = ""

martes1 = ""
martes2 = ""
martes3 = ""

# Menú
while True:
    print("\n1) Reservar turno")
    print("2) Cancelar turno")
    print("3) Ver agenda del día")
    print("4) Ver resumen general")
    print("5) Cerrar sistema")

    opcion = input("Opción: ")

    if not opcion.isdigit():
        print("Error: ingrese un número válido.")
        continue

    opcion = int(opcion)

    if opcion < 1 or opcion > 5:
        print("Error: opción fuera de rango.")
        continue

    # 1. RESERVAR
    if opcion == 1:
        dia = input("Día (1=Lunes, 2=Martes): ")

        if not dia.isdigit() or int(dia) not in [1, 2]:
            print("Error: día inválido.")
            continue

        dia = int(dia)

        # Nombre paciente
        while True:
            paciente = input("Nombre del paciente: ")
            if paciente != "" and paciente.isalpha():
                break
            else:
                print("Error: solo letras.")

        # LUNES
        if dia == 1:
            # verificar repetido
            if paciente == lunes1 or paciente == lunes2 or paciente == lunes3 or paciente == lunes4:
                print("Error: paciente ya tiene turno ese día.")
            else:
                if lunes1 == "":
                    lunes1 = paciente
                elif lunes2 == "":
                    lunes2 = paciente
                elif lunes3 == "":
                    lunes3 = paciente
                elif lunes4 == "":
                    lunes4 = paciente
                else:
                    print("No hay turnos disponibles para Lunes.")

        # MARTES
        else:
            if paciente == martes1 or paciente == martes2 or paciente == martes3:
                print("Error: paciente ya tiene turno ese día.")
            else:
                if martes1 == "":
                    martes1 = paciente
                elif martes2 == "":
                    martes2 = paciente
                elif martes3 == "":
                    martes3 = paciente
                else:
                    print("No hay turnos disponibles para Martes.")

    # 2. CANCELAR
    elif opcion == 2:
        dia = input("Día (1=Lunes, 2=Martes): ")

        if not dia.isdigit() or int(dia) not in [1, 2]:
            print("Error: día inválido.")
            continue

        dia = int(dia)

        while True:
            paciente = input("Nombre del paciente a cancelar: ")
            if paciente != "" and paciente.isalpha():
                break
            else:
                print("Error: solo letras.")

        encontrado = False

        if dia == 1:
            if lunes1 == paciente:
                lunes1 = ""
                encontrado = True
            elif lunes2 == paciente:
                lunes2 = ""
                encontrado = True
            elif lunes3 == paciente:
                lunes3 = ""
                encontrado = True
            elif lunes4 == paciente:
                lunes4 = ""
                encontrado = True

        else:
            if martes1 == paciente:
                martes1 = ""
                encontrado = True
            elif martes2 == paciente:
                martes2 = ""
                encontrado = True
            elif martes3 == paciente:
                martes3 = ""
                encontrado = True

        if encontrado:
            print("Turno cancelado.")
        else:
            print("Paciente no encontrado.")

    # 3. VER AGENDA
    elif opcion == 3:
        dia = input("Día (1=Lunes, 2=Martes): ")

        if not dia.isdigit() or int(dia) not in [1, 2]:
            print("Error: día inválido.")
            continue

        dia = int(dia)

        if dia == 1:
            print("\nAgenda Lunes:")
            print("Turno 1:", lunes1 if lunes1 != "" else "(libre)")
            print("Turno 2:", lunes2 if lunes2 != "" else "(libre)")
            print("Turno 3:", lunes3 if lunes3 != "" else "(libre)")
            print("Turno 4:", lunes4 if lunes4 != "" else "(libre)")
        else:
            print("\nAgenda Martes:")
            print("Turno 1:", martes1 if martes1 != "" else "(libre)")
            print("Turno 2:", martes2 if martes2 != "" else "(libre)")
            print("Turno 3:", martes3 if martes3 != "" else "(libre)")

    # 4. RESUMEN
    elif opcion == 4:
        ocupados_lunes = 0
        ocupados_martes = 0

        if lunes1 != "": ocupados_lunes += 1
        if lunes2 != "": ocupados_lunes += 1
        if lunes3 != "": ocupados_lunes += 1
        if lunes4 != "": ocupados_lunes += 1

        if martes1 != "": ocupados_martes += 1
        if martes2 != "": ocupados_martes += 1
        if martes3 != "": ocupados_martes += 1

        disponibles_lunes = 4 - ocupados_lunes
        disponibles_martes = 3 - ocupados_martes

        print("\nResumen:")
        print(f"Lunes -> Ocupados: {ocupados_lunes}, Libres: {disponibles_lunes}")
        print(f"Martes -> Ocupados: {ocupados_martes}, Libres: {disponibles_martes}")

        if ocupados_lunes > ocupados_martes:
            print("Día con más turnos: Lunes")
        elif ocupados_martes > ocupados_lunes:
            print("Día con más turnos: Martes")
        else:
            print("Empate entre días.")

    # 5. SALIR
    elif opcion == 5:
        print("Sistema cerrado.")
        break

#Ejercicio 4
# Variables iniciales
energia = 100
tiempo = 12
cerraduras_abiertas = 0
alarma = False
codigo_parcial = ""

racha_forzar = 0  # para regla anti-spam

# Nombre del agente
while True:
    agente = input("Ingrese nombre del agente: ")
    if agente != "" and agente.isalpha():
        break
    else:
        print("Error: solo letras.")

# Juego principal
while energia > 0 and tiempo > 0 and cerraduras_abiertas < 3:

    print("\n--- ESTADO ---")
    print(f"Energía: {energia} | Tiempo: {tiempo} | Cerraduras: {cerraduras_abiertas} | Alarma: {alarma}")
    
    # Regla de bloqueo por alarma
    if alarma and tiempo <= 3 and cerraduras_abiertas < 3:
        print("¡Sistema bloqueado por alarma!")
        break

    print("\n1) Forzar cerradura")
    print("2) Hackear panel")
    print("3) Descansar")

    opcion = input("Opción: ")

    if not opcion.isdigit():
        print("Error: ingrese un número válido.")
        continue

    opcion = int(opcion)

    if opcion < 1 or opcion > 3:
        print("Error: opción fuera de rango.")
        continue

    # OPCIÓN 1: FORZAR
    if opcion == 1:
        racha_forzar += 1

        energia -= 20
        tiempo -= 2

        # Regla anti-spam
        if racha_forzar == 3:
            print("¡Forzaste demasiado! La cerradura se trabó.")
            alarma = True
            racha_forzar = 0
            continue

        # Riesgo de alarma
        if energia < 40:
            while True:
                riesgo = input("Riesgo! Elegí un número (1-3): ")
                if riesgo.isdigit() and int(riesgo) in [1,2,3]:
                    riesgo = int(riesgo)
                    break
                else:
                    print("Error: número inválido.")
            
            if riesgo == 3:
                alarma = True
                print("¡Se activó la alarma!")

        if not alarma:
            cerraduras_abiertas += 1
            print("Abriste una cerradura.")

    # OPCIÓN 2: HACKEAR
    elif opcion == 2:
        racha_forzar = 0
        energia -= 10
        tiempo -= 3

        print("Hackeando...")
        for i in range(4):
            codigo_parcial += "A"
            print(f"Progreso: {codigo_parcial}")

        if len(codigo_parcial) >= 8 and cerraduras_abiertas < 3:
            cerraduras_abiertas += 1
            print("¡Código completo! Se abrió una cerradura.")

    # OPCIÓN 3: DESCANSAR
    elif opcion == 3:
        racha_forzar = 0
        energia += 15
        if energia > 100:
            energia = 100

        tiempo -= 1

        if alarma:
            energia -= 10
            print("La alarma consume energía extra.")

        print("Descansaste.")

# RESULTADO FINAL
print("\n--- RESULTADO ---")

if cerraduras_abiertas == 3:
    print("🎉 ¡VICTORIA! Abriste la bóveda.")
elif energia <= 0 or tiempo <= 0:
    print("💀 DERROTA: te quedaste sin recursos.")
elif alarma and tiempo <= 3 and cerraduras_abiertas < 3:
    print("💀 DERROTA: sistema bloqueado por alarma.")
else:
    print("💀 DERROTA.")

#Ejercicio 5 
print("--- BIENVENIDO A LA ARENA ---")

# Nombre del gladiador
while True:
    nombre = input("Nombre del Gladiador: ")
    if nombre != "" and nombre.isalpha():
        break
    else:
        print("Error: Solo se permiten letras.")

# Variables iniciales
vida_jugador = 100
vida_enemigo = 100
pociones = 3

danio_pesado = 15
danio_enemigo = 12

turno_jugador = True  # boolean

print("\n=== INICIO DEL COMBATE ===")

# Ciclo principal
while vida_jugador > 0 and vida_enemigo > 0:

    print("\n=== NUEVO TURNO ===")
    print(f"{nombre} (HP: {vida_jugador}) vs Enemigo (HP: {vida_enemigo}) | Pociones: {pociones}")

    if turno_jugador:
        print("\nElige acción:")
        print("1. Ataque Pesado")
        print("2. Ráfaga Veloz")
        print("3. Curar")

        # Validación del menú
        while True:
            opcion = input("Opción: ")
            if opcion.isdigit() and int(opcion) in [1, 2, 3]:
                opcion = int(opcion)
                break
            else:
                print("Error: Ingrese un número válido.")

        # OPCIÓN 1: ATAQUE PESADO
        if opcion == 1:
            danio = danio_pesado

            if vida_enemigo < 20:
                danio = danio_pesado * 1.5  # float
                print("¡Golpe crítico!")

            vida_enemigo -= danio
            print(f"¡Atacaste al enemigo por {danio} puntos de daño!")

        # OPCIÓN 2: RÁFAGA
        elif opcion == 2:
            print(">> ¡Inicias una ráfaga de golpes!")
            for i in range(3):
                vida_enemigo -= 5
                print("> Golpe conectado por 5 de daño")

        # OPCIÓN 3: CURAR
        elif opcion == 3:
            if pociones > 0:
                vida_jugador += 30
                pociones -= 1
                print("¡Te curaste 30 HP!")
            else:
                print("¡No quedan pociones!")

        turno_jugador = False  # pasa turno

    # TURNO ENEMIGO
    else:
        if vida_enemigo > 0:  # solo ataca si sigue vivo
            vida_jugador -= danio_enemigo
            print(f">> ¡El enemigo contraataca por {danio_enemigo} puntos!")

        turno_jugador = True

# RESULTADO FINAL
print("\n=== FIN DEL COMBATE ===")

if vida_jugador > 0:
    print(f"¡VICTORIA! {nombre} ha ganado la batalla.")
else:
    print("DERROTA. Has caído en combate.")