"""

@Author: TarunSai
@Date: 2024-07-04
@Last Modified by: 
@Last Modified time:
@Title : Program to lowercase first n characters in a string.

"""


def modify_string(string, n):

    """

    description:
        This function is used to lowercase first n characters in a string.

    parameters:
        string(str) : string that going to modify
        
    return:
        none

    """

    modified_str = string[0:n+1:].lower() + string[n+1::]
    print(modified_str)
    
    

def main():

    global n, string
    string = input("enter a string: ")
    n = int(input("enter n value: "))
    modify_string(string, n)


if __name__ == "__main__":
    main()