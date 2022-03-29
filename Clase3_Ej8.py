lista1=["a","b","c","d","e"]
lista2=["c","e","f","t","g"]
listaTodo=[]
lSolo1=[]
lSolo2=[]
lAmbas=[]

listaTodo=lista1+lista2
for palabra in lista1:
    if palabra in lista2:
        lAmbas=lAmbas+[palabra]
    else:
        lSolo1=lSolo1+[palabra]
for palabra in lista2:
    if palabra not  in lista1:
        lSolo2=lSolo2+[palabra]
print(lista1)
print(lista2)
print(listaTodo)
print(lSolo1)
print(lSolo2)
print(lAmbas)

    


