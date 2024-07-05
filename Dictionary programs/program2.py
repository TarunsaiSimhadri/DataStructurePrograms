"""

@Author: TarunSai
@Date: 2024-07-03
@Last Modified by: Tarunsai
@Last Modified time: 
@Title : Program to add a key to dictionary.

"""


def add_key(my_dict):

    """

    description:
        This function is used to add a program to dictionary.
    
    parameters:
        dict(dictionary) : which we are perform adding operation.
        
    return:
        none

    """

    my_dict['key'] = eval(input("enter new key: "))
    print(my_dict)
    
def main():

    my_dict = eval(input("enter dictionary: "))
    add_key(my_dict)

if __name__ == "__main__":
    main()