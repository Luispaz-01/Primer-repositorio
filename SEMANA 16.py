# Escritura de Archivo de Texto
# Creamos un nuevo archivo llamado my_notes.txt y escribimos en él

# Abrimos el archivo en modo escritura ('w'), esto creará el archivo si no existe
with open('my_notes.txt', 'w') as file:
    # Escribimos tres líneas de notas personales en el archivo
    file.write("Nota 1: Recoger la ropa de la tintorería.\n")
    file.write("Nota 2: Comprar ingredientes para la cena.\n")
    file.write("Nota 3: Llamar a mamá.\n")

# Lectura de Archivo de Texto
# Ahora abrimos el archivo my_notes.txt en modo lectura ('r')
with open('my_notes.txt', 'r') as file:
    # Leemos el contenido del archivo línea por línea
    for line in file:
        # Mostramos cada línea leída en la consola
        print(line.strip())  # strip() se usa para eliminar el salto de línea al final

# Cierre de Archivos
# Los archivos se cierran automáticamente al salir del bloque 'with'
# No es necesario cerrar el archivo manualmente