"""

@Author: TarunSai
@Date: 2024-07-04
@Last Modified by: 
@Last Modified time: 
@Title : Program to remove an item in set if it is present.

"""

def iterate_set(numbers):

    """

    description:
        This function is used remove an item in set if it is present.
    
    parameters:
        numbers(set) : numbers in set that are used for iteration and remove from the set.
        
    return:
        none

    """
    
    for i in numbers:
        if i == item:
            numbers.remove(item)
    print(numbers)
          

def main():

    global numbers, item
    item = int(input("enter a item: "))
    numbers = [1, 2, 3, 4, 5]
    iterate_set(numbers)


if __name__ == "__main__":
    main()