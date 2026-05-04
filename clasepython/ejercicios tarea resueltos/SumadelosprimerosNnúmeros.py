# Paso 1: Pedimos al usuario el número N
N = int(input("Ingresa un número entero positivo: "))

# Paso 2: Creamos una variable acumuladora
# Aquí vamos guardando la suma
suma = 0

# Paso 3: Usamos un bucle for para recorrer desde 1 hasta N
# range(1, N+1) significa: empieza en 1 y llega hasta N
for i in range(1, N + 1):
    # En cada vuelta, sumamos el valor de i a la variable suma
    suma = suma + i

# Paso 4: Mostramos el resultado final
print("La suma de los números desde 1 hasta", N, "es:", suma)