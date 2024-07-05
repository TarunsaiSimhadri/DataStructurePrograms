"""

@Author: TarunSai
@Date: 2024-07-03
@Last Modified by: Tarunsai
@Last Modified time: 
@Title : Program to iterate dictionaries using loop.

"""


def iterate_dictionary(my_dict):

    """

    description:
        This function is used to iterate dictionaries.
    
    parameters:
        my_dict(dictionary) : which we are perform iteration.
        
    return:
        none

    """
    for key, value in my_dict.items():
        print(f'key: {key}, value: {value}' )
      
        

def main():

    my_dict = eval(input("enter a dictionary: "))
    iterate_dictionary(my_dict)

if __name__ == "__main__":
    main() 