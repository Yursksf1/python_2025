def ver_menu():
    print("Menú:")
    print("1. Opción 1")
    print("2. Opción 2")
    print("3. Opción 3")
    print("4. Salir")

while True:
    # Imprimir el menú
    ver_menu()
    # Solicitar al usuario que ingrese una opción
    opcion = input("Ingrese el número de opción que desea: ")
    # Procesar la opción seleccionada
    if opcion == "1":
        
        print("Ha seleccionado la Opción 1.")
    elif opcion == "2":
        print("Ha seleccionado la Opción 2.")
    elif opcion == "3":
        print("Ha seleccionado la Opción 3.")
    elif opcion == "4":
        print("Saliendo del programa ... ")
        break # Salir del ciclo while

    else:
        print("Opción inválida. Por favor, ingrese un número válido.")