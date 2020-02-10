""" SSW 567 Software Testing, Quality Assurance and Maintainance
HW 01 - Testing Triangle Classification
Author: Mrunal Salvi
Github Link: https://github.com/msalvi96/Software-Testing
Due: January 28, 2020 """

import unittest
from testing_triangle import SimpleTriangle, classify_triangle

class TestNonTriangles(unittest.TestCase):
    """ Test class for Non Triangle Inputs """

    def test_non_triangles1(self):

        with self.assertRaises(ValueError):
            triangle = SimpleTriangle('One', 2, 3)

        with self.assertRaises(ValueError):
            triangle = SimpleTriangle('One', 'Two', 3)

        with self.assertRaises(ValueError):
            triangle = SimpleTriangle('One', 'Two', 'Three')

        with self.assertRaises(ValueError):
            triangle = SimpleTriangle(2.136, 5, 6)

    def test_non_triangles2(self):

        with self.assertRaises(ArithmeticError):
            triangle = SimpleTriangle(1, 10, 12)

        with self.assertRaises(ArithmeticError):
            triangle = SimpleTriangle(3, 16, 12)

        with self.assertRaises(ArithmeticError):
            triangle = SimpleTriangle(25, 10, 12)

        with self.assertRaises(ArithmeticError):
            triangle = SimpleTriangle(0, 0, -1)

        with self.assertRaises(ArithmeticError):
            triangle = SimpleTriangle(-1, 1, -2)

    def test_non_triangles3(self):

        with self.assertRaises(AttributeError):
            triangle = SimpleTriangle(0, 12, 12)

        with self.assertRaises(AttributeError):
            triangle = SimpleTriangle(3, 0, 3)

        with self.assertRaises(AttributeError):
            triangle = SimpleTriangle(4, 4, 0)

        with self.assertRaises(AttributeError):
            triangle = SimpleTriangle(0, 0, 0)

    def test_classify(self):

        test_string1 = "All 3 sides are not integers"
        test_string2 = "Sum of 2 sides not greater than or equal to the third side"
        test_string3 = "Triangle cannot have side with length <= 0"

        self.assertEqual(classify_triangle('One', 2, 3), test_string1)
        self.assertEqual(classify_triangle('One', 'Two', 3), test_string1)
        self.assertEqual(classify_triangle('One', 'Two', 'Three'), test_string1)
        self.assertEqual(classify_triangle(2.136, 5, 6), test_string1)

        self.assertEqual(classify_triangle(1, 10, 12), test_string2)
        self.assertEqual(classify_triangle(3, 16, 12), test_string2)
        self.assertEqual(classify_triangle(25, 10, 12), test_string2)
        self.assertEqual(classify_triangle(0, 0, -1), test_string2)
        self.assertEqual(classify_triangle(-1, 1, -2), test_string2)

        self.assertEqual(classify_triangle(0, 12, 12), test_string3)
        self.assertEqual(classify_triangle(3, 0, 3), test_string3)
        self.assertEqual(classify_triangle(4, 4, 0), test_string3)
        self.assertEqual(classify_triangle(0, 0, 0), test_string3)


if __name__ == "__main__":
    unittest.main(exit=False, verbosity=2)