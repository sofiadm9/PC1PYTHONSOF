# Obtener el tiempo del usuario
time_input = input("Ingrese una hora en formato de 24 horas (HH:MM): ")

# Analizar la entrada de tiempo
horas, minutos = map(int, time_input.split(":"))

# Comprobar si es la hora del desayuno.
if 7 <= horas <= 8:
    print("¡Es hora de desayunar!")

# Comprobar si es la hora del almuerzo.
elif 12 <= horas <= 13:
    print("¡Es la hora del almuerzo!")

# Comprobar si es hora de cenar.
elif 18 <= horas <= 19:
    print("¡Es hora de cenar!")

# Si no es hora de comer, no imprimir nada.
else:
    print("No es hora de comer en este momento.")
