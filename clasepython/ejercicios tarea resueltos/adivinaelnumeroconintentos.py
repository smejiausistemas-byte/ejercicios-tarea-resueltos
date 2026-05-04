# Paso 1: Definimos el número secreto
numero_secreto = 13  # Puedes cambiarlo por cualquier número entre 1 y 20

# Paso 2: Definimos la cantidad máxima de intentos
intentos_maximos = 5

# Paso 3: Iniciamos un bucle for para los intentos
for intento in range(1, intentos_maximos + 1):
    
    # Mostramos el número de intento actual
    print("Intento", intento, "de", intentos_maximos)
    
    # Paso 4: Pedimos al usuario un número
    numero_usuario = int(input("Adivina el número (entre 1 y 20): "))
    
    # Paso 5: Comparamos el número ingresado con el secreto
    if numero_usuario == numero_secreto:
        print("¡Correcto! 🎉 Adivinaste el número")
        break  # Terminamos el bucle si acierta
    
    elif numero_usuario < numero_secreto:
        print("El número es mayor 🔼")
    
    else:
        print("El número es menor 🔽")

# Paso 6: Si se acaban los intentos sin acertar
# El else del for se ejecuta solo si NO se usó break
else:
    print("Se acabaron los intentos ❌")
    print("El número secreto era:", numero_secreto)