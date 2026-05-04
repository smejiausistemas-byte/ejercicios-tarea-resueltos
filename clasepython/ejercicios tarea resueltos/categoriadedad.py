# Paso 1: Pedimos al usuario que ingrese su edad
# Usamos int() porque la edad es un número entero
edad = int(input("Ingresa tu edad: "))

# Paso 2: Evaluamos las condiciones

# Preguntamos si la edad está entre 0 y 12
if edad >= 0 and edad <= 12:
    print("Eres un Niño")

# Si no se cumple lo anterior, verificamos si está entre 13 y 17
elif edad >= 13 and edad <= 17:
    print("Eres un Adolescente")

# Si tampoco se cumple, verificamos si está entre 18 y 64
elif edad >= 18 and edad <= 64:
    print("Eres un Adulto")

# Si no es ninguno de los anteriores, entonces es 65 o más
elif edad >= 65:
    print("Eres un Adulto mayor")

# Este caso es por si ingresan una edad inválida (negativa)
else:
    print("Edad no válida")