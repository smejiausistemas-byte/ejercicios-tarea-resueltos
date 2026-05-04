# Paso 1: Pedimos al usuario el número
numero = int(input("Ingresa un número: "))

# Paso 2: Usamos un bucle for para recorrer del 1 al 10
# range(1, 11) genera números del 1 al 10
for i in range(1, 11):
    
    # Paso 3: Calculamos la multiplicación
    resultado = numero * i
    
    # Paso 4: Mostramos el resultado en forma de tabla
    print(numero, "x", i, "=", resultado)