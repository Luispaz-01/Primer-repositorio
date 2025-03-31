# Crear un diccionario llamado informacion_personal
informacion_personal = {
    "nombre": "Juan Pérez",  # Nombre de la persona
    "edad": 30,              # Edad de la persona
    "ciudad": "Madrid",      # Ciudad de residencia
    "profesion": "Ingeniero" # Profesión de la persona
}

# Función para mostrar el menú de opciones
def mostrar_menu():
    print("\n--- Menú de Opciones ---")
    print("1. Ver información personal")  # Opción para ver la información
    print("2. Modificar ciudad")          # Opción para modificar la ciudad
    print("3. Agregar número de teléfono") # Opción para agregar un teléfono
    print("4. Eliminar edad")             # Opción para eliminar la edad
    print("5. Salir")                      # Opción para salir del programa

# Función para ver la información personal
def ver_informacion():
    print("\nInformación Personal:")
    for clave, valor in informacion_personal.items():  # Iterar sobre el diccionario
        print(f"{clave}: {valor}")  # Imprimir cada clave y su valor

# Función para modificar la ciudad
def modificar_ciudad():
    nueva_ciudad = input("Ingrese la nueva ciudad: ")  # Solicitar nueva ciudad al usuario
    informacion_personal["ciudad"] = nueva_ciudad  # Actualizar el valor de la clave "ciudad"
    print(f"Ciudad actualizada a: {nueva_ciudad}")  # Confirmar la actualización

# Función para agregar un número de teléfono
def agregar_telefono():
    telefono = input("Ingrese el número de teléfono: ")  # Solicitar número de teléfono al usuario
    if "telefono" not in informacion_personal:  # Verificar si la clave "telefono" no existe
        informacion_personal["telefono"] = telefono  # Agregar el número de teléfono al diccionario
        print(f"Número de teléfono agregado: {telefono}")  # Confirmar la adición
    else:
        print("El número de teléfono ya existe.")  # Mensaje si ya existe

# Función para eliminar la edad
def eliminar_edad():
    if "edad" in informacion_personal:  # Verificar si la clave "edad" existe
        del informacion_personal["edad"]  # Eliminar la clave "edad" del diccionario
        print("La clave 'edad' ha sido eliminada.")  # Confirmar la eliminación
    else:
        print("La clave 'edad' no existe.")  # Mensaje si no existe

# Bucle principal del menú
while True:
    mostrar_menu()  # Mostrar el menú de opciones
    opcion = input("Seleccione una opción (1-5): ")  # Solicitar opción al usuario

    # Ejecutar la acción correspondiente según la opción seleccionada
    if opcion == "1":
        ver_informacion()  # Ver información personal
    elif opcion == "2":
        modificar_ciudad()  # Modificar la ciudad
    elif opcion == "3":
        agregar_telefono()  # Agregar un número de teléfono
    elif opcion == "4":
        eliminar_edad()  # Eliminar la edad
    elif opcion == "5":
        print("Saliendo del programa.")  # Mensaje de salida
        break  # Salir del bucle
    else:
        print("Opción no válida. Por favor, seleccione una opción del 1 al 5.")  # Mensaje de error