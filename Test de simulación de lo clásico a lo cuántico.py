import unittest
from Experimento_CNYT import *
class TestStringMethods(unittest.TestCase):
    def test_canicas_con_coeficiente_booleanos(self):
        m1 = [[False,False,False,False,False,False],[False,False,False,False,False,False],[False,True,False,False,False,True],[False,False,False,True,False,False],[False,False,True,False,False,False],[True,False,False,False,True,False]]
        v1 = [True,False,False,False,False,False]
        n = 1
        self.assertEqual(experimento_canicas(m1,v1,n),([False, False, False, False, False, True]))
if __name__ == '__main__':
    unittest.main()
