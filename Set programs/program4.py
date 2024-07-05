"""

@Author: TarunSai
@Date: 2024-07-04
@Last Modified by: 
@Last Modified time: 
@Title : Program to remove elements sets.

"""

def iterate_set(numbers):

    """

    description:
        This function is used to remove elements sets.
    
    parameters:
        numbers(set) : numbers in set that are used for iteration and adding to set.
        
    return:
        none

    """

    numbers.remove(1)
    numbers.remove(2)

    print(numbers)       

def main():
    global numbers
    numbers = {1, 2, 3, 4, 5}
    iterate_set(numbers)


if __name__ == "__main__":
    main()