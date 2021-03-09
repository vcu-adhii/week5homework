"""Homework file for my students to have fun with some algorithms! """


def find_greatest_number(incoming_list):
    if incoming_list is None or len(incoming_list) == 0:
        return 0
    incoming_list = [1, 2, 3, 4, 5, 6, 7, 8]
    (max(incoming_list))
    

def find_least_number(incoming_list):
    if incoming_list is None or len(incoming_list) == 0:
        return 0
    incoming_list = [1, 2, 3, 4, 5, 6, 7, 8]
    (min(incoming_list))


def add_list_numbers(incoming_list):
    if incoming_list is None:
        return 0
    incoming_list = [1, 2, 3, 4]
    sum(incoming_list)


def longest_value_key(incoming_dict):
    if incoming_dict is None:
        return None
    current_values_used = 0
    longest_key = ""
    for x, y in incoming_dict.values():
        if len(y) > current_values_used:
            current_values_used = len(y)
            longest_key = y
    for x, y in incoming_dict.values():
        if y == longest_key:
            return x
