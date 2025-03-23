def calcular_descuento(monto_total, porcentaje_descuento=10):
    """
    Calcula el monto del descuento basado en el monto total de la compra
    y un porcentaje de descuento predeterminado.

    :param monto_total: Monto total de la compra
    :param porcentaje_descuento: Porcentaje de descuento (por defecto 10%)
    :return: Monto del descuento calculado
    """
    # Calculamos el descuento multiplicando el monto total por el porcentaje de descuento
    descuento = (monto_total * porcentaje_descuento) / 100
    return descuento  # Devolvemos el monto del descuento calculado

# Programa principal
if __name__ == "__main__":
    # Solicitar al usuario que ingrese el nombre del producto
    producto = input("¿Qué producto compró? ")

    # Solicitar al usuario que ingrese el valor unitario del producto
    valor_unitario = float(input(f"Ingrese el valor unitario de {producto}: $"))

    # Solicitar al usuario que ingrese la cantidad de unidades que va a llevar
    cantidad = int(input(f"¿Cuántas unidades de {producto} va a llevar? "))

    # Calcular el monto total de la compra
    monto_compra = valor_unitario * cantidad

    # Llamar a la función para calcular el total de la compra (sin descuento)
    total_compra = monto_compra  # Esta variable almacena el total de la compra

    # Llamar a la función para calcular el descuento del 10% sobre el total de la compra
    descuento = calcular_descuento(total_compra)  # Segunda llamada a la función
    monto_final = total_compra - descuento  # Calculamos el monto final a pagar

    # Imprimir los resultados
    print(f"\nProducto: {producto}")
    print(f"Monto total de la compra: ${total_compra:.2f}")
    print(f"Monto del descuento (10%): ${descuento:.2f}")
    print(f"Monto final a pagar: ${monto_final:.2f}")
