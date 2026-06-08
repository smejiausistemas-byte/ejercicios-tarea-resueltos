# Variables
boletos = 0
total = 0

# Función de bienvenida
def bienvenida():

    print("=" * 35)
    print("      CINE PYTHON")
    print("=" * 35)

    print("1. Minecraft La Película ($10000)")
    print("2. Sonic 3 ($12000)")
    print("3. Avengers Endgame ($15000)")


# Función para comprar boletos
def comprar_boletos():

    global boletos
    global total

    pelicula = input("Seleccione una película (1-3): ")

    cantidad = int(input("¿Cuántos boletos desea?: "))

    if pelicula == "1":
        precio = 10000

    elif pelicula == "2":
        precio = 12000

    elif pelicula == "3":
        precio = 15000

    else:
        print("Película no válida")
        return

    boletos += cantidad
    total += precio * cantidad

    print("Compra realizada con éxito.")


# Mostrar cantidad de boletos
def mostrar_boletos():

    print("Boletos comprados:", boletos)


# Mostrar total
def mostrar_total():

    print("Total a pagar: $", total)


# Menú principal
while True:

    bienvenida()

    print("4. Ver boletos comprados")
    print("5. Ver total a pagar")
    print("6. Salir")

    opcion = input("Seleccione una opción: ")

    if opcion == "1" or opcion == "2" or opcion == "3":
        comprar_boletos()

    elif opcion == "4":
        mostrar_boletos()

    elif opcion == "5":
        mostrar_total()

    elif opcion == "6":
        print("Gracias por visitar Cine Python.")
        break

    else:
        print("Opción inválida.")