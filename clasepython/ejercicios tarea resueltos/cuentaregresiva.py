# Paso 1: Pedimos un número entero positivo al usuario
numero = int(input("Ingresa un número entero positivo: "))

# Paso 2: Verificamos que el número sea positivo
if numero < 0:
    print("El número no es válido")
else:
    # Paso 3: Iniciamos el bucle while
    # El ciclo se ejecutará mientras numero sea mayor o igual a 0
    while numero >= 0:
        print(numero)  # Mostramos el número actual

        # Paso 4: Disminuimos el número en 1 (decremento)
        numero = numero - 1

    # Paso 5: Cuando el ciclo termina, mostramos el mensaje final
    print("¡Despegue!")