"""

@Author: TarunSai
@Date: 2024-07-04
@Last Modified by: 
@Last Modified time:
@Title : Program to check whether two lists are circularly identical.

"""


def are_circularly_identical(list1, list2):

    """

    description:
        This function is used to check whether two lists are circularly identical.

    parameters:
        list1, Sample_test2(list) : list of elements.
        
    return:
        none

    """

    if len(list1) != len(list2):
        return False
    
    concatenated = list1 + list1
    
    if list2 in concatenated:
        return True
    else:
        return False


def main():

    global list1, list2 
    list1 = [1, 2, 3, 4, 5]
    list2 = [3, 4, 5, 1, 2]

    print("List 1:", list1)
    print("List 2:", list2)

    if are_circularly_identical(list1, list2):
        print("Lists are circularly identical.")
    else:
        print("Lists are not circularly identical.")
 
    


if __name__ == "__main__":
    main()