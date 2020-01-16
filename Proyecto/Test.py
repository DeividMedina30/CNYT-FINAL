import unittest
from LibreriaComplejos import *
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
        self.assertEqual(cart_a_Polares(m),(2.5,1.1071487177940904))
    def test_fase(self):
        m = (1,2)
        self.assertEqual(fase(m),(1.1071487177940904))
if __name__ == '__main__':
    unittest.main()
