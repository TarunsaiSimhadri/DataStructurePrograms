"""

@Author: TarunSai
@Date: 2024-07-04
@Last Modified by: 
@Last Modified time:
@Title : Program to append a list to the second list.

"""


def append_list(Sample_list1, Sample_list2):

    """

    description:
        This function is used to append a list to the second list.
    
    parameters:
        Sample_list1, Sample_test2(list) : list of elements.
        
    return:
        none

    """
    Sample_list2.append(Sample_list1)
    print(Sample_list2)

def main():

    global Sample_list1, Sample_list2 
    Sample_list1 = ['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow']
    Sample_list2 = ['Red', 'Green', 'White', 'Pink']
    
    append_list(Sample_list1, Sample_list2)
    


if __name__ == "__main__":
    main()