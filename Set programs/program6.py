"""

@Author: TarunSai
@Date: 2024-07-04
@Last Modified by: 
@Last Modified time: 
@Title : Program to create an intersection of set.

"""

def iterate_set(numbers1, numbers2):

    """

    description:
        This function is used create an intersection of set.
    
    parameters:
        numbers1, numbers2(set) : sets that are going to print intersection elements.
        
    return:
        none

    """
    # numbers = set()
    # for i in numbers1:
    #     if i in numbers2:
    #         numbers.add(i)  
    # print(numbers) 
    print(numbers1.intersection(numbers2))       

def main():

    global numbers1, numbers2 
    numbers1 = {1, 2, 3, 4, 5}
    numbers2 = {2, 3, 4}
    iterate_set(numbers1, numbers2)


if __name__ == "__main__":
    main()