"""

@Author: TarunSai
@Date: 2024-07-04
@Last Modified by: 
@Last Modified time: 
@Title : Program to clear set.

"""

def clear_set(numbers):

    """

    description:
        This function is used clear an set.
    
    parameters:
        numbers : set that is going to clear.
        
    return:
        none

    """
    numbers.clear()
    print(numbers)
          

def main():

    global numbers1 
    numbers = {1, 2, 3, 4, 5}
    clear_set(numbers)


if __name__ == "__main__":
    main()