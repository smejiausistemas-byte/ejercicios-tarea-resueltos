# Paso 1: Pedimos el salario mensual
# Usamos float porque puede tener decimales
salario = float(input("Ingresa tu salario mensual: "))

# Paso 2: Preguntamos si tiene deudas
# Usamos lower() para convertir la respuesta a minúsculas
deuda = input("¿Tienes deudas? (si/no): ").lower()

# Paso 3: Evaluamos la condición
# Para aprobar: salario > 1000 Y no tener deudas
if salario > 1000 and deuda == "no":
    print("Crédito Aprobado")
else:
    print("Crédito Denegado")