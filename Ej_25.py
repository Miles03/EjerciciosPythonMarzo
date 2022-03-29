def imprimir(tabla):
    for i in range(len(tabla)):
        print("[",end="")
        for j in range(len(tabla)):
            print("%3s"%tabla[i][j],end="")
        print(" ]")
def llenarVacio(n):
    tabla=[]
    for i in range(n):
        tabla.append([])
        for j in range(n):
            tabla[i]+=[" "]
    return tabla
def asteriscos(tabla,simbolo):
    cont=len(tabla)
    for i in range(len(tabla)):
        cont-=1
        for j in range(len(tabla)):
            if i==len(tabla)//2:
                tabla[i][j]=simbolo
            elif j==len(tabla)//2:
                  tabla[i][j]=simbolo
            elif i==j:
                  tabla[i][j]=simbolo
            else :
                tabla[i][cont]=simbolo
                

                
    
tabla=llenarVacio(11)
##imprimir(tabla)
asteriscos(tabla,"z")
imprimir(tabla)