"""Homework file for my students to have fun with some algorithms! """


def find_greatest_number(incoming_list):
    if incoming_list is None or len(incoming_list) == 0:
    return 0
    incoming_list = [1, 2, 3, 4, 5, 6, 7, 8]
    (max(incoming_list))
    pass


def find_least_number(incoming_list):
    if incoming_list is None or len(incoming_list) == 0:
    return 0
    incoming_list = [1, 2, 3, 4, 5, 6, 7, 8]
    (min(incoming_list))
    pass


def add_list_numbers(incoming_list):
    if incoming_list is None:
    return 0
    incoming_list = [1, 2, 3, 4]
    sum(incoming_list)
    pass


def longest_value_key(incoming_dict):
    if incoming_dict is None:
        return None
    current_longest_value = 0
    longest_value = ""
    for key, value in incoming_dict.items():
        if len(value) > current_longest_value:
            current_longest_value = len(value)
            longest_value = value
    for key, value in incoming_dict.items():
        if value == longest_value:
            return key
