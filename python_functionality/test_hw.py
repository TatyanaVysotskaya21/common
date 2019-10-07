import unittest
from hw_5 import (
    without_duplicates_list,
    number_letter_a_in_str,
    power_of_three,
    result_single_digit,
    zeros_to_the_end,
    arithmetic_progression,
    number_not_occur_twice,
    missing_list_number,
    count_elements_until_tuple,
    string_reversed_order,
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
    def test_without_duplicates_list(self):
        a =[1,1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
        b =[1,2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
        self.assertListEqual(without_duplicates_list(a, b), [1, 2, 3, 5, 8, 13])

    def test_number_letter_a_in_str(self):
        self.assertEqual(number_letter_a_in_str('I am a good developer. I am also a writer', 'a'), 5)

    def test_power_of_three(self):
        number = 9
        self.assertTrue(power_of_three(number))

    def test_result_single_digit(self):
        number = 48
        self.assertEqual(result_single_digit(number), 3)

    def test_zeros_to_the_end(self):
        new_list = [0,2,3,4,6,7,10]
        self.assertListEqual(zeros_to_the_end(new_list), [2, 3, 4, 6, 7, 10, 0])

    def test_arithmetic_progression(self):
        list_progression = [5, 7, 9, 11]
        self.assertTrue(arithmetic_progression(list_progression))

    def test_number_not_occur_twice(self):
        list_input = [5, 3, 4, 3, 4]
        self.assertEqual(number_not_occur_twice(list_input), 5)

    def test_missing_list_number(self):
        list_input = [1,2,3,4,6,7,8]
        self.assertEqual(missing_list_number(list_input), 5)

    def test_count_elements_until_tuple(self):
        list_input = [1,2,3,(1,2),3]
        self.assertEqual(count_elements_until_tuple(list_input), 3)

    def test_string_reversed_order(self):
        str_input = "Hello World and Coders"
        self.assertEqual(string_reversed_order(str_input), "sredoC dna dlroW olleH")

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