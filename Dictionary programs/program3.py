"""

@Author: TarunSai
@Date: 2024-07-03
@Last Modified by: Tarunsai
@Last Modified time: 
@Title : Program to concat dictionaries.

"""


def concat_dictionary():

    """

    description:
        This function is used to conacat dictionaries.
    
    parameters:
        dict(dictionary) : which we are perform concatination.
        
    return:
        none

    """

    dict1 = {1:10, 2:20}
    dict2 = {3:30, 4:40}
    dict3 = {5:50,6:60}

    dict1.update(dict2)
    dict1.update(dict3)
    
    print(dict1)

def main():
    concat_dictionary()

if __name__ == "__main__":
    main()