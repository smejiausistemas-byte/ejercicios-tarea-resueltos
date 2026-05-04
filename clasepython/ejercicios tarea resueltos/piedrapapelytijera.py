import random, time
opciones = ["piedra", "papel", "tijera"]
print("="*55)
print("==== PIEDRA PAPEL O TIJERA ====")
print("="*55)
# usumos el "while True" porque es un bucle infinito
while True:
    # al final colocamos el .lower para que el programa no falle si se escribe en mayusculas o minusculas
    usuario = input("Elige piedra, papel o tijera (o salir): ").lower()

    if usuario == "salir":
        print("Fin del juego")
        break
# este nos sirve para que la computadora pueda escojer las opciones aleatorias 
    pc = random.choice(opciones)

    print("Tú:", usuario)
    print("PC:", pc)

    if usuario == pc:
        print("Empate")
    elif usuario == "piedra" and pc == "tijera":
        print("Ganaste")
    elif usuario == "tijera" and pc == "papel":
        print("Ganaste")
    elif usuario == "papel" and pc == "piedra":
        print("Ganaste")
    else:
        print("Perdiste")
