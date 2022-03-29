def llenarSecuencial(n):
    tabla=[]
    cont=1
    for i in range(n):
        tabla.append([])
        for j in range (n):
            tabla[i]+=[cont]
            cont+=1
    return tabla
def imprimir(tabla):
    for i in range(len(tabla)):
        print("[",end="")
        for j in range(len(tabla)):
            print("%3s"%tabla[i][j],end="")
        print(" ]")
    


tabla=llenarSecuencial(5)
imprimir(tabla)