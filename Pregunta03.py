# Obtén el número de payasos y muñecos vendidos.
num_payasos = int(input("¿Cuántos payasos se vendieron? "))
num_muñecas = int(input("¿Cuántas muñecas se vendieron? "))
# Calcular el peso de cada tipo de juguete.
peso_payaso = num_payasos * 112
peso_muñeca = num_muñecas * 75
# Calcular el peso total del paquete.
peso_total = peso_payaso + peso_muñeca
# Imprime el peso total
print("El peso total del paquete es", peso_total, "gramos.")