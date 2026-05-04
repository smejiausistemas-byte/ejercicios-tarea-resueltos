# Paso 1: Creamos una variable acumuladora para el total
total = 0

# Paso 2: Pedimos el primer precio
precio = float(input("Ingresa el precio del producto (0 para terminar): "))

# Paso 3: Iniciamos el bucle while
# Se repetirá mientras el precio sea diferente de 0
while precio != 0:
    
    # Sumamos el precio al total
    total = total + precio
    
    # Volvemos a pedir otro precio
    precio = float(input("Ingresa el precio del producto (0 para terminar): "))

# Paso 4: Aplicamos descuento si corresponde
if total > 100:
    descuento = total * 0.10
    total_pagar = total - descuento
else:
    descuento = 0
    total_pagar = total

# Paso 5: Mostramos los resultados
print("Total de la compra:", total)
print("Descuento aplicado:", descuento)
print("Total a pagar:", total_pagar)