"""

@Author: TarunSai
@Date: 2024-07-04
@Last Modified by: 
@Last Modified time:
@Title : Program to slice a tuple.

"""

def create_tuple(tuple_of_items):

    """

    description:
        This function is used to slice a tuple.
    
    parameters:
        tuple_of_items(tuple) : items in tuple we are slicing in tuple.
        
    return:
        none

    """
    starting_index = int(input("enter starting index postion: "))
    ending_index = int(input("enter ending index postion: "))
    updation = int(input("enter updation value: "))
    print(tuple_of_items[starting_index:ending_index:updation])

def main():

    global tuple_of_items
    tuple_of_items = (1, "tarun", (1, 2), 4, [1,3], {'tarun', (1,2)}, {'tarun': 21})
    create_tuple(tuple_of_items)


if __name__ == "__main__":
    main()