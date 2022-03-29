frase = "jhon morales"
letra="p"
cont=0

for carac in frase:
    if  carac==letra:
        cont+=1
if cont >0:
    print("La lera "+letra+" se encontró: "+str(cont)+" veces en la frase")
else:
    print("La lera "+letra+" no existe en la frase")

