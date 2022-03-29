def imprimir(dic):
    for indice in dic:
        print("Key:",indice,"Precio: ",dic[indice])

dic={}
#dic["pan"]=.12
print(dic)
menu=True
total=0
while menu:
    op=int(input("Elija una opcion\n1.-Agregar Producto\n2.-Facturar\n3.-Salir\n"))
    if op==1:
        indice=input("ingrese el indice: ")
        cantidad=int(input("Ingrese el valor: "))
        dic[indice]=cantidad
        print(dic)
    elif op==2:
        factura=True
        while factura:
            imprimir(dic)
            
            print("Elija una opcion\n1.Agregar a factura\n2.-Finalizar")
            opf=int(input())
            if opf==1:
                indice=input("Ingrese el producto: ")
                cantidad=int(input("Ingrese la cantidad: "))
                ##dic[indice]=cantidad
                if dic.get(indice) is None:
                    print("Producto no encontrado")
                else:
                    total+=dic.get(indice)*cantidad
                    print("El total es: ",total)
            elif opf==2:
                factura=False
            else:
                print("Ingrese una opcion valida")

    elif op==3:
        menu=False
    else:
        print("Ingrese una opcion valida")