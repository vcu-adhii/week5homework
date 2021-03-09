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
    incoming_list = [1, 2, 3, 4]
    total = sum(incoming_list)
    print("The sum is:",total)


def longest_value_key(incoming_dict):
    if incoming_dict is None:
        return None
    incoming_dict = {"dog": "cat", "a": "asdfasdfasdfasdfasdf"}
    longest_value_key = max(incoming_dict, key=len)
    print(longest_value_key)
