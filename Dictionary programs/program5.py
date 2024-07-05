"""

@Author: TarunSai
@Date: 2024-07-03
@Last Modified by: Tarunsai
@Last Modified time: 
@Title : Program to generate and print dictionary.

"""


def generate_dictionary(n):

    """

    description:
        This function is used to generate and print dictionary..
    
    parameters:
        n(integer): which we are creating a dictionary with required numbers.
        
    return:
        none

    """
    
    my_dict = {}
    for i in range(1, n+1):
        my_dict.setdefault(i, i**2)
    print(my_dict)

def main():

    global n
    n = int(input("enter n value: ")) 
    generate_dictionary(n)  

if __name__ == "__main__":
    main() 