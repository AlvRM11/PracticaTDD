import unittest
from contador import Contador

class Test_Contador(unittest.TestCase):

    def test1(self):
        contador1 = Contador(0, 2, 5)

        self.assertEqual(contador1.get_vInicial(), 0)
        self.assertEqual(contador1.get_incremento(), 2)
        self.assertEqual(contador1.get_limite(), 5)

    def test2(self):
        contador2 = Contador(limite=3)

        self.assertEqual(contador2.get_vInicial(), 0)
        self.assertEqual(contador2.get_incremento(), 1)

    def test3(self):
        contador3 = Contador(0, 4, 16)

        self.assertEqual(contador3.incrementador(), 0)

    def test4(self):
        contador4 = Contador(0, 4, 16)

        self.assertEqual(contador4.reset(), contador4.get_vInicial())

if __name__ == '__main__':
    unittest.main()