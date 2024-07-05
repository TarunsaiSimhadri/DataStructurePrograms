"""

@Author: TarunSai
@Date: 2024-07-04
@Last Modified by: 
@Last Modified time:
@Title : Program to create a tuple.

"""

def create_tuple(tuple_of_numbers):

    """

    description:
        This function is used to create tuple.
    
    parameters:
        tuple_of_numbers(tuple)) : numbers in tuple we are printing.
        
    return:
        none

    """

    print(tuple_of_numbers)

def main():

    global tuple_of_numbers
    tuple_of_numbers = (1, 2, 3, 4)
    create_tuple(tuple_of_numbers)


if __name__ == "__main__":
    main()