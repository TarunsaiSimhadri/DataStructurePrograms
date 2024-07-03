"""

@Author: TarunSai
@Date: 2024-07-02
@Last Modified by: Tarunsai
@Last Modified time: 
@Title : Program to print index positions along with elements.

"""


def access_elements(arr):

    """

    description:
        This function is used print index positions along with element of that position
    
    parameters:
        arr(array): which we are going to access the elements of array
        
    return:
        none

    """

    for i in range(len(arr)):
        print(i, arr[i])

def main():

    arr=[1, 20, 34, 77, 87]
    access_elements(arr)

if __name__ == "__main__":
    main()

    