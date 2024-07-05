"""

@Author: TarunSai
@Date: 2024-07-04
@Last Modified by: 
@Last Modified time:
@Title : Program to print repeated elements a tuple.

"""

def repeated_items_tuple(tuple_of_numbers):

    """

    description:
        This function print repeated elements a tuple.
    
    parameters:
        tuple_of_numbers(tuple)) : tuple we are unpacking.
        
    return:
        none

    """

    list_of_numbers = []
    repeated = []
    for i in tuple_of_numbers:
        if i not in list_of_numbers:
            list_of_numbers.append(i)
        else:
            repeated.append(i)
    print(list_of_numbers)
    print(repeated)


def main():

    global tuple_of_numbers
    tuple_of_numbers = (1, 1, 2, 3, 4)
    repeated_items_tuple(tuple_of_numbers)


if __name__ == "__main__":
    main()