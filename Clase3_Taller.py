lista=[80,34,80,23,70]
pesoMax=lista[0]

for i in range(len(lista)):
    for j in range(i+1,len(lista)):
        suma=lista[i]+lista[j]
        if suma<=150:
            print("La suma de: ",lista[i],"+",lista[j],"=",suma)
            if suma>pesoMax:
                pesoMax=suma
print("El peso maximo posible es: ",pesoMax)


    
