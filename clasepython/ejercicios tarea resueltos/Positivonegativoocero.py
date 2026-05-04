# Paso 1: Pedimos al usuario que ingrese un número
# Usamos float para permitir números con decimales
numero = float(input("Ingresa un número: "))

# Paso 2: Evaluamos si el número es mayor que 0
if numero > 0:
    # Si es mayor que 0, es positivo
    print("El número es positivo")

# Paso 3: Si no es positivo, evaluamos si es menor que 0
elif numero < 0:
    # Si es menor que 0, es negativo
    print("El número es negativo")

# Paso 4: Si no es ni mayor ni menor que 0, entonces es exactamente 0
else:
    print("El número es cero")