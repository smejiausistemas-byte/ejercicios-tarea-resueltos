tamano = int(input("Ingrese el tamaño para sus figuras: "))

# Paso 2: Creamos el menú
print("\n--- MENÚ DE FIGURAS ---")
print("1. Triángulo")
print("2. Cuadrado")
print("3. Rectángulo")
print("4. Círculo")
print("5. Pentágono")

opcion = int(input("Elige una opción: "))

if opcion == 1:
    print("\n--- TRIÁNGULO ---")
    
    for fila in range(1, tamano + 1):
        for columna in range(fila):
            print("#", end=" ")
        print()

elif opcion == 2:
    print("\n--- CUADRADO ---")
    
    for fila in range(tamano):
        for columna in range(tamano):
            print("#", end=" ")
        print()

elif opcion == 3:
    print("\n--- RECTÁNGULO ---")
    
    for fila in range(tamano):
        for columna in range(tamano * 2):
            print("#", end=" ")
        print()

elif opcion == 4:
    print("\n--- CÍRCULO ---")
    
    radio = tamano

    for y in range(-radio, radio + 1):
        for x in range(-radio, radio + 1):
            
            # Fórmula del círculo
            if x*x + y*y <= radio*radio:
                print("#", end=" ")
            else:
                print(" ", end=" ")
        print()
elif opcion == 5:
    print("\n--- PENTÁGONO ---")

    for fila in range(tamano):
        for espacio in range(tamano - fila - 1):
            print(" ", end=" ")
        for columna in range(2 * fila + 1):
            print("#", end=" ")
        print()

    for fila in range(tamano):
        for espacio in range(1):
            print(" ", end=" ")
        for columna in range(2 * tamano - 1):
            print("#", end=" ")
        print()

else:
    print("Opción no válida")