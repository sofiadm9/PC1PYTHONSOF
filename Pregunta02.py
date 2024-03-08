# Obtener el costo de la comida y el porcentaje de propina del usuario.
costo_comida = float(input("¿Cuánto costó tu comida? "))
porcentaje_propina = float(input("¿Qué porcentaje de propina le gustaría dejar? "))
# Calcular el monto de la propina
cantidad_propina = costo_comida * (porcentaje_propina / 100)
# Imprime el monto de la propina
print("El monto de la propina es $", round(cantidad_propina, 2))
