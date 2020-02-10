""" SSW 567 Software Testing, Quality Assurance and Maintainance
HW 01 - Testing Triangle Classification
Author: Mrunal Salvi
Github Link: https://github.com/msalvi96/Software-Testing
Due: January 28, 2020 """

import unittest

class SimpleTriangle:
    """ Triangle class to determine different types of triangles """

    def __init__(self, side1, side2, side3):
        """ Initialize sides of triangle """

        self.side1 = side1
        self.side2 = side2
        self.side3 = side3

        if not(isinstance(self.side1, int) and isinstance(self.side2, int) and isinstance(self.side3, int)):
            raise ValueError

        if ((self.side1 + self.side2) < self.side3) or ((self.side2 + self.side3) < self.side1) or ((self.side1 + self.side3) < self.side2):
            raise ArithmeticError

        if self.side1 <= 0 or self.side2 <= 0 or self.side3 <= 0:
            raise AttributeError

    def right_triangle(self):
        """ Right Angle Triangle """

        side1, side2, side3 = sorted([self.side1, self.side2, self.side3])
        return round((side1 * side1) + (side2 * side2) - (side3 * side3), 2) == 0

    def equilateral(self):
        """ Equilateral Triangle """

        return self.side1 == self.side2 and self.side2 == self.side3

    def isosceles(self):
        """ Isosceles Triangle """

        return (self.side1 == self.side2 and self.side2 != self.side3) or (self.side2 == self.side3 and self.side2 != self.side1) or (self.side1 == self.side3 and self.side3 != self.side2)

    def scalene(self):
        """ Scalene Triangle """

        return self.side1 != self.side2 and self.side2 != self.side3 and self.side1 != self.side3

class TriangleTest(unittest.TestCase):
    """ Test Class for SimpleTriangle and Classify Triangle Function"""

    def test_init(self):
        """ Verify that __init__ method works properly """

        triangle = SimpleTriangle(3, 4, 5)
        self.assertEqual(triangle.side1, 3)
        self.assertEqual(triangle.side2, 4)
        self.assertEqual(triangle.side3, 5)

    def test_right_triangle(self):
        """ Verify that Right Triangle method works properly """

        triangle1 = SimpleTriangle(3, 4, 5)
        self.assertTrue(triangle1.right_triangle())

        triangle2 = SimpleTriangle(3, 3, 4)
        self.assertFalse(triangle2.right_triangle())

        triangle3 = SimpleTriangle(1, 1, 1.414)
        self.assertTrue(triangle3.right_triangle())

    def test_equilateral(self):
        """ Verify that Equilateral method works properly """

        triangle1 = SimpleTriangle(3, 3, 3)
        self.assertTrue(triangle1.equilateral())

        triangle2 = SimpleTriangle(3, 3, 4)
        self.assertFalse(triangle2.equilateral())

        triangle3 = SimpleTriangle(1, 2, 2)
        self.assertFalse(triangle3.equilateral())

    def test_isosceles(self):
        """ Verify that Isosceles method works properly """

        triangle1 = SimpleTriangle(3, 3, 5)
        self.assertTrue(triangle1.isosceles())

        triangle2 = SimpleTriangle(3, 4, 3)
        self.assertTrue(triangle2.isosceles())

        triangle3 = SimpleTriangle(4, 2, 2)
        self.assertTrue(triangle3.isosceles())

        triangle4 = SimpleTriangle(3, 4, 5)
        self.assertFalse(triangle4.isosceles())

    def test_scalene(self):
        """ Verify that Scalene method works properly """

        triangle1 = SimpleTriangle(3, 4, 5)
        self.assertTrue(triangle1.scalene())

        triangle2 = SimpleTriangle(3, 4, 3)
        self.assertFalse(triangle2.scalene())

        triangle3 = SimpleTriangle(4, 2, 2)
        self.assertFalse(triangle3.scalene())

        triangle4 = SimpleTriangle(3, 3, 3)
        self.assertFalse(triangle4.scalene())

    def test_classify(self):
        """ Verify that classify triangle works properly """

        triangle1 = classify_triangle(3, 3, 3)
        self.assertEqual(triangle1, "Equilateral Triangle")
        self.assertNotEqual(triangle1, "Isoceles Triangle")

        triangle2 = classify_triangle(1, 1, 1.414)
        self.assertEqual(triangle2, "Isosceles Right Angled Triangle")
        self.assertNotEqual(triangle2, "Isoceles Triangle")

        triangle3 = classify_triangle(4, 5, 4)
        self.assertEqual(triangle3, "Isosceles Triangle")
        self.assertNotEqual(triangle3, "Isosceles Right Angled Triangle")

        triangle4 = classify_triangle(3, 4, 5)
        self.assertEqual(triangle4, "Right Angled Triangle")
        self.assertNotEqual(triangle4, "Scalene Triangle")

        triangle5 = classify_triangle(4, 6, 7)
        self.assertEqual(triangle5, "Scalene Triangle")
        self.assertNotEqual(triangle5, "Right Angled Triangle")


def classify_triangle(a, b, c):
    """ Function to classify triangle """

    try:
        triangle = SimpleTriangle(a, b, c)

    except ValueError:
        return "All 3 sides are not integers"

    except ArithmeticError:
        return "Sum of 2 sides not greater than or equal to the third side"

    except AttributeError:
        return "Triangle cannot have side with length <= 0"

    if triangle.equilateral():
        return "Equilateral Triangle"

    if triangle.isosceles() and triangle.right_triangle():
        return "Isosceles Right Angled Triangle"

    if triangle.isosceles():
        return "Isosceles Triangle"

    if triangle.right_triangle():
        return "Right Angled Triangle"

    if triangle.scalene():
        return "Scalene Triangle"

if __name__ == "__main__":
    unittest.main(exit=False, verbosity=2)
    triangle_list = [
        classify_triangle(3, 3, 3),
        classify_triangle(3, 3, 5),
        classify_triangle(5, 4, 3),
        classify_triangle(2, 3, 4),
        classify_triangle(1, 1, 1.414)
    ]

    for triangle in triangle_list:
        print(triangle)