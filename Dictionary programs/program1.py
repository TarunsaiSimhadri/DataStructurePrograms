"""

@Author: TarunSai
@Date: 2024-07-03
@Last Modified by: Tarunsai
@Last Modified time: 
@Title : program to sort the dictionary according to the values.

"""


def sort_dictionary(my_dict):

    """

    description:
        This function is used to sort the dictionary according to the values

    parameters:
        my_dict(dictionary) : dictionary that we are going to sort.
        
    return:
        ascending_sorted, descending_sorted

    """

    ascending_sorted = sorted(my_dict.items())
    print(ascending_sorted)
    
    descending_sorted = sorted(my_dict.items(), reverse = True)
    print(descending_sorted)


def main():

    my_dict = eval(input("enter dictionary: "))
    sort_dictionary(my_dict)

if __name__ == "__main__":
    main()