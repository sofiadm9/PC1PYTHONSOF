# Obtener los dos números del usuario.
num1 = float(input("Ingrese el primer número: "))
num2 = float(input("Ingrese el segundo número: "))

# Mostrar el menú
print("\nElija una opción:")
print("1. Suma")
print("2. Diferencia (primer número menos segundo número)")
print("3. Producto")

# Obtener la elección del usuario
elección = int(input("Ingrese su elección (1, 2 o 3): "))

# Realizar la operación elegida
if elección == 1:
    resultado = num1 + num2
elif elección == 2:
    resultado = num1 - num2
elif elección == 3:
    resultado = num1 * num2
else:
    print("Elección no válida!")
    resultado = None

# Mostrar el resultado
if resultado is not None:
    print("\nEl resultado es:", resultado)
