# Paso 1: Definimos el PIN secreto
pin_secreto = "1234"

# Paso 2: Pedimos al usuario que ingrese el PIN por primera vez
pin_usuario = input("Ingresa el PIN: ")

# Paso 3: Iniciamos el bucle while
# El ciclo se repite mientras el PIN ingresado sea diferente al secreto
while pin_usuario != pin_secreto:
    print("PIN incorrecto Intenta de nuevo")

    # Volvemos a pedir el PIN
    pin_usuario = input("Ingresa el PIN: ")

# Paso 4: Cuando el PIN es correcto, el ciclo termina
print("PIN correcto Acceso permitido")