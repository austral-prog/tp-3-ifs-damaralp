def discount():
    """
    Ejercicio 9 (Integrador) - Sistema de Descuentos

    Crear un sistema de descuentos para una tienda. Leer mediante input():
    1. El precio unitario de un producto (decimal)
    2. La cantidad de unidades a comprar (entero)

    Calcular el total aplicando los siguientes descuentos según la cantidad:
    - Si compra 10 o más unidades: 20% de descuento
    - Si compra entre 5 y 9 unidades: 10% de descuento
    - Si compra menos de 5 unidades: sin descuento

    Imprimir:
    1. El subtotal (precio × cantidad)
    2. El porcentaje de descuento aplicado
    3. El monto del descuento
    4. El total final

    Ejemplo:
        Para las entradas "100" y "12", la salida esperada es:
        Subtotal: 1200.0
        Descuento aplicado: 20%
        Monto de descuento: 240.0
        Total final: 960.0
    """
    pass

    precio = float(input())
    cantidad = int(input())
    subtotal = precio * cantidad

    if cantidad >= 10:
        descuento = "20%"
        valordesc = subtotal * 0.2
        final = subtotal - valordesc

    elif cantidad >= 5:
        descuento = "10%"
        valordesc = subtotal * 0.1
        final = subtotal - valordesc

    else:
        descuento = "0%"
        valordesc = 0.0
        final = subtotal - valordesc

    print(f"Subtotal: {subtotal}\nDescuento aplicado: {descuento}\nMonto de descuento: {valordesc}\nTotal final: {final}")
