# Taller 1: Sistema de Gestión de Dispositivos - Menú Básico

opcion = ""

while opcion != "5":
    print("\n=== SISTEMA DE GESTIÓN DE DISPOSITIVOS ===")
    print("1. Agregar dispositivo")
    print("2. Eliminar dispositivo")
    print("3. Modificar dispositivo")
    print("4. Listar todos los dispositivos")
    print("5. Salir")
    print("==========================================")
    
    opcion = input("Seleccione una opción (1-5): ")

    if opcion == "1":
        print("\n[INFO] Opción seleccionada: Agregar dispositivo")
    elif opcion == "2":
        print("\n[INFO] Opción seleccionada: Eliminar dispositivo")
    elif opcion == "3":
        print("\n[INFO] Opción seleccionada: Modificar dispositivo")
    elif opcion == "4":
        print("\n[INFO] Opción seleccionada: Listar todos los dispositivos")
    elif opcion == "5":
        print("\n[INFO] Saliendo del programa... ¡Hasta luego!")
    else:
        print("\n[ERROR] Opción no válida. Por favor, ingrese un número del 1 al 5.")