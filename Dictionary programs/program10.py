"""

@Author: TarunSai
@Date: 2024-07-03
@Last Modified by: Tarunsai
@Last Modified time: 
@Title : Program to count the values associated with key in a dictionary.

"""


def count_common_keys(sample_data):

    """

    description:
        This function is used to count the values associated with key in a dictionary.
    
    parameters:
        sample_data(list) : list of dictionaries.
        
    return:
        none

    """
    count = 0
    for i in sample_data:
        for value in i.values():
            if value == 'True':   
                count += 1 
    print(count)

def main():

    sample_data = [{'id': 1, 'success': 'True', 'name': 'Lary'}, 
                   {'id': 2, 'success':'False', 'name': 'Rabi'}, 
                   {'id': 3, 'success': 'True', 'name': 'Alex'}]
    count_common_keys(sample_data)

if __name__ == "__main__":
    main() 