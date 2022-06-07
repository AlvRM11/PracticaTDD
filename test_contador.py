import unittest
from contador import Contador

class Test_Contador(unittest.TestCase):

    def test1(self):
        contador1 = Contador(0, 2, 5)

        self.assertEqual(contador1.vInicial, 0)
        self.assertEqual(contador1.incremento, 2)
        self.assertEqual(contador1.limite, 5)

if __name__ == '__main__':
    unittest.main()