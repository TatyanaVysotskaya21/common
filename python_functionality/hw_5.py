import math
import string


def without_duplicates_list(a, b):
    return list(set(a) & set(b))

def number_letter_a_in_str(a_str, letter):
    return a_str.count(letter)

def power_of_three(number):
    return math.sqrt(number) == 3

def result_single_digit(number):
    while len(str(number)) > 1:
        sum_number = 0
        for i in list(str(number)):
            sum_number += int(i)
        number = sum_number
    return number

def zeros_to_the_end(new_list):
    return [i for i in new_list if i != 0] + [i for i in new_list if i == 0]

def arithmetic_progression(list_progression):
    for i in range(3, len(list_progression), 2):
        if (list_progression[i] - list_progression[i - 1]) != list_progression[1] - list_progression[0]:
            return False
    return True

def number_not_occur_twice(list_number):
    for i in list_number:
        if list_number.count(i) == 1:
            return i

def missing_list_number(list_number):
    new_list_number = [i for i in range(1, len(list_number) + 1)]
    return list(set(new_list_number) - set(list_number))[0]

def count_elements_until_tuple(list_number):
    n = 0
    for i in list_number:
        if isinstance(i, tuple):
            return n
        else:
            n += 1

def string_reversed_order(some_line):
    return " ".join([i[::-1] for i in some_line.split()[::-1]])

def number_hours_and_minutes(some_int_number):
    return str(some_int_number // 60) + ':' + str(some_int_number % 60)

def largest_word_in_string(some_line):
    return max(some_line.split())

def string_in_backwards_order(input_func):
    some_text = input_func()
    return " ".join([i for i in some_text.split()[::-1]])

def fib_numbers(n):
    if n == 0 or n == 1:
        return 1
    else:
        return fib_numbers(n - 1) + fib_numbers(n - 2)

def output_fib_numbers_to_generate(input_func):
    number_fib = input_func()
    return fib_numbers(number_fib)

def new_list_even_elements(some_list):
    return [i for i in some_list if i % 2 == 0]

def sum_input_number(input_func):
    some_number = input_func()
    sum_number = 0
    for y in [i for i in range(1, some_number + 1)]:
        sum_number += y
    return sum_number

def return_factorial_number(some_number):
    f_number = 1
    for y in [i for i in range(1, some_number + 1)]:
        f_number *= y
    return f_number

def alphabetical_shift_letters_in_line(some_text):
    new_text_list = [string.ascii_lowercase[string.ascii_lowercase.find(y) + 1] for y in some_text]
    for i in range(len(new_text_list)):
        if new_text_list[i] in 'aeiou':
            new_text_list[i] = new_text_list[i].upper()
    return ''.join(new_text_list)

def letters_row_in_alphabetical_order(some_text):
     return ''.join([i * some_text.count(i) for i in string.ascii_lowercase if i in list(some_text)])

def comparison_of_two_numbers(first_number, second_number):
    if first_number == second_number:
        return -1
    else:
        return first_number < second_number






