from random import randint
zonaUsuario=int(input("ingrese la zona a disparar"))
zonaportero=randint(1,6)
print("La zona del portero fue",zonaportero)
if zonaUsuario==zonaportero:
    print("No ha sido un gol")
else:
    print("Ha sido un gol")

