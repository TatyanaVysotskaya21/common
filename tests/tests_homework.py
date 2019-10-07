import unittest
import math
from homework import Rectangle


class RectangleTestCases(unittest.TestCase):
    def setUp(self):

        self.rez_list = [
            {
                'args':(2, 8),
                'perimetr':20,
                'square':16,
                'diagonal': math.sqrt(68)
            },
            {
                'args':(6, 12),
                'perimetr':36,
                'square':72,
                'diagonal': math.sqrt(180)
            },
            {
                'args':(5, 5),
                'perimetr':20,
                'square':25,
                'diagonal': math.sqrt(50)
            }]

    def test_get_rectangle_perimeter(self):
        for i in self.rez_list:
            self.example = Rectangle(i['args'][0], i['args'][1])
            result = self.example.get_rectangle_perimeter()
            self.assertEqual(result, i['perimetr'])

    def test_get_rectangle_square(self):
        for i in self.rez_list:
            self.example = Rectangle(i['args'][0], i['args'][1])
            result = self.example.get_rectangle_square()
            self.assertEqual(result, i['square'])

    def test_get_sum_of_corners(self):
        for corner in range(1, 5):
            for i in self.rez_list:
                self.example = Rectangle(i['args'][0], i['args'][1])
                self.assertEqual(self.example.get_sum_of_corners(corner), corner * 90)

    def test_get_sum_of_corners_invalid_values(self):
        for corner in range(5, 20):
            with self.assertRaises(ValueError):
                for i in self.rez_list:
                    self.example = Rectangle(i['args'][0], i['args'][1])
                    self.example.get_sum_of_corners(corner)

    def test_get_rectangle_diagonal(self):
        for i in self.rez_list:
            self.example = Rectangle(i['args'][0], i['args'][1])
            result = self.example.get_rectangle_diagonal()
            self.assertEqual(result, i['diagonal'])

    def test_get_radius_of_circumscribed_circle(self):
        for i in self.rez_list:
            self.example = Rectangle(i['args'][0], i['args'][1])
            result = self.example.get_radius_of_circumscribed_circle()
            self.assertEqual(result, i['diagonal'] / 2)

    def test_get_radius_of_inscribed_circle(self):

        for i in self.rez_list:
            if i['args'][0] == i['args'][1]:
                self.example = Rectangle(i['args'][0], i['args'][1])
                result = self.example.get_radius_of_inscribed_circle()
                self.assertEqual(result, i['diagonal'] / (math.sqrt(2) * 2))

    def test_get_radius_of_inscribed_circle_invalid_values(self):
        with self.assertRaises(ValueError):
            for i in self.rez_list:
                if i['args'][0] != i['args'][1]:
                    self.example = Rectangle(i['args'][0], i['args'][1])
                    self.example.get_radius_of_inscribed_circle()


if __name__ == "__main__":
    unittest.main()

