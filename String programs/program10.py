"""

@Author: TarunSai
@Date: 2024-07-04
@Last Modified by: 
@Last Modified time:
@Title : Program to count occurrences of a substring in a string.

"""


def occurance_of_substring(string, substring):

    """

    description:
        This function is used to count occurrences of a substring in a string.
    
    parameters:
        string(str) : string counting he occurance of substring
        
    return:
        none

    """

    ocuurance = 0
    for i in string:
        if substring == i:
            ocuurance += 1
    print(ocuurance, "is the no.of times occured in the substring") 


def main():
    global string, substring
    string = input("enter a string: ")
    substring = input("enter a substring: ")
    occurance_of_substring(string, substring)


if __name__ == "__main__":
    main()