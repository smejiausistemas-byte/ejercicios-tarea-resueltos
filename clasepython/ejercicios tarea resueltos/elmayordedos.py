# Paso 1: Pedimos el primer número
num1 = float(input("Ingresa el primer número: "))

# Paso 2: Pedimos el segundo número
num2 = float(input("Ingresa el segundo número: "))

# Paso 3: Comparamos los dos números usando if
if num1 > num2:
    print("El primer número es mayor que el segundo")

# Si la condición anterior no se cumple,suelta esta otra
elif num2 > num1:
    print("El segundo número es mayor que el primer numero")