hora=23
minuto=59
segundo=46
print("La hora es: ",hora,":",minuto,":",segundo)
if hora<=23  and minuto<=59 and segundo<=59:
    segundo+=1
    if segundo==60:
        minuto+=1
        segundo=0
    if minuto==60:
        minuto=0
        hora+=1
    if hora==24:
        hora=0
    print("La hora un segundo despues es: ",hora,":",minuto,":",segundo)
else:
    print("Ingrese una hora valida")