# Paso 1: Pedimos al usuario una frase
frase = input("Ingresa una frase: ")

# Paso 2: Convertimos la frase a minúsculas
# Esto ayuda a contar también vocales mayúsculas (A, E, I, O, U)
frase = frase.lower()

# Paso 3: Creamos una variable contador
contador = 0

# Paso 4: Usamos un bucle for para recorrer cada letra de la frase
for letra in frase:
    
    # Paso 5: Verificamos si la letra es una vocal
    if letra == "a" or letra == "e" or letra == "i" or letra == "o" or letra == "u":
        contador = contador + 1  # Sumamos 1 al contador

# Paso 6: Mostramos el resultado final
print("La cantidad de vocales es:", contador)