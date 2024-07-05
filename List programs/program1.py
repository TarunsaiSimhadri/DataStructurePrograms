"""

@Author: TarunSai
@Date: 2024-07-04
@Last Modified by: 
@Last Modified time:
@Title : Program to print sum of all items in list.

"""


def sum_of_list(list_of_numbers):

    """

    description:
        This function is used to print sum of all items in list.
    
    parameters:
        list_of_numbers(list) : numbers in a set going to print in the function.
        
    return:
        none

    """

    summ = 0

    for i in list_of_numbers:
        summ+=i

    print(summ)

def main():

    global list_of_numbers
    list_of_numbers = [1, 2, 3, 4]
    sum_of_list(list_of_numbers)


if __name__ == "__main__":
    main()