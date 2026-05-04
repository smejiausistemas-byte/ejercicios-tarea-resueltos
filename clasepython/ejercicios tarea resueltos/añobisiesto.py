# Paso 1: Pedimos el año al usuario
anio = int(input("Ingresa un año: "))

# Paso 2: Evaluamos si es bisiesto usando el operador módulo (%)
# % sirve para saber el residuo de una división

# Primero: verificamos si es divisible por 4
if (anio % 4 == 0 and anio % 100 != 0) or (anio % 400 == 0):
    # Si cumple la condición, es bisiesto
    print("El año es bisiesto")
else:
    # Si no cumple, no es bisiesto
    print("El año no es bisiesto")