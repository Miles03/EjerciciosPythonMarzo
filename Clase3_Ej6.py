lista=[1,"hola",3.5,False]
while len(lista)>0:
    print(lista)
    elem=int(input("Ingrese la posicion del elemento a eliminar: "))
    del(lista[elem])