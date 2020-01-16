import math
def sumComplejos(a,b):
    return (a[0]+b[0], a[1]+b[1])
def Restacomplejos(a,b):
    return (a[0]-b[0], a[1]-b[1])
def Multicomplejos(a,b):
    return((a[0]*b[0] - a[1]*b[1]) , (a[1]*b[0] + a[0]*b[1]))
def Cocientecomplejos(a,b):
    return ((a[0]*b[0] + a[1]*b[1])/(b[0]**2 + b[1]**2) , (b[0]*a[1]-a[0]*b[1])/(b[0]**2 + b[1]**2))
def conjugado(a):
    return(a[0] ,(a[1] * -1 ))
def modulo(a):
    return ( a[0]**2 + a[1]**2 )** 1/2 
def cart_a_Polares(a):
    return((a[0]**2 + a[1]**2 )** 1/2 , math.atan(a[1]/a[0]))
def fase(a):
    return (math.atan(a[1]/a[0]))
def prettyprintings(c):
    print(c[0] , "+" , c[1], "i")
def prettyprintingsPolares(c):
    print("(",c[0], "," ,c[1],")")
def prettyprintingsmodulo(c):
    print("El modulo es:",c)
def prettyprintingsFase(c):
    print("La fase es:",c)
a = (1,2)
b = (2,3)
prettyprintings(sumComplejos(a,b))
prettyprintings(Restacomplejos(a,b))
prettyprintings(Multicomplejos(a,b))
prettyprintings(Cocientecomplejos(a,b))
prettyprintings(conjugado(a))
prettyprintingsmodulo(modulo(a))
prettyprintingsPolares(cart_a_Polares(a))
prettyprintingsFase(fase(a))
