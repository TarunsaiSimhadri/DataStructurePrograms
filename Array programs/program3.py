"""

@Author: TarunSai
@Date: 2024-07-02
@Last Modified by: Tarunsai
@Last Modified time: 
@Title : Program to reverse an array.

"""    


def element_occurance(arr):

    """

    description:
        This function is used print the number of occurenace of the element.
    
    parameters:
        arr(array): which we are going to access the array and print the occurance of element.
        
    return:
        none

    """
    count = 0
    element = input("enter an element")
    for ele in arr:

        if ele == element:
            count += 1
    print(count)

def main():

    arr = eval(input("enter list of elements: "))
    element_occurance(arr)

if __name__ == "__main__":
    main()

