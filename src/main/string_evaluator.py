# Created by Leon Hunter at 3:57 PM 10/23/2020
class StringManipulator(object):
    def get_hello_world(self):
        return print("Hello World")

    def concatenate(self, value_to_be_added_to, value_to_add):
        # new_string = value_to_be_added_to + value_to_add
        return (str(value_to_be_added_to) + str(value_to_add))

    def substring_inclusive(self, string_to_fetch_from, starting_index, ending_index):

        return slice(string_to_fetch_from, starting_index,ending_index)

    def substring_exclusive(self, string_to_fetch_from, starting_index, ending_index):
        return slice(string_to_fetch_from, starting_index, ending_index)

    def compare(self, first_value, second_value):
        return None # TODO - Implement solution

    def get_middle_character(self, string_to_fetch_from):
        return None # TODO - Implement solution

    def get_first_word(self, string_to_fetch_from):
        return None # TODO - Implement solution

    def get_second_word(self, string_to_fetch_from):
        return None # TODO - Implement solution

    def reverse(self, string_to_be_reversed):
        return None # TODO - Implement solution