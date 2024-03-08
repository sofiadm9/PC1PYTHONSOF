# Obtener el número de espectáculos musicales vistos por el usuario.
num_shows = int(input("¿Cuántos espectáculos musicales has visto el año pasado? "))

# Comprobar si el usuario ha visto más de 3 programas.
has_visto_muchos_shows = num_shows > 3

# Imprime el valor booleano
print("¿El usuario ha visto más de 3 programas?", has_visto_muchos_shows)