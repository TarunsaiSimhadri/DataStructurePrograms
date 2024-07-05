"""

@Author: TarunSai
@Date: 2024-07-04
@Last Modified by: 
@Last Modified time:
@Title : Program to unpacking a tuple.

"""

def unpacking_tuple(tuple_of_numbers):

    """

    description:
        This function is used to unpacking a tuple.
    
    parameters:
        tuple_of_numbers(tuple)) : tuple we are unpacking.
        
    return:
        none

    """

    a, b, c, d = tuple_of_numbers
    print("a:", a)
    print("b:", b)
    print("c:", c)
    print("d:", d)


def main():

    global tuple_of_numbers
    tuple_of_numbers = (1, 2, 3, 4)
    unpacking_tuple(tuple_of_numbers)


if __name__ == "__main__":
    main()