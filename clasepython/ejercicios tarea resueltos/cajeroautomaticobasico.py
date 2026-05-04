# Paso 1: Definimos el saldo inicial
saldo = 1000

# Paso 2: Creamos una variable para controlar el bucle
opcion = 0

# Paso 3: Iniciamos el bucle while
# El programa se repetirá hasta que el usuario elija salir (opción 3)
while opcion != 3:
    
    # Mostramos el menú
    print("\n--- CAJERO AUTOMÁTICO ---")
    print("1. Consultar saldo")
    print("2. Retirar dinero")
    print("3. Salir")
    
    # Pedimos al usuario que elija una opción
    opcion = int(input("Selecciona una opción: "))
    
    # Paso 4: Evaluamos la opción elegida
    
    if opcion == 1:
        # Consultar saldo
        print("Tu saldo actual es:", saldo)
    
    elif opcion == 2:
        # Retirar dinero
        retiro = float(input("Ingresa la cantidad a retirar: "))
        
        # Verificamos si hay suficiente saldo
        if retiro <= saldo:
            saldo = saldo - retiro  # Actualizamos el saldo
            print("Retiro exitoso")
            print("Tu nuevo saldo es:", saldo)
        else:
            print("Fondos insuficientes")
    
    elif opcion == 3:
        # Salir del programa
        print("Gracias por usar el cajero")
    
    else:
        # Opción inválida
        print("Opción no válida")