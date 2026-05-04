# Paso 1: Pedimos los datos al usuario
# Usamos float porque pueden tener decimales
peso = float(input("Ingresa tu peso en kg: "))
altura = float(input("Ingresa tu altura en metros: "))

# Paso 2: Calculamos el IMC usando la fórmula
imc = peso / (altura ** 2)

# Paso 3: Mostramos el valor del IMC
print("Tu IMC es:", imc)

# Paso 4: Clasificamos según el resultado

if imc < 18.5:
    print("Estás en Bajo peso")

elif imc >= 18.5 and imc <= 24.9:
    print("Estás en rango Normal")

elif imc >= 25 and imc <= 29.9:
    print("Tienes Sobrepeso")

else:
    print("Tienes Obesidad")