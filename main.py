import unittest
import math

class UnitTest(unittest.TestCase):
    "Test ldexp function"
    

    "natural numbers in ldexp test"
    def naturalNumbersTest(self):
        
        expected = 80.0
        result = math.ldexp(5, 4)
        self.assertEqual(expected, result)

    "negative numbers in ldexp test"
    def negativeNumberTest(self):
        
        expected = -0.125
        result = math.ldexp(-2, -4)
        self.assertEqual(expected, result)

    "Using natural and negative numbers in ldexp args"
    def naturalWithNegativeNumber(self):

        expected = 0.75
        result = math.ldexp(3, -2)
        self.assertEqual(expected, result)

    def zeroTest(self):
        "Test with natural number and zero in ldexp args"
        expected = 2.0
        result = math.ldexp(2, 0)
        self.assertEqual(expected, result)

    def stringTest(self):
        "Test strings in ldexp args"
        with self.assertRaises(TypeError) as verr:
            math.ldexp("two", "five")
            self.assertIn("it shall not be a string", verr)

if __name__ == '__main__':
    unittest.main()