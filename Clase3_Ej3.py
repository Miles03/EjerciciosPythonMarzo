from random import randint

def ppt(op):
    if op==1:
        r="piedra"
    elif op==2:
        r="papel"
    else:
        r="tijeras"
    return r
    


opUsuario = int(input("Ingrese una opcion:\n1.-Piedra\n2.-Papel\n3.-Tijeras"))
opMaquina=randint(1,3)
ganadas=0
ganadasMaquina=0

while ganadas<3  and ganadasMaquina<3:
    opUsuario=int(input("Ingrese una opcion:\n1.-Piedra\n2.-Papel\n3.-Tijeras"))
    if opUsuario>3 or opUsuario<1:
        print("Ingrese una opcion valida porfavor ")
        continue
    opMaquina=randint(1,3)
    print("El usuario eligio: ",ppt(opUsuario))
    print("La maquina eligio: ",ppt(opMaquina))
    if (opUsuario==1 and opMaquina==3)or(opUsuario==3 and opMaquina==2)or (opUsuario==2 and opMaquina==1):
        print("Gana el usuario")
        ganadas+=1
    elif opUsuario==opMaquina:
        print("Es un empate")
    else:
        print("Gana la maquina")
        ganadasMaquina+=1
    print()   
    print("Ganadas Usuario: ",ganadas,"\n")
    print("Ganadas maquina: ",ganadasMaquina,"\n")

