import unittest
from LibreriaComplejos4 import *
class TestStringMethods(unittest.TestCase):
    
    def test_suma(self):
        m = (1,2)
        d = (2,3)
        self.assertEqual(sumComplejos(m,d),(3,5))
    def test_resta(self):
        m = (1,2)
        d = (2,3)
        self.assertEqual(Restacomplejos(m,d),(-1,-1))
    def test_Producto(self):
        m = (1,2)
        d = (2,3)
        self.assertEqual(Multicomplejos(m,d),(-4,7))
    def test_Cociente(self):
        m = (1,2)
        d = (2,3)
        self.assertEqual(Cocientecomplejos(m,d),(00.6153846153846154,0.07692307692307693))
    def test_conjugado(self):
        m = (1,2)
        self.assertEqual(conjugado(m),(1,-2))
    def test_modulo(self):
        m = (1,2)
        self.assertEqual(modulo(m),(2.5))
    
    def test_polares(self):
        m = (1,2)
        self.assertEqual(cart_a_Polares(m),(2.5,1.11))
    def test_fase(self):
        m = (1,2)
        self.assertEqual(fase(m),(1.11))
    
    def test_vectores_Suma(self):
        v1 = [(1,2),(3,4)]
        v2 = [(5,6),(7,8)] 
        self.assertEqual(leer_vectores_Suma(v1,v2),([[[6, 8]], [[10, 12]]]))
    
    def test_vectores_Inversa(self):
        v1 = [(1,2),(3,4)]
        self.assertEqual(leer_vectores_Inversa(v1),([[[-1, -2]], [[-3, -4]]]))
    
    def test_vectores_por_escalar(self):
        v1 = [(1,1),(-3,0),(4,-3)]
        c = (2,2)
        self.assertEqual(leer_vectores_por_escalar(v1,c),([[[0, 4]], [[-6, -6]], [[14, 2]]]))
    
    def test_matriz_suma(self):
        m1 = [[(1,2),(3,4)],[(5,6),(7,8)]]
        m2 = [[(9,10),(11,12)],[(13,14),(15,16)]]
        self.assertEqual(leer_Matrices_Suma(m1,m2),([[[10, 12], [14, 16]], [[18, 20], [22, 24]]]))
    
    def test_matriz_inversa(self):
        m1 = [[(1,2),(3,4)],[(5,6),(7,8)]]
        self.assertEqual(leer_Matrices_Inversa(m1),([[[-1, -2], [-3, -4]], [[-5, -6], [-7, -8]]]))        
    
    def test_matriz_escalar(self):
        m1 = [[(1,2),(3,4)],[(5,6),(7,8)]]
        c = (2,2)
        self.assertEqual(leer_Matrices_Escalar(m1,c),([[[-2, 6], [-2, 14]], [[-2, 22], [-2, 30]]]))
    
    def test_matriz_transpuesta(self):
        #valor = 1 para matrices, valor = 2 para vectores
        v1 = [(0,-1),(1,0)]
        p = 2
        self.assertEqual(leer_Matrices_Transpuesta(v1,p),([[[0, -1], [1, 0]]]))
    
    def test_matriz_conjugada(self):
        #valor = 1 para matrices, valor = 2 para vectores
        m1 = [[(1,2),(3,4)],[(5,6),(7,8)]]
        valor = 1
        self.assertEqual(leer_Matrices_Conjugada(m1,valor),([[[1, -2], [3, -4]], [[5, -6], [7, -8]]]))
        
    def test_matriz_adjunta(self):
        #valor = 1 para matrices, valor = 2 para vectores
        m1 = [[(1,2),(3,4)],[(5,6),(7,8)]]
        valor = 1
        self.assertEqual(leer_Matrices_Adjunta(m1,valor),([[[1, -2], [5, -6]], [[3, -4], [7, -8]]]))
        
    def test_producto_2_matrices(self):
        m1 = [[(1,2),(3,4)],[(5,6),(7,8)]]
        m2 = [[(9,10),(11,12)],[(13,14),(15,16)]]
        self.assertEqual(leer_Matrices_producto(m1,m2),([[[-28, 122], [-32, 142]], [[-36, 306], [-40, 358]]]))
    
    def test_accion_matriz_vector(self):
        m1 = [[(1,2),(3,4)],[(5,6),(7,8)]]
        v1 = [(5,6),(7,8)]
        self.assertEqual(leer_accion_matriz_vector(m1,v1),([[[-18, 68]], [[-26, 172]]]))
    
    def test_productoInterno_vectores(self):
        v1 = [(1,2),(3,4)]
        v2 = [(5,6),(7,8)]
        self.assertEqual(leer_Producto_Interno(v1,v2),(70,-8))
    
    def test_norma_vector(self):
        v1 = [(1,1),(-3,0),(4,-3)]
        self.assertEqual(leer_vector_norma(v1),(6.0))
    
    def test_Matriz_Unitaria(self):
        m1 = [[(0,0),(1,0)],[(1,0),(0,0)]]
        self.assertEqual(leer_matriz_Unitaria(m1),([[[1, 0], [0, 0]], [[0, 0], [1, 0]]]))
    
    def test_Matriz_Hermitiana(self):
        m1 = [[(0,0),(1,0)],[(1,0),(0,0)]]
        self.assertEqual(leer_matriz_Hermitiana(m1),([[(0, 0), (1, 0)], [(1, 0), (0, 0)]]))
    
    def test_distancia_Vectores(self):
        v1 = [(1,2),(3,4),(5,6)]
        v2 = [(6,5),(4,3),(2,1)]
        self.assertEqual(leer_distancia_vectores(v1,v2),(8.37))
    
    def test_producto__tensor_Vectores(self):
        v1 = [(3,0),(4,0),(7,0)]
        v2 = [(-1,0),(2,0)]
        self.assertEqual(leer_producto_Tensor_Vector(v1,v2),([(-3, 0), (6, 0), (-4, 0), (8, 0), (-7, 0), (14, 0)]))
    
    def test_producto__tensor_Matrices(self):
        m1 = [[(0,0),(1,0)],[(1,0),(0,0)]]
        m2 = [[((1/(2**(1/2))),0),((1/(2**(1/2))),0)],[((1/(2**(1/2))),0),((-1/(2**(1/2))),0)]]
        self.assertEqual(leer_producto_Tensor_Matrices(m1,m2),([[(0.0, 0.0), (0.0, 0.0), (0.7071067811865475, 0.0), (0.7071067811865475, 0.0)], [(0.0, 0.0), (-0.0, 0.0), (0.7071067811865475, 0.0), (-0.7071067811865475, 0.0)], [(0.7071067811865475, 0.0), (0.7071067811865475, 0.0), (0.0, 0.0), (0.0, 0.0)], [(0.7071067811865475, 0.0), (-0.7071067811865475, 0.0), (0.0, 0.0), (-0.0, 0.0)]]))

    def test_probabilidad_de_encontrarlo_en_una_posición(self):
        v = [(-3,-1),(0,-2),(0,1),(2,0)]
        p = 2
        self.assertEqual(posibilidad_posicion(v,p),(0.052632))
    
    def test_Amplitud_de_Transicion(self):
        v1 = [(0,1),(1,0)]
        v2 = [(1,0),(0,-1)]
        self.assertEqual(amplitud_de_transicion(v1,v2),([[[0.0, -1.0]]]))  
if __name__ == '__main__':
    unittest.main()
