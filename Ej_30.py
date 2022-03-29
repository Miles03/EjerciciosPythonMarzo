from operator import itemgetter


def imprimir(dic):
    for i in dic:
        print("Key",i,"value:",dic[i])

def agregarEstudiante(dic,codigo,nombre):
    dic[codigo]=[]
    dic[codigo].append(nombre)
    dic[codigo]=[].append([])

def agregarNota(dic,codigo,nota):
    dic[codigo][1]+=[nota]
def prom(lista):
    suma=0
    for iten in lista:
        suma+=iten
    return suma/len(lista)
dic={}
imprimir(dic)
agregarEstudiante(dic,"001","Kevin")
agregarNota(dic,"001",10)
imprimir(dic)
prom(dic(["001"][1]))