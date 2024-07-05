"""

@Author: TarunSai
@Date: 2024-07-03
@Last Modified by: Tarunsai
@Last Modified time: 
@Title : Program to print uncommon values in a dictionaries.

"""


def print_uncommon_values(my_list):

    """

    description:
        This function is used to print uncommon values in a dictionary.
    
    parameters:
        my_list(list): which we are going to perform opoeartion.
        
    return:
        none

    """
    
    un_common_values = set()
    for i in my_list:
        for value in i.values():
            # print(value)
            un_common_values.add(value)
    
    print(un_common_values)
   
def main():

    my_list = eval(input("enter a list: "))
    print_uncommon_values(my_list)

if __name__ == "__main__":
    main() 