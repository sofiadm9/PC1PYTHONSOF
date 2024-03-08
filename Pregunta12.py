# Obtener el nombre del archivo del usuario
nombre_de_archivo = input("Ingrese un nombre de archivo: ")

# Determinar el tipo MIME según la extensión del nombre del archivo
if nombre_de_archivo.endswith(('.gif', '.jpg', '.jpeg')):
    mime_type = 'imagen/jpeg'
elif nombre_de_archivo.endswith('.png'):
    mime_type = 'imagen/png'
elif nombre_de_archivo.endswith('.pdf'):
    mime_type = 'aplicación/pdf'
elif nombre_de_archivo.endswith('.txt'):
    mime_type = 'texto/sin formato'
elif nombre_de_archivo.endswith('.zip'):
    mime_type = 'aplicación/zip'
else:
    mime_type = 'aplicación/flujo de octeto'

# Imprime el tipo MIME
print("Tipo MIME:", mime_type)
