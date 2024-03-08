# Obtener el valor de N del usuario
n = int(input("Ingrese un número entero positivo: "))
# Calcular la suma de todos los números enteros del 1 al N
suma_de_números = (n * (n + 1)) // 2
# Imprime la suma
print("La suma de todos los números enteros del 1 al", n, "es", suma_de_números)