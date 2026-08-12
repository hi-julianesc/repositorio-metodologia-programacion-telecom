
# Captura de datos básica
mensajeuser = input("Ingrese su nombre de usuario: ")
edaduser = int(input("Ingrese su edad: "))

# Muestra de datos usando f-string
print(f"Nombre de usuario ingresado: {mensajeuser} y su edad es: {edaduser}\n")


# Operaciones y Condicionales
a = 3
b = 2
suma = a + b
print(f"La suma de {a} + {b} es: {suma}")

if suma > 6:
    print("La suma dio mayor a 6")
elif suma == 5:
    print("La suma es igual a 5")
elif suma == 0:
    # Se corrigió la condición para verificar si es exactamente cero (== 0)
    print("La suma es igual a cero")
else:
    print("La suma dio menor a 6")

print()  # Línea en blanco para separar


# Bucles: FOR y WHILE (Ejemplo Simple)

# Ejemplo con FOR
print("--- Recorrido con FOR ---")
for i in range(1, 4):
    print(f"Número: {i}")

print()

# Ejemplo simple con WHILE al final
print("--- Recorrido con WHILE ---")
contador = 1
while contador <= 3:
    print(f"Contador: {contador}")
    contador += 1