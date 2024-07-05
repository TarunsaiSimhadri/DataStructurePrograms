"""

@Author: TarunSai
@Date: 2024-07-04
@Last Modified by: 
@Last Modified time: 
@Title : Program to print count of reversed strings in list.

"""


def no_of_reversed_strings(Sample_list):

    """

    description:
        This function is used print count of reversed strings in list.
    
    parameters:
        Sample_list(list) : list going to print count of reversed strings.
        
    return:
        none

    """

    count = 0

    for i in Sample_list:
        if len(i)>2:
            if i[::-1] == i:
                count+=1
    print(count)
    

def main():

    global Sample_list 
    Sample_list = ['abc', 'xyz', 'aba', '1221']
    no_of_reversed_strings(Sample_list)


if __name__ == "__main__":
    main()