"""

@Author: TarunSai
@Date: 2024-07-04
@Last Modified by: 
@Last Modified time: 
@Title : Program to add numbers sets.

"""

def iterate_set(numbers):

    """

    description:
        This function is used to add numbers sets.
    
    parameters:
        numbers(set) : numbers in set that are used for iteration and adding to set.
        
    return:
        none

    """
    elements = set()

    for i in numbers:
        elements.add(i)

    print(elements)       

def main():
    global numbers
    numbers = [1, 2, 3, 4, 5]
    iterate_set(numbers)


if __name__ == "__main__":
    main()