# Paso 1: Pedimos el total de la compra
# Usamos float porque puede tener decimales
total = float(input("Ingresa el total de la compra: "))

# Paso 2: Inicializamos el descuento en 0
descuento = 0

# Paso 3: Evaluamos las condiciones

# Si el total es menor a 50, no hay descuento
if total < 50:
    descuento = 0

# Si el total está entre 50 y 100, aplicamos 5%
elif total >= 50 and total <= 100:
    descuento = total * 0.05

# Si el total es mayor a 100, aplicamos 10%
elif total > 100:
    descuento = total * 0.10

# Paso 4: Calculamos el total a pagar
total_pagar = total - descuento

# Paso 5: Mostramos los resultados
print("Descuento aplicado:", descuento)
print("Total a pagar:", total_pagar)