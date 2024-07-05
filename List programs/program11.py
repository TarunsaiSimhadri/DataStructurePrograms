"""

@Author: TarunSai
@Date: 2024-07-04
@Last Modified by: 
@Last Modified time:
@Title : Program to that takes two lists and returns True if they have atleast one common member.

"""


def generate_permutations(input_list):

    """

    description:
        This function is used to least one common member least one common member.
    
    parameters:
        Sample_list(list) : list of elements.
        
    return:
        none

    """
    
    from itertools import permutations

    perm = permutations(input_list)
    perm_list = list(perm)
    
    return perm_list

def main():

    input_list = [1, 2, 3]
    print("Input List:", input_list)
    print("Permutations:")
    for perm in generate_permutations(input_list):
        print(perm)

if __name__ == "__main__":
    main()




