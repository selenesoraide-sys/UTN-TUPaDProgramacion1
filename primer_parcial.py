#Primer Parcial – Programación 1
#Alumno: Selene Carolina Soraide Aramayo 
#Enunciado
#La biblioteca escolar necesita un sistema de gestión sencillo para su catálogo de libros y las
#copias disponibles. Se pide desarrollar un programa con una interfaz basada en menú que
#utilice listas paralelas (una para titulos[] y otra para ejemplares[]). Cada título debe estar
#vinculado a su número correspondiente de copias utilizando el mismo índice en ambas listas.
#Se debe utilizar un bucle while para navegar por las opciones del menú hasta que el usuario
#elija salir

#Biblioteca escolar


titulos = []
ejemplares = []


opcion = 0

while opcion != 8:
    print("\n--- MENÚ DE LA BIBLIOTECA ---")
    print("1. Ingresar títulos")
    print("2. Ingresar ejemplares")
    print("3. Mostrar catálogo")
    print("4. Consultar disponibilidad")
    print("5. Listar agotados")
    print("6. Agregar título")
    print("7. Actualizar ejemplares (préstamo/devolución)")
    print("8. Salir")

    opcion = input("Seleccione una opción: ")

    if opcion.isdigit():
        opcion = int(opcion)
    else:
        print("Debe ingresar un número válido.")
        continue

    #1 Ingresar títulos
    if opcion == 1:
        cantidad = input("¿Cuántos títulos desea ingresar?: ")
        if cantidad.isdigit():
            cantidad = int(cantidad)
            for i in range(cantidad):
                titulo = input(f"Ingrese el título {i+1}: ")
                titulos.append(titulo)
                ejemplares.append(0)  # Inicializa en 0 hasta que se carguen ejemplares
        else:
            print("Debe ingresar un número válido.")

    #2 Ingresar ejemplares
    elif opcion == 2:
        if len(titulos) == 0:
            print("Primero debe ingresar títulos (opción 1).")
        else:
            for i in range(len(titulos)):
                cantidad = input(f"Ingrese cantidad de ejemplares para '{titulos[i]}': ")
                if cantidad.isdigit():
                    ejemplares[i] = int(cantidad)
                else:
                    print("Debe ingresar un número válido.")

    #3 Mostrar catálogo
    elif opcion == 3:
        if len(titulos) == 0:
            print("No hay libros en el catálogo.")
        else:
            print("\n--- Catálogo ---")
            for i in range(len(titulos)):
                print(f"{titulos[i]} -> {ejemplares[i]} ejemplares")

    #4 Consultar disponibilidad
    elif opcion == 4:
        buscar = input("Ingrese el título a buscar: ")
        if buscar in titulos:
            indice = titulos.index(buscar)
            print(f"'{buscar}' tiene {ejemplares[indice]} ejemplares disponibles.")
        else:
            print("El título no se encuentra en el catálogo.")

    #5 Listar agotados
    elif opcion == 5:
        print("\n--- Libros Agotados ---")
        agotados = False
        for i in range(len(titulos)):
            if ejemplares[i] == 0:
                print(titulos[i])
                agotados = True
        if not agotados:
            print("No hay libros agotados.")

    #6 Agregar título
    elif opcion == 6:
        nuevo_titulo = input("Ingrese el nuevo título: ")
        cantidad = input("Ingrese la cantidad de ejemplares: ")
        if cantidad.isdigit():
            titulos.append(nuevo_titulo)
            ejemplares.append(int(cantidad))
            print("Título agregado con éxito.")
        else:
            print("Cantidad inválida, no se agregó el título.")

    #7 Actualizar ejemplares (préstamo/devolución)
    elif opcion == 7:
        if len(titulos) == 0:
            print("No hay títulos cargados.")
        else:
            for i in range(len(titulos)):
                print(f"{i+1}. {titulos[i]} ({ejemplares[i]} ejemplares)")
            seleccion = input("Seleccione el número del libro a modificar: ")
            if seleccion.isdigit():
                seleccion = int(seleccion) - 1
                if 0 <= seleccion < len(titulos):
                    accion = input("¿Desea registrar un préstamo (p) o devolución (d)?: ").lower()
                    if accion == "p":
                        if ejemplares[seleccion] > 0:
                            ejemplares[seleccion] -= 1
                            print("Préstamo registrado.")
                        else:
                            print("No hay ejemplares disponibles para préstamo.")
                    elif accion == "d":
                        ejemplares[seleccion] += 1
                        print("Devolución registrada.")
                    else:
                        print("Opción inválida.")
                else:
                    print("Selección inválida.")
            else:
                print("Debe ingresar un número válido.")

    #8 Salir
    elif opcion == 8:
        print("Saliendo del sistema...")

    else:
        print("Opción no válida, intente de nuevo.")