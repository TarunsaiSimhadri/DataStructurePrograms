"""

@Author: TarunSai
@Date: 2024-07-02
@Last Modified by: Tarunsai
@Last Modified time: 
@Title : Program to reverse an array.

"""


def reverse_array(arr):
    
    """

    description:
        This function is used print reverse of an array.
    
    parameters:
        arr(array): which we are going to be reversed.
        
    return:
        none

    """
    arr.reverse()
    print(arr)
    # print(arr[::-1])

def main():

    arr = [1, 2, 3, 4, 5]
    reverse_array(arr)

if __name__ == "__main__":
    main()

