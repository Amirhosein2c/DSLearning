import random 
from math import *
import time
import argparse


def parse_args():
    desc = ('A simple naive implementation of heap sort algorithm just for studying purpose. \ndefault value for the length of array is 1,000. if you want to try different lengths, please specify it with --length argument')
    parser = argparse.ArgumentParser(description=desc)
    parser.add_argument('--length', type=int, default=1000)
    args = parser.parse_args()
    return args

def swap(the_array, first, second):
    """Swap the two elements of index first and second in the array"""
    the_array[first] = the_array[first] + the_array[second]
    the_array[second] = the_array[first] - the_array[second]
    the_array[first] = the_array[first] - the_array[second]


def whos_bigger(the_array, left_idx, right_idx):
    """Check which child is bigger in the array, return the bigger child's index"""
    if the_array[left_idx] >= the_array[right_idx]:
        return left_idx
    else:
        return right_idx

    
def generate_array(length):
    """Generates a random integer array in range of 1 to length times 10"""
    A = []
    for i in range(length):
        A.append(random.randint(1,length*10))
    # print("Generated array: ", A)
    return A


def bigger_than(the_array, first, second):
    """ Checks if the first node is bigger in the array"""
    if the_array[first] >= the_array[second]:
        return True
    else:
        return False


def show_array(the_array):
    print("Array: ", the_array)


def heapify(main_list, list_length, parent_node_idx):
    """Heapify main module which is in fact a max heap"""
    # print("heapify method called with length of " + str(list_length) + " from parent node at index " + str(parent_node_idx))
    
    left_child_idx = floor(parent_node_idx * 2) + 1
    right_child_idx =  floor(parent_node_idx * 2) + 2
    
    if list_length > right_child_idx:
        has_right_child = True
    else:
        has_right_child = False

    if list_length > left_child_idx:
        has_left_child = True
    else:
        has_left_child = False

    if (not has_left_child) and (not has_right_child):
        # show_array(main_list)
        return

    if not has_right_child:
        if bigger_than(main_list, parent_node_idx, left_child_idx):
            pass
        else:
            swap(main_list, parent_node_idx, left_child_idx)
            # show_array(main_list)
            return
    else:
        bigger_child_idx = whos_bigger(main_list, left_child_idx, right_child_idx)
        if bigger_than(main_list, bigger_child_idx, parent_node_idx):
            swap(main_list, parent_node_idx, bigger_child_idx)
            heapify(main_list, list_length, bigger_child_idx)            
    # show_array(main_list)
    return


def heap_sort(main_list):

    sorted_list = []
    
    list_length = len(main_list)
    
    for i in range(floor(list_length/2) - 1, 0, -1):
        heapify(main_list, list_length, i)

    # print("############ END OF HEAPIFY METHOD #############")
    
    tail_idx = list_length - 1
    
    while tail_idx > 0:
        swap(main_list, tail_idx, 0)
        heapify(main_list, tail_idx, 0)
        tail_idx -= 1
        # show_array(main_list)

    return main_list


def main():
    
    args = parse_args()
    print("Array's length is: ", args.length)
    sorted_array = []
    unsorted_array = generate_array(args.length)
    tic = time.time()
    sorted_array = heap_sort(unsorted_array)
    toc = time.time()
    diff = toc - tic
    print("implemented heap sort: ", diff)
    
    # tic = time.time()
    # unsorted_array.sort()
    # toc = time.time()
    # diff = toc - tic
    # print("built-in sort: ", diff)


if __name__ == "__main__":
    main()
























        
    
