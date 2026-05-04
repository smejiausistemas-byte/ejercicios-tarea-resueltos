# Paso 1: Importamos la librería time para usar pausas
import time

# Paso 2: Pedimos los datos al usuario
tamano = int(input("Ingrese el tamaño del archivo (MB): "))
tiempo_total = int(input("Ingrese el tiempo de carga (segundos): "))

# Paso 3: Mostramos mensaje inicial
print("\nIniciando subida de", tamano, "MB...")

# Paso 4: Definimos cuántos pasos tendrá la barra
# Usaremos 20 pasos (cada uno representa 5%)
pasos = 20

# Paso 5: Calculamos cuánto tiempo debe durar cada paso
tiempo_paso = tiempo_total / pasos

# Paso 6: Creamos el bucle para simular la carga
for i in range(1, pasos + 1):
    
    # Calculamos el porcentaje
    porcentaje = int((i / pasos) * 100)
    
    # Creamos la barra
    llenos = "#" * i              # parte llena
    vacios = "-" * (pasos - i)    # parte vacía
    
    # Mostramos la barra
    print("[" + llenos + vacios + "]", porcentaje, "%")
    
    # Esperamos el tiempo correspondiente
    time.sleep(tiempo_paso)

# Paso 7: Mensaje final
print("\n¡Archivo de", tamano, "MB subido con éxito! 🎉")