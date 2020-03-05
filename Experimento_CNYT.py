from sys import stdin
import matplotlib.pyplot as plot
import numpy as np
def prettyprintingsVectores(vector):
    for i in range(len(vector)):
        for j in range(1):
            print(vector[i])
def prettyprintingsVectores2(vector):
    for i in range(len(vector)):
        for j in range(1):
            print(vector[i][j])
def matriz_sobre_Vector(m1,v1):
    cont = 1
    suma = 0
    matriz_Vector = [0 for i in range(len(m1))]
    for i in range(len(m1)):
        for j in range(len(m1)):
            for k in range(len(m1[0])):
                suma = suma + m1[i][k] * v1[k]
            if suma == 0:
                matriz_Vector[i] = False
            else:
                matriz_Vector[i] = True
            suma = 0
            break                
    return matriz_Vector
def matriz_sobre_Vector2(m1,v1):
    cont = 1
    matriz_Vector = [[[0,0] for j in range(1)] for i in range(len(m1))]
    for i in range(len(m1)):
        for j in range(len(v1[0])):
            for k in range(len(m1[0])):
                matriz_Vector[i][j][0] = matriz_Vector[i][j][0] + (m1[i][k][0] * v1[k][j] - m1[i][k][1]*v1[k][j+cont])
                matriz_Vector[i][j][1] = matriz_Vector[i][j][1] + (m1[i][k][1] * v1[k][j] + m1[i][k][0]*v1[k][j+cont])
            break
    return(matriz_Vector)
def experimento_canicas(m1,v1,n):
    if len(m1) == 0 or len(v1) == 0:
        print("No se puede ralizar la operación.")
    elif len(m1[0]) != len(v1):
        print("No se puede ralizar la operación.")
    else:
        cont = 1
        while cont <= n:
            matriz_sobreVector = matriz_sobre_Vector(m1,v1)
            cont += 1
        prettyprintingsVectores(matriz_sobreVector)
        return(matriz_sobreVector)
def cuantico_rendija(m,e,n):
    if len(m) == 0 or len(e) == 0:
        print("No se puede ralizar la operación.")
    elif len(m[0]) != len(e):
        print("No se puede ralizar la operación.")
    else:
        cont = 1
        while cont <= n:
            rendija = matriz_sobre_Vector2(m,e)
            cont += 1
        prettyprintingsVectores2(rendija)
    return(rendija)
def clasico_rendija(m,e,n):
    if len(m) == 0 or len(e) == 0:
        print("No se puede ralizar la operación.")
    elif len(m[0]) != len(e):
        print("No se puede ralizar la operación.")
    else:
        cont = 1
        while cont <= n:
            rendija = matriz_sobre_Vector2(m,e)
            cont += 1
        prettyprintingsVectores2(rendija)
    print(rendija)
    return(rendija)
def Probabilidad(v):
    unidades = len(v)
    x = np.array([ x for x in range(unidades)])
    y = np.array([round(v[x][0]*100,2) for x in range(unidades)])
    plot.bar( x,y , color ='b', align='center')
    plot.title('Propabilidad del estado')
    plot.show()
"""m1 = [[False,False,False,False,False,False],[False,False,False,False,False,False],[False,True,False,False,False,True],[False,False,False,True,False,False],[False,False,True,False,False,False],[True,False,False,False,True,False]]
v1 = [True,False,False,False,False,False]
n = 5
m2 = [[(0,0),(0,0),(0,0),(0,0),(0,0),(0,0),(0,0),(0,0)]
    ,[(1/(2**(1/2)),0),(0,0),(0,0),(0,0),(0,0),(0,0),(0,0),(0,0)]
    ,[(1/(2**(1/2)),0),(0,0),(0,0),(0,0),(0,0),(0,0),(0,0),(0,0)]
    ,[(0,0),(-1/(6**(1/2)),1/(6**(1/2))),(0,0),(1,0),(0,0),(0,0),(0,0),(0,0)]
    ,[(0,0),(-1/(6**(1/2)),-1/(6**(1/2))),(0,0),(0,0),(1,0),(0,0),(0,0),(0,0)]
    ,[(0,0),(1/(6**(1/2)),-1/(6**(1/2))),(-1/(6**(1/2)),1/(6**(1/2))),(0,0),(0,0),(1,0),(0,0),(0,0)]
    ,[(0,0),(0,0),(-1/(6**(1/2)),-1/(6**(1/2))),(0,0),(0,0),(0,0),(1,0),(0,0)]
     ,[(0,0),(0,0),(1/(6**(1/2)),-1/(6**(1/2))),(0,0),(0,0),(0,0),(0,0),(1,0)]]"""
"""e2 = [(1,0),(0,0),(0,0),(0,0),(0,0),(0,0),(0,0),(0,0)]
m3 = [[(0,0),(0,0),(0,0),(0,0),(0,0),(0,0),(0,0),(0,0)]
    ,[(1/(2),0),(0,0),(0,0),(0,0),(0,0),(0,0),(0,0),(0,0)]
    ,[(1/(2),0),(0,0),(0,0),(0,0),(0,0),(0,0),(0,0),(0,0)]
    ,[(0,0),(1/3,0),(0,0),(1,0),(0,0),(0,0),(0,0),(0,0)]
    ,[(0,0),(1/3,0),(0,0),(0,0),(1,0),(0,0),(0,0),(0,0)]
    ,[(0,0),(1/3,0),(1/3,0),(0,0),(0,0),(1,0),(0,0),(0,0)]
    ,[(0,0),(0,0),(1/3,0),(0,0),(0,0),(0,0),(1,0),(0,0)]
     ,[(0,0),(0,0),(1/3,0),(0,0),(0,0),(0,0),(0,0),(1,0)]]
n = 1
clasico_rendija(m3,e2,n)"""
#cuantico_rendija(m2,e2,n)
#v = [[1/4,0],[1/6,0],[1/3,0],[1/6,0],[1/6,0]]
#experimento_canicas(m1,v1,n)
#Probabilidad(v)
