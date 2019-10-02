from typing import List, Dict, Union, Generator
import pytest

# We will work with such dicts
ST = Dict[str, Union[str, int]]
# And we will put this dicts in list
DT = List[ST]


def task_1_fix_names_start_letter(data) -> DT:
    """
    Make all `names` field in list of students to start from upper letter

    Examples:
        fix_names_start_letters([{'name': 'Alex', 'age': 26}, {'name': 'denys', 'age': 89}])
        >>> [{'name': 'Alex', 'age': 26}, {'name': 'Denys', 'age': 89}]
    """
    for i in data:
        for k, v in i.items():
            if k == 'name':
                if v.istitle() is False:
                    i[k] = v.capitalize()
            else:
                continue
    return data

def task_2_remove_dict_fields(data, redundant_keys) -> DT:
    """given_data
    Remove from dictionaries given key value

    Examples:
       remove_dict_field([{'name': 'Alex', 'age': 26}, {'name': 'denys', 'age': 89}], 'age')
        >>> [{'name': 'Alex'}, {'name': 'denys'}]
    """
    for name in data:
        for i in redundant_keys:
            if i in name.keys():
                del name[i]
    return data


def task_3_find_item_via_value(data, value) -> DT:
    """
    Find and return all items that has @searching value in any key
    Examples:
        find_item_via_value([{'name': 'Alex', 'age': 26}, {'name': 'denys', 'age': 89}], 26)
        >>> [{'name': 'Alex', 'age': 26}]
    """
    for students in data:
        if value in students.values():
            return [students]


def task_4_min_value_integers(data) -> int:
    """
    Find and return minimum value from list
    """
    if len(data) > 0:
        return min(data)

def task_5_min_value_strings(data) -> str:
    """
    Find the longest string
    """
    if len(data) > 0:
        stand = str(data[0])
        for i in range(1, len(data)):
            if len(str(data[i])) <= len(stand):
                stand = str(data[i])
        return str(stand)


def task_6_min_value_list_of_dicts(data: DT, key: str) -> ST:
    """
    Find minimum value by given key
    Returns:
    """
    key_value_list = []
    for i in data:
        if key in i.keys():
            key_value_list += [i[key]]
    for i in data:
        if i[key] == min(key_value_list):
            return i

def task_7_max_value_list_of_lists(data) -> int:
    """
    Find max value from list of lists
    """
    n = 0
    for i in data:
        for j in i:
            if j > n:
                n = j
    return n

def task_8_sum_of_ints(data) -> int:
    """
    Find sum of all items in given list
    """
    return sum(data)


def task_9_sum_characters_positions(text) -> int:
    """
    Please read first about ascii table.
    https://python-reference.readthedocs.io/en/latest/docs/str/ASCII.html
    You need to calculate sum of decimal value of each symbol in text

    Examples:
        task_9_sum_characters_positions("A")
        >>> 65
        task_9_sum_characters_positions("hello")
        >>> 532

    """
    sum_characters_positions = 0
    for i in text:
        sum_characters_positions += ord(i)
    return sum_characters_positions

def task_10_generator_of_simple_numbers() -> Generator[int, None, None]:
    """
    Return generator of simple numbers
    Stop then iteration if returned value is more than 200
    Examples:
        a = task_10_generator_of_simple_numbers()
        next(a)
        >>> 2
        next(a)
        >>> 3
    """
    n = 2
    yield n
    while True:
        n += 1
        k = 0
        for i in range(2, n + 1):
            if n % i == 0:
                k += 1
        if k == 1:
            yield n
