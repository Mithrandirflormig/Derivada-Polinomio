"""
@autor: Mario Alberto Florentino Miguel
@github: https://github.com/Mithrandirflormig
@correo: yondaimeflormig@ciencias.unam.mx
"""
import unittest
import init

class TestPolynomial(unittest.TestCase):
     
    def test_Derivative(self):
        self.assertEqual(init.init("2x^2+4"), "+4x")
        self.assertEqual(init.init("-32x^4+x^3-100+4x^2+5x"), "-128x^3+3x^2+8x+5")
        self.assertEqual(init.init("+7x^100 - 4x^2 +5x ^3 - 1 + 2"), "+700x^99-8x+15x^2")
        self.assertEqual(init.init("- x ^2 + 2x^4 -10x + 2"), "-2x+8x^3-10")
        self.assertEqual(init.init("x^3"), "+3x^2")
        self.assertEqual(init.init("-2x^2"), "-4x")
        self.assertEqual(init.init("-2^4 + 3x^2 - x +1"), "+6x-1")
        self.assertEqual(init.init("9-6x^3"), "-18x^2")
        self.assertEqual(init.init("x^5 + 7x^4 -x + sqrt(2)"), "+5x^4+28x^3-1")
        self.assertEqual(init.init("- 4 x ^ 5 + 1 x ^ 2 - 100"), "-20x^4+2x")
        self.assertEqual(init.init("sin(0)x^2-x + 1"), "-1")
        self.assertEqual(init.init("3x^3+2x^1"), "+9x^2+2")
        self.assertEqual(init.init("-5 x ^ 2 -3x^1 + 30x + 1"), "-10x-3+30")
        self.assertEqual(init.init("+2.5x^2 - 1.2x^3 +10.5"), "+5.0x-3.6x^2")
        self.assertEqual(init.init("3.1x^2 - 1.2x^1 +3x^0 + 2"), "+6.2x-1.2")
        self.assertEqual(init.init("4+1+100"), '0')

if __name__ == "__main__":
    unittest.main()