import unittest
from geometric_lib.rectangle import *
from geometric_lib.triangle import *
from geometric_lib.square import *
from geometric_lib.circle import *
class RectangleTestCase(unittest.TestCase):
    def test_area(self):
        res = rectangle_area(10, 5)
        self.assertEqual(res, 50)

        res = rectangle_perimeter(4,5)
        self.assertEqual(res,18)

        res = rectangle_area(2,0)
        self.assertEqual(res, 0)

        res = rectangle_area(2,2)
        self.assertEqual(res, 4)

        res = rectangle_area(90,100)
        self.assertEqual(res, 9000)

    def test_perimetr(self):
        res = rectangle_perimeter(4,5)
        self.assertEqual(res, 18)

        res = rectangle_perimeter(3,100)
        self.assertEqual(res, 206)
        
class CircleTests(unittest.TestCase):
    def test_area(self):
        res = circle_area(5)
        self.assertEqual(res, math.pi * 5 * 5)
        
        res = circle_area(0)
        self.assertEqual(res, 0)

    def test_perimetr(self):
        res = circle_perimeter(13)
        self.assertEqual(res, math.pi * 13 * 2)

        res = circle_area(0)
        self.assertEqual(res, 0)

class TriangleTests(unittest.TestCase):
    def test_area(self):
        res = triangle_area(5, 9)
        self.assertEqual(res, 5 * 9 / 2)

        res = triangle_area(4,4)
        self.assertEqual(res, 8) 

    def test_perimetr(self):

        res = triangle_perimeter(4, 2, 5)
        self.assertEqual(res, 11)

        res = triangle_perimeter(10, 13, 15)
        self.assertEqual(res, 38)

    def test_is_triangle(self):
        self.assertFalse(is_triangle(2, 3, 5))

        self.assertTrue(is_triangle(12, 15, 14))

    def test_is_isoscelesTests(self):
        self.assertFalse(is_isosceles(2, 3, 4))

        self.assertTrue(is_triangle(12, 12, 10))

    def test_is_equilateral(self):
        self.assertFalse(is_isosceles(10, 11, 13))

        self.assertTrue(is_triangle(10, 10, 10))

class SquareTests(unittest.TestCase):
    def test_area(self):
        res = square_area(4)
        self.assertEqual(res, 16)

        res = square_area(0)
        self.assertEqual(res, 0)

    def test_perimetr(self):
        res = square_perimetr(13)
        self.assertEqual(res, 52)
        
        res = square_perimetr(5)
        self.assertEqual(res, 20)

    def test_is_square(self):
        self.assertTrue(is_square(5,5,5,5))
        self.assertFalse(is_square(5,5,3,5))