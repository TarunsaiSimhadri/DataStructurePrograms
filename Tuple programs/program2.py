"""

@Author: TarunSai
@Date: 2024-07-04
@Last Modified by: 
@Last Modified time:
@Title : Program to create a tuple with different data types.

"""

def create_tuple(tuple_of_items):

    """

    description:
        This function is used to create tuple with different data types.
    
    parameters:
        tuple_of_items(tuple) : items in tuple we are printing.
        
    return:
        none

    """

    print(tuple_of_items)

def main():

    global tuple_of_items
    tuple_of_items = (1, "tarun", (1, 2), 4, [1,3], {'tarun', (1,2)}, {'tarun': 21})
    create_tuple(tuple_of_items)


if __name__ == "__main__":
    main()