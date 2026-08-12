# Taller 2: Sistema de Gestión de Dispositivos - Modularizado con Funciones

def agregar_dispositivo():
    pass

def eliminar_dispositivo():
    """Muestra la opción de eliminar un dispositivo existente."""
    print("\n[INFO] Opción seleccionada: Eliminar dispositivo")

def modificar_dispositivo():
    """Muestra la opción de modificar los datos de un dispositivo."""
    print("\n[INFO] Opción seleccionada: Modificar dispositivo")

def listar_dispositivos():
    """Muestra la opción de listar todos los dispositivos."""
    print("\n[INFO] Opción seleccionada: Listar todos los dispositivos")

def mostrar_menu():
    """Despliega las opciones del menú principal en pantalla."""
    print("\n=== SISTEMA DE GESTIÓN DE DISPOSITIVOS ===")
    print("1. Agregar dispositivo")
    print("2. Eliminar dispositivo")
    print("3. Modificar dispositivo")
    print("4. Listar todos los dispositivos")
    print("5. Salir")
    print("==========================================")

def ejecutar_sistema():
    """Función principal que controla el flujo de la aplicación."""
    opcion = ""
    
    while opcion != "5":
        mostrar_menu()
        opcion = input("Seleccione una opción (1-5): ")

        if opcion == "1":
            agregar_dispositivo()
        elif opcion == "2":
            eliminar_dispositivo()
        elif opcion == "3":
            modificar_dispositivo()
        elif opcion == "4":
            listar_dispositivos()
        elif opcion == "5":
            print("\n[INFO] Saliendo del programa... ¡Hasta luego!")
        else:
            print("\n[ERROR] Opción no válida. Por favor, ingrese un número del 1 al 5.")

# Punto de entrada de la aplicación
if __name__ == "__main__":
    ejecutar_sistema()