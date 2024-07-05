"""

@Author: TarunSai
@Date: 2024-07-03
@Last Modified by: Tarunsai
@Last Modified time: 
@Title : program to check multiple keys exists in a dictionary.

"""


def key_exists(my_dict, keys):

    """

    description:
        This function is used to check multiple keys exists in a dictionary.

    parameters:
        my_dict(dictionary) : dictionary that we are going to check key is exsists or not.
        
    return:
        True(if key present), False(if key not present)

    """
    
    for key in keys:
        if key in my_dict:
                print(key, "key exists") 
        else:
             print(key, "key not exists")

def main():

    my_dict = eval(input("enter dictionary: "))
    global keys
    keys = eval(input("enter key: "))
    key_exists(my_dict, keys)

if __name__ == "__main__":
    main()