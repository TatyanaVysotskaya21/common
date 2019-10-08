import unittest
from hw_5 import (
    number_hours_and_minutes,
    largest_word_in_string,
    string_in_backwards_order,
    output_fib_numbers_to_generate,
    new_list_even_elements,
    sum_input_number,
    return_factorial_number,
    comparison_of_two_numbers,
    alphabetical_shift_letters_in_line,
    letters_row_in_alphabetical_order)


class TaskTestCases(unittest.TestCase):

    def test_number_hours_and_minutes(self):
        number_input = 63
        self.assertEqual(number_hours_and_minutes(number_input), "1:3")

    def test_largest_word_in_string(self):
        str_input = "I love dogs"
        self.assertEqual(largest_word_in_string(str_input), 'love')

    def test_string_in_backwards_order(self):
        self.assertEqual(string_in_backwards_order(lambda: "My name is Michele"), 'Michele is name My')

    def test_output_fib_numbers_to_generate(self):
        self.assertEqual(output_fib_numbers_to_generate(lambda: 11), 144)

    def test_new_list_even_elements(self):
        input_list = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
        self.assertEqual(new_list_even_elements(input_list), [4, 16, 36, 64, 100])

    def test_sum_input_number(self):
        self.assertEqual(sum_input_number(lambda: 4), 10)

    def test_return_factorial_number(self):
        input_number = 4
        self.assertEqual(return_factorial_number(input_number), 24)

    def test_comparison_of_two_numbers(self):
        number_1 = 10
        number_2 = 15
        self.assertTrue(comparison_of_two_numbers(number_1, number_2))
        self.assertFalse(comparison_of_two_numbers(number_2, number_1))
        self.assertEqual(comparison_of_two_numbers(number_1, number_1), -1)

    def test_alphabetical_shift_letters_in_line(self):
        input_text = 'abcd'
        self.assertEqual(alphabetical_shift_letters_in_line(input_text), 'bcdE')

    def test_letters_row_in_alphabetical_order(self):
        input_text = 'hello'
        self.assertEqual(letters_row_in_alphabetical_order(input_text), 'ehllo')


if __name__ == "__main__":
    unittest.main()




