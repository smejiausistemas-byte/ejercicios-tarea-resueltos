# Paso 1: Pedimos un número al usuario
numero = int(input("Ingresa un número: "))

# Paso 2: Asumimos que el número es primo (bandera)
es_primo = True

# Paso 3: Validamos que el número sea mayor que 1
if numero <= 1:
    es_primo = False
else:
    # Paso 4: Usamos un bucle for para probar divisiones
    # Probamos desde 2 hasta numero - 1
    for i in range(2, numero):
        
        # Paso 5: Verificamos si el número es divisible entre i
        if numero % i == 0:
            # Si es divisible, ya no es primo
            es_primo = False
            break  # Salimos del bucle porque ya no necesitamos seguir

# Paso 6: Mostramos el resultado final
if es_primo:
    print("El número es primo")
else:
    print("El número no es primo")