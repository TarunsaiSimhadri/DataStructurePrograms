"""

@Author: TarunSai
@Date: 2024-07-04
@Last Modified by: 
@Last Modified time: 
@Title : Program to print min number of list.

"""


def min_number(numbers):

    """

    description:
        This function is used print min number of list.
    
    parameters:
        numbers(list) : list going to find the min number.
        
    return:
        none

    """
    numbers.sort()
    print(numbers[0])
    

def main():

    global numbers 
    numbers = [1, 3, 5, 83, 0]
    min_number(numbers)


if __name__ == "__main__":
    main()