from sys import stdin
from fractions import Fraction
import matplotlib.pyplot as plot
import numpy as np
def prettyprintingsVectores(vector):
    for i in range(len(vector)):
        for j in range(1):
            print(vector[i])
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
def crearMatriz(long):
    matriz = [[0 for j in range(long+1)]for i in range(long+1)]
    return matriz
def crearMatriz2(long):
    matriz = [[[0,0] for j in range(long)]for i in range(long)]
    return matriz
def llenar(r,pr,b,pb,m):
    x = r+1
    cont = b//2
    for i in range(r):
        m[i+1][0] = str(pr)
    if r % 2 == 0:
        n = r+1
        z = 1
        for i in range(x,len(m)):
            for j in range(1,len(m)):
                if i == j:
                    m[i][j] = str(1)
                if cont > 0 and n < len(m):
                    m[n][z] = str(pb)
                    cont = cont - 1
                    n += 1
                if cont == 0:
                    cont = b//2
                    z += 1
    else:
        n = r+1
        z = 1
        contador = r
        for i in range(x,len(m)):
            for j in range(1,len(m)):
                if i == j:
                    m[i][j] = str(1)
                if cont > 0 and n < len(m):
                    m[n][z] = str(pb)
                    cont = cont - 1
                    n += 1 
                if cont == 0:
                    cont = b//2
                    z += 1
                    if contador > 1:
                        n = n - 1
                        contador = contador - 1
    return m
def llenar2(r,pr,b,pb,m):
    x = r+1
    cont = b//2
    for i in range(r):
        m[i+1][0] = str(pr)
    if r % 2 == 0:
        n = r+1
        z = 1
        for i in range(x,len(m)):
            for j in range(1,len(m)):
                if i == j:
                    m[i][j] = str(1)
                if cont > 0 and n < len(m):
                    m[n][z] = str(pb)
                    cont = cont - 1
                    n += 1
                if cont == 0:
                    cont = b//2
                    z += 1
    else:
        n = r+1
        z = 1
        contador = r
        for i in range(x,len(m)):
            for j in range(1,len(m)):
                if i == j:
                    m[i][j] = str(1)
                if cont > 0 and n < len(m):
                    m[n][z] = str(pb)
                    cont = cont - 1
                    n += 1 
                if cont == 0:
                    cont = b//2
                    z += 1
                    if contador > 1:
                        n = n - 1
                        contador = contador - 1
    return m
def ver(matriz,rejillas):
    if rejillas % 2 == 0:
        for i in range(len(matriz)):
            for j in range(len(matriz)):
                print(matriz[i][j], end = " ")
            print()
    else:
        for i in range(len(matriz)):
            for j in range(len(matriz)):
                print(matriz[i][j], end = "  ")
            print()
def rendijas_clásico_probabilístico(rejillas,blancos):
    if blancos%2 != 0:
        blancos = blancos + 1
    probalidadRejillas = Fraction(1/rejillas).limit_denominator()
    probalidadblancos = Fraction(1/blancos).limit_denominator()
    matriz = crearMatriz(rejillas+blancos)
    matriz = llenar(rejillas,probalidadRejillas,blancos,probalidadblancos,matriz)
    ver(matriz,rejillas)
    return(matriz)
def rendijas_clásico_cuantico(rejillas,blancos):
    if blancos%2 != 0:
        blancos = blancos + 1
    probalidadRejillas = Fraction(1/rejillas).limit_denominator()
    probalidadblancos = Fraction(1/blancos).limit_denominator()
    matriz = crearMatriz2(rejillas+blancos+1)
    matriz = llenar2(rejillas,probalidadRejillas,blancos,probalidadblancos,matriz)
    print(matriz)
    ver(matriz,rejillas)
    return(matriz)
def Probabilidad(v):
    unidades = len(v)
    x = np.array([ x for x in range(unidades)])
    y = np.array([round(v[x][0]*100,2) for x in range(unidades)])
    plot.bar( x,y , color ='b', align='center')
    plot.title('Propabilidad del estado')
    plot.show()
#m1 = [[False,False,False,False,False,False],[False,False,False,False,False,False],[False,True,False,False,False,True],[False,False,False,True,False,False],[False,False,True,False,False,False],[True,False,False,False,True,False]]
#v1 = [True,False,False,False,False,False]
#n = 5
#v = [[1/4,0],[1/6,0],[1/3,0],[1/6,0],[1/6,0]]
#experimento_canicas(m1,v1,n)
#rendijas_clásico_probabilístico(3,4)
#rendijas_clásico_cuantico(3,4)
#Probabilidad(v)
