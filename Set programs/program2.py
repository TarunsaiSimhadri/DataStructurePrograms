"""

@Author: TarunSai
@Date: 2024-07-04
@Last Modified by: 
@Last Modified time: 
@Title : Program to iteration over sets.

"""

def iterate_set(numbers):

    """

    description:
        This function is used to iteration over sets.
    
    parameters:
        numbers(set) : numbers in set that are used for iteration
        
    return:
        none

    """

    for i in numbers:
        print(i)

def main():
    global numbers
    numbers = {1, 2, 3, 4, 5}
    iterate_set(numbers)


if __name__ == "__main__":
    main()