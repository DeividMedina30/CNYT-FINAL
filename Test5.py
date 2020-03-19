import unittest
from LibreriaComplejos4 import *
class TestStringMethods(unittest.TestCase):
    def test_probabilidad_de_encontrarlo_en_una_posición(self):
        v = [(-3,-1),(0,-2),(0,1),(2,0)]
        p = 2
        self.assertEqual(posibilidad_posicion(v,p),(0.052632))
    def test_Amplitud_de_Transicion(self):
        v1 = [(1,0),(0,-1)]
        v2 = [(0,1),(1,0)]
        self.assertEqual(amplitud_de_transicion(v1,v2),([[[0.0, -1.0]]]))
    def test_varianza(self):
        v1 = [(0,1),(1,0)]
        m1 = [[(1,0),(1,-1)],[(1,1),(1,0)]]
        self.assertEqual(varianza(m1,v1),([[[2, 0]]]))
if __name__ == '__main__':
    unittest.main()
