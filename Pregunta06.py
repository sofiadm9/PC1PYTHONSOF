# Obtener la edad del cliente del usuario.
edad = int(input("¿Cuál es la edad del cliente? "))

# Calcular el precio de la entrada según la edad del cliente.
if edad < 4:
    precio = 0
elif edad <= 18:
    precio = 5
elif edad > 18:    
    precio=10

# Imprimir el precio de la entrada.
print(f"El precio de la entrada es ${precio}.")
