def password():
    """
    Ejercicio 10 - Validador de Contraseña

    Leer una contraseña mediante input(). Validar que cumpla con los siguientes requisitos:
    1. Debe tener al menos 8 caracteres de longitud
    2. Debe contener al menos un número (usar el operador in para verificar cada dígito del 0 al 9)

    Si cumple ambos requisitos, imprimir "Contraseña valida".
    Si no cumple, imprimir cuál requisito falta.

    Ejemplo:
        Para la entrada "abc12345", la salida esperada es:
        Contraseña valida

        Para la entrada "abc123", la salida esperada es:
        Contraseña muy corta

        Para la entrada "abcdefgh", la salida esperada es:
        Debe contener un numero

        Para la entrada "abc", la salida esperada es:
        Contraseña muy corta
        Debe contener un numero
    """
    pass

    contrasena = input()
    largo = False
    numero = False

    if len(contrasena) >= 8:
        largo = True

    if "0" in contrasena:
        numero = True
    if "1" in contrasena:
        numero = True
    if "2" in contrasena:
        numero = True
    if "3" in contrasena:
        numero = True
    if "4" in contrasena:
        numero = True
    if "5" in contrasena:
        numero = True
    if "6" in contrasena:
        numero = True
    if "7" in contrasena:
        numero = True
    if "8" in contrasena:
        numero = True
    if "9" in contrasena:
        numero = True

    if largo == False:
        print("Contraseña muy corta")
    if numero == False:
        print("Debe contener un numero")
    if largo == True and numero == True:
        print("Contraseña valida")
