import unittest
from calcarea import calculate_area, Triangle, Circle


class TestCalculateArea(unittest.TestCase):
    def test_calculate_area_circle(self):
        self.assertEqual(calculate_area(5), 78.540)
        self.assertEqual(calculate_area(6), 113.097)

    def test_calculate_area_triangle(self):
        self.assertEqual(calculate_area(3, 4, 5), 6.0)
        self.assertEqual(calculate_area(1, 1, 1), 0.433)

    def test_correct_right_triangle(self):
        self.assertTrue(Triangle(3, 4, 5).is_right_triangle())

    def test_incorrect_right_triangle(self):
        self.assertFalse(Triangle(3, 4, 6).is_right_triangle())

    def test_invalid_type_figure(self):
        with self.assertRaises(ValueError):
            calculate_area(1, 2, 3, 4)
        with self.assertRaises(ValueError):
            calculate_area(1, 2)

    def test_invalid_triangle(self):
        with self.assertRaises(ValueError):
            Triangle(5, 1, 1)
        with self.assertRaises(ValueError):
            Triangle(1, 2, -3)

    def test_invalid_circle(self):
        with self.assertRaises(ValueError):
            Circle(0)
