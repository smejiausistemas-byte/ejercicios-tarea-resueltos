# Paso 1: Pedimos al usuario cuántos términos quiere
n = int(input("¿Cuántos términos de Fibonacci deseas ver?: "))

# Paso 2: Inicializamos los dos primeros valores de la serie
a = 0
b = 1

# Paso 3: Usamos un bucle for para generar la serie
for i in range(n):
    
    # Mostramos el valor actual
    print(a)
    
    # Paso 4: Calculamos el siguiente número
    # Guardamos el valor actual de 'a' en una variable temporal
    temp = a
    
    # Ahora 'a' toma el valor de 'b'
    a = b
    
    # 'b' se convierte en la suma del valor anterior de 'a' y 'b'
    b = temp + b