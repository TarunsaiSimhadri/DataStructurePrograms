"""

@Author: TarunSai
@Date: 2024-07-03
@Last Modified by: Tarunsai
@Last Modified time: 
@Title : program to count number of items in a dictionary value that is a list.

"""


def count_value_lists(my_dict):

    """

    description:
        This function is used to count number of items in a dictionary value that is a list.

    parameters:
        my_dict(dictionary) : dictionary that we are going to check how many lists are as values.
        
    return:
        none

    """

    count = 0
    for value in my_dict.values():
        if isinstance(value, list):
                count += 1 
    print("no.of lists as values in dictionary are", count)

def main():

    my_dict = eval(input("enter dictionary: "))
    count_value_lists(my_dict)

if __name__ == "__main__":
    main()