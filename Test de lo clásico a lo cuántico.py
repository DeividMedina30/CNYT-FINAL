import unittest
from Experimento_CNYT import *
class TestStringMethods(unittest.TestCase):
    def test_canicas_con_coeficiente_booleanos(self):
        m1 = [[False,False,False,False,False,False],[False,False,False,False,False,False],[False,True,False,False,False,True],[False,False,False,True,False,False],[False,False,True,False,False,False],[True,False,False,False,True,False]]
        v1 = [True,False,False,False,False,False]
        n = 1
        self.assertEqual(experimento_canicas(m1,v1,n),([False, False, False, False, False, True]))
        self.assertEqual(experimento_canicas(m1,v1,3),([False, False, False, False, False, True]))
        self.assertEqual(experimento_canicas(m1,v1,5),([False, False, False, False, False, True]))
    def test_múltiples_rendijas_clásico_cuantico(self):
        m = [[(0,0),(0,0),(0,0),(0,0),(0,0),(0,0),(0,0),(0,0)]
            ,[(1/(2**(1/2)),0),(0,0),(0,0),(0,0),(0,0),(0,0),(0,0),(0,0)]
            ,[(1/(2**(1/2)),0),(0,0),(0,0),(0,0),(0,0),(0,0),(0,0),(0,0)]
            ,[(0,0),(-1/(6**(1/2)),1/(6**(1/2))),(0,0),(1,0),(0,0),(0,0),(0,0),(0,0)]
            ,[(0,0),(-1/(6**(1/2)),-1/(6**(1/2))),(0,0),(0,0),(1,0),(0,0),(0,0),(0,0)]
            ,[(0,0),(1/(6**(1/2)),-1/(6**(1/2))),(-1/(6**(1/2)),1/(6**(1/2))),(0,0),(0,0),(1,0),(0,0),(0,0)]
            ,[(0,0),(0,0),(-1/(6**(1/2)),-1/(6**(1/2))),(0,0),(0,0),(0,0),(1,0),(0,0)]
             ,[(0,0),(0,0),(1/(6**(1/2)),-1/(6**(1/2))),(0,0),(0,0),(0,0),(0,0),(1,0)]]
        e = [(1,0),(0,0),(0,0),(0,0),(0,0),(0,0),(0,0),(0,0)]
        self.assertEqual(cuantico_rendija(m,e,1),([[[0, 0]], [[0.7071067811865475, 0.0]], [[0.7071067811865475, 0.0]], [[0.0, 0.0]], [[0.0, 0.0]], [[0.0, 0.0]], [[0.0, 0.0]], [[0.0, 0.0]]]))
        self.assertEqual(cuantico_rendija(m,e,3),([[[0, 0]], [[0.7071067811865475, 0.0]], [[0.7071067811865475, 0.0]], [[0.0, 0.0]], [[0.0, 0.0]], [[0.0, 0.0]], [[0.0, 0.0]], [[0.0, 0.0]]]))
    def test_múltiples_rendijas_clásico(self):
        m3 = [[(0,0),(0,0),(0,0),(0,0),(0,0),(0,0),(0,0),(0,0)]
            ,[(1/(2),0),(0,0),(0,0),(0,0),(0,0),(0,0),(0,0),(0,0)]
            ,[(1/(2),0),(0,0),(0,0),(0,0),(0,0),(0,0),(0,0),(0,0)]
            ,[(0,0),(1/3,0),(0,0),(1,0),(0,0),(0,0),(0,0),(0,0)]
            ,[(0,0),(1/3,0),(0,0),(0,0),(1,0),(0,0),(0,0),(0,0)]
            ,[(0,0),(1/3,0),(1/3,0),(0,0),(0,0),(1,0),(0,0),(0,0)]
            ,[(0,0),(0,0),(1/3,0),(0,0),(0,0),(0,0),(1,0),(0,0)]
             ,[(0,0),(0,0),(1/3,0),(0,0),(0,0),(0,0),(0,0),(1,0)]]
        e = [(1,0),(0,0),(0,0),(0,0),(0,0),(0,0),(0,0),(0,0)]
        self.assertEqual(clasico_rendija(m3,e,1),([[[0, 0]], [[0.5, 0.0]], [[0.5, 0.0]], [[0.0, 0.0]], [[0.0, 0.0]], [[0.0, 0.0]], [[0.0, 0.0]], [[0.0, 0.0]]]))
        self.assertEqual(clasico_rendija(m3,e,3),([[[0, 0]], [[0.5, 0.0]], [[0.5, 0.0]], [[0.0, 0.0]], [[0.0, 0.0]], [[0.0, 0.0]], [[0.0, 0.0]], [[0.0, 0.0]]]))
    def test_probabilidad_estado(self):
        v = [[1/4,0],[1/6,0],[1/3,0],[1/6,0],[1/6,0]]
        Probabilidad(v)
if __name__ == '__main__':
    unittest.main()
