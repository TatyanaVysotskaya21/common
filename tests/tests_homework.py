import unittest
import math
from homework import Rectangle


class RectangleTestCases(unittest.TestCase):
    def setUp(self):
        self.example_1 = Rectangle(2, 8)
        self.example_2 = Rectangle(6, 12)
        self.example_3 = Rectangle(15, 15)


    def test_get_rectangle_perimeter(self):
        result = self.example_1.get_rectangle_perimeter()
        self.assertEqual(result, (2 + 8) * 2)
        result = self.example_2.get_rectangle_perimeter()
        self.assertEqual(result, (6 + 12) * 2)
        result = self.example_3.get_rectangle_perimeter()
        self.assertEqual(result, (15 + 15) * 2)


    def test_get_rectangle_square(self):
        result = self.example_1.get_rectangle_square()
        self.assertEqual(result, 2 * 8)
        result = self.example_2.get_rectangle_square()
        self.assertEqual(result, 6 * 12)
        result = self.example_3.get_rectangle_square()
        self.assertEqual(result, 15 * 15)


    def test_get_sum_of_corners(self):
        for corner in range(1, 5):
            self.assertEqual(self.example_1.get_sum_of_corners(corner), corner * 90)
            self.assertEqual(self.example_2.get_sum_of_corners(corner), corner * 90)
            self.assertEqual(self.example_3.get_sum_of_corners(corner), corner * 90)


    def test_get_sum_of_corners_invalid_values(self):
        for corner in range(5, 20):
            with self.assertRaises(ValueError):
                self.example_1.get_sum_of_corners(corner)
                self.example_2.get_sum_of_corners(corner)
                self.example_3.get_sum_of_corners(corner)


    def test_get_rectangle_diagonal(self):
        result = self.example_1.get_rectangle_diagonal()
        self.assertEqual(result, math.sqrt(2 ** 2 + 8 ** 2))
        result = self.example_2.get_rectangle_diagonal()
        self.assertEqual(result, math.sqrt(6 ** 2 + 12 ** 2))
        result = self.example_3.get_rectangle_diagonal()
        self.assertEqual(result, math.sqrt(15 ** 2 + 15 ** 2))


    def test_get_radius_of_circumscribed_circle(self):
        result = self.example_1.get_radius_of_circumscribed_circle()
        self.assertEqual(result, math.sqrt(2 ** 2 + 8 ** 2) / 2)
        result = self.example_2.get_radius_of_circumscribed_circle()
        self.assertEqual(result, math.sqrt(6 ** 2 + 12 ** 2) / 2)
        result = self.example_3.get_radius_of_circumscribed_circle()
        self.assertEqual(result, math.sqrt(15 ** 2 + 15 ** 2) / 2)


    def test_get_radius_of_inscribed_circle(self):
        result = self.example_3.get_radius_of_inscribed_circle()
        self.assertEqual(result, math.sqrt(15 ** 2 + 15 ** 2) / (math.sqrt(2) * 2))


    def test_get_radius_of_inscribed_circle_invalid_values(self):
        with self.assertRaises(ValueError):
            self.example_1.get_radius_of_inscribed_circle()
            self.example_2.get_radius_of_inscribed_circle()


if __name__ == "__main__":
    unittest.main()


