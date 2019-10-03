from typing import List, Dict, Union, Generator

# We will work with such dicts
ST = Dict[str, Union[str, int]]
# And we will put this dicts in list
DT = List[ST]


def task_1_fix_names_start_letter(data_list) -> DT:
    """
    Make all `names` field in list of students to start from upper letter

    Examples:
        fix_names_start_letters([{'name': 'Alex', 'age': 26}, {'name': 'denys', 'age': 89}])
        >>> [{'name': 'Alex', 'age': 26}, {'name': 'Denys', 'age': 89}]
    """
    for dict_in_data in data_list:
        for key, value in dict_in_data.items():
            if key == 'name' and value.istitle() is False: 
                    dict_in_data[key] = value.capitalize()
            else:
                continue
    return data_list

def task_2_remove_dict_fields(data, redundant_keys) -> DT:
    """given_data
    Remove from dictionaries given key value

    Examples:
       remove_dict_field([{'name': 'Alex', 'age': 26}, {'name': 'denys', 'age': 89}], 'age')
        >>> [{'name': 'Alex'}, {'name': 'denys'}]
    """
    for name in data:
        for key in redundant_keys:
            if key in name.keys():
                del name[key]
    return data


def task_3_find_item_via_value(data, value) -> DT:
    """
    Find and return all items that has @searching value in any key
    Examples:
        find_item_via_value([{'name': 'Alex', 'age': 26}, {'name': 'denys', 'age': 89}], 26)
        >>> [{'name': 'Alex', 'age': 26}]
    """
    sorting_data_list = []
    for students in data:
        if value in students.values():
            sorting_data_list.append([students])
    for value in sorting_data_list:
        return value


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
        data = [str(value) for value in data]
        value_min = data[0]
        for counter, value in enumerate(data):
            if len(value) < len(value_min):
                value_min = value
        return value_min


def task_6_min_value_list_of_dicts(data: DT, key: str) -> ST:
    """
    Find minimum value by given key
    Returns:
    """
    key_value_list = []
    for dict_value in data:
        if key in dict_value.keys():
            key_value_list += [dict_value.get(key)]
    for value in data:
        if min(key_value_list) in value.values():
            return value

def task_7_max_value_list_of_lists(data) -> int:
    """
    Find max value from list of lists
    """
    comparison_value = 0
    for data_element in data:
        for value in data_element:
            if value > comparison_value:
                comparison_value = value
    return comparison_value

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
    for character_in_str in text:
        sum_characters_positions += ord(character_in_str)
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
    for number in range(2, 200):
        if all(number % i != 0 for i in range(2, number)):
            yield number
