"""Homework file for my students to have fun with some algorithms! """


def find_greatest_number(incoming_list):
    if incoming_list is None or len(incoming_list) == 0:
        return 0
    return (max(incoming_list))
    pass


def find_least_number(incoming_list):
    if incoming_list is None or len(incoming_list) == 0:
        return 0
    return (min(incoming_list))
    pass


def add_list_numbers(incoming_list):
    total = 0
    incoming_list = [1, 2, 3, 4]
    for ele in range(0, len(incoming_list)):
        total = total + incoming_list[ele]
    print("Sum of all elements in given list: ", total)


def longest_value_key(incoming_dict):
    incoming_dict = {"dog": "cat", "a": "asdfasdfasdfhasdfasdf"}
    longest_value_key = max(incoming_dict, key=len)
    return longest_value_key
