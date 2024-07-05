"""

@Author: TarunSai
@Date: 2024-07-03
@Last Modified by: Tarunsai
@Last Modified time: 
@Title : Program to create a dictionary from a string.

"""


def string_elements_as_keys(inp_str):

    """

    description:
        This function is used to create a dictionary from a string.
    
    parameters:
        string(string) : for assiging keys.
        
    return:
        none

    """
    
    dict = {}.fromkeys(inp_str, 1)
    print(dict)    
      
        

def main():

    inp_str = input("enter a string: ")
    string_elements_as_keys(inp_str)

if __name__ == "__main__":
    main() 