"""

@Author: TarunSai
@Date: 2024-07-04
@Last Modified by: Tarunsai
@Last Modified time: 
@Title : program to count number of items in a dictionary value that is a list.

"""


def print_table(dictionary):

    """

    description:
        This function is used to print keys and values in a table.

    parameters:
        my_dict(dictionary) : dictionary that we are going to print the keys and values.
        
    return:
        none

    """

    print("+---------------------+-------------------------+")
    print("| Key                 | Value                   |")
    print("+---------------------+-------------------------+")

    for key, value in dictionary.items():
        print("| {:<19} | {:<23} |".format(key, str(value)))

    print("+---------------------+-------------------------+")

def main():
    my_dict = {
        "Name": "Alice",
        "Age": 30,
        "City": "Wonderland",
        "Occupation": "Adventurer"
    }

    print("Dictionary in Table Format:")
    print_table(my_dict)

if __name__ == "__main__":
    main()