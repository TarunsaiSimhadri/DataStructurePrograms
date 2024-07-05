"""

@Author: TarunSai
@Date: 2024-07-03
@Last Modified by: Tarunsai
@Last Modified time: 
@Title : program to sort the dictionary according to the values.

"""


def nested_dictionary(keys_list, value):

    """

    description:
        This function is used to create nested dictioanary.

    parameters:
        key_list(list) : nested dictionary that we are going to create with this list.
        values (integer) : finally going to assign 
        
    return:
        None

    """

    nested_dict = {}
    current_dict = nested_dict

    for key in keys_list[:-1]:

        current_dict[key] = {}
        current_dict = current_dict[key]
    

    current_dict[keys_list[-1]] = value

    print(nested_dict)
    
def main():

    keys_list = eval(input("enter list of keys: "))
    value = int(input("enter value: "))
    nested_dictionary(keys_list, value)

if __name__ == "__main__":
    main()