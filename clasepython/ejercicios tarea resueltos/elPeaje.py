# Paso 1: Pedimos al usuario que ingrese su edad
edad = int(input("Por favor, ingresa tu edad: "))

# Paso 2: Evaluamos la condición con if
if edad >= 18:
    # Si la condición es verdadera, se ejecuta este bloque
    print("Puedes conducir ")
else:
    # Si la condición es falsa, se ejecuta este otro bloque
    print("Aún no tienes edad para conducir ")