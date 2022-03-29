anioInicio=1500
anioFin=2022
r="Los anios bisiestos entre "+str(anioInicio)+" y "+str(anioFin)+ " son: "
for i in range (anioInicio,anioFin):
    if (i%4==0 and i%100!=0) or i%400==0:
        r=r+str(i)+","
print(r)
