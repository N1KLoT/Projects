'''
Created on 21.09.2014

@author: Thomas
'''
import random

def merge_sort(list_to_sort):
    pass

def bubble_sort(list_to_sort):
    sorted_list = list_to_sort
    sorting = True
    while (sorting):
        sorting = False
        for i in range(0, len(list_to_sort)-1):
            if sorted_list[i] > sorted_list[i+1]:
                sorting = True
                tmp = sorted_list[i+1]
                sorted_list[i+1] = sorted_list[i]
                sorted_list[i] = tmp
    return sorted_list

def main():
    list_to_sort = random.sample(range(-100, 100), 10)
        
    print (str(bubble_sort(list_to_sort)))
#     merge_sort(list_to_sort)
#     print (str(list_to_sort))

if __name__ == '__main__':
    main()