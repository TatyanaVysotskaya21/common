import pytest
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
    string_reversed_order)


def test_without_duplicates_list():
    a =[1,1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
    b =[1,2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
    assert without_duplicates_list(a, b)  == [1, 2, 3, 5, 8, 13]

def test_number_letter_a_in_str():
    assert number_letter_a_in_str('I am a good developer. I am also a writer', 'a') == 5

def test_power_of_three():
    assert power_of_three(9) == True

def test_result_single_digit():
    assert result_single_digit(48) == 3

def test_zeros_to_the_end():
    new_list = [0,2,3,4,6,7,10]
    assert zeros_to_the_end(new_list) == [2, 3, 4, 6, 7, 10, 0]

def test_arithmetic_progression():
    list_progression = [5, 7, 9, 11]
    assert arithmetic_progression(list_progression) == True

def test_number_not_occur_twice():
    list_input = [5, 3, 4, 3, 4]
    assert number_not_occur_twice(list_input) == 5

def test_missing_list_number():
    list_input = [1,2,3,4,6,7,8]
    assert missing_list_number(list_input) == 5

def test_count_elements_until_tuple():
    list_input = [1,2,3,(1,2),3]
    assert count_elements_until_tuple(list_input) == 3

def test_string_reversed_order(self):
    str_input = "Hello World and Coders"
    assert string_reversed_order(str_input) == "sredoC dna dlroW olleH"


