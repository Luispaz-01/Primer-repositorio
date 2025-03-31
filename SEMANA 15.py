# Crear un diccionario llamado informacion_personal
informacion_personal = {
    "nombre": "Juan Pérez",
    "edad": 30,
    "ciudad": "Madrid",
    "profesion": "Ingeniero"
}

def mostrar_menu():
    print("\n--- Menú de Opciones ---")
    print("1. Ver información personal")
    print("2. Modificar ciudad")
    print("3. Agregar número de teléfono")
    print("4. Eliminar edad")
    print("5. Salir")

def ver_informacion():
    print("\nInformación Personal:")
    for clave, valor in informacion_personal.items():
        print(f"{clave}: {valor}")

def modificar_ciudad():
    nueva_ciudad = input("Ingrese la nueva ciudad: ")
    informacion_personal["ciudad"] = nueva_ciudad
    print(f"Ciudad actualizada a: {nueva_ciudad}")

def agregar_telefono():
    telefono = input("Ingrese el número de teléfono: ")
    if "telefono" not in informacion_personal:
        informacion_personal["telefono"] = telefono
        print(f"Número de teléfono agregado: {telefono}")
    else:
        print("El número de teléfono ya existe.")

def eliminar_edad():
    if "edad" in informacion_personal:
        del informacion_personal["edad"]
        print("La clave 'edad' ha sido eliminada.")
    else:
        print("La clave 'edad' no existe.")

# Bucle principal del menú
while True:
    mostrar_menu()
    opcion = input("Seleccione una opción (1-5): ")

    if opcion == "1":
        ver_informacion()
    elif opcion == "2":
        modificar_ciudad()
    elif opcion == "3":
        agregar_telefono()
    elif opcion == "4":
        eliminar_edad()
    elif opcion == "5":
        print("Saliendo del programa.")
        break
    else:
        print("Opción no válida. Por favor, seleccione una opción del 1 al 5.")