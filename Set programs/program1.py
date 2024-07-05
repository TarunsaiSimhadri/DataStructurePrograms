"""

@Author: TarunSai
@Date: 2024-07-04
@Last Modified by: 
@Last Modified time:
@Title : Program to create a set.

"""

def create_set(set_of_numbers):

    """

    description:
        This function is used to create set.
    
    parameters:
        set_of_numbers(set) : numbers in a set going to print in the function.
        
    return:
        none

    """

    print(set_of_numbers)

def main():

    global set_of_numbers
    set_of_numbers = {1, 2, 3, 4}
    create_set(set_of_numbers)


if __name__ == "__main__":
    main()