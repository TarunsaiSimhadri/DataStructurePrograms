"""

@Author: TarunSai
@Date: 2024-07-03
@Last Modified by: Tarunsai
@Last Modified time: 
@Title : Program to create a remove a key from dictionary.

"""


def remove_key(my_dict):

    """

    description:
        This function is used to remove a key from dictionary.
    
    parameters:
        dict(dictionary): which we are going to remove a key.
        
    return:
        none

    """
    
    my_dict.pop(key)
    print(my_dict)

    
def main():

    my_dict = eval(input("enter a dictioanry: "))
    global key
    key = eval(input("enter a key: "))
    remove_key(my_dict)    

if __name__ == "__main__":
    main() 