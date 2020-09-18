""" Simple code to learn how to implement Shell sort algorithm
    This code is written only for the purpose of learning, obviously it is 
    so naive in the sense of performance """

import random
import math

def swap(the_array, first, second):
    the_array[first] = the_array[first] + the_array[second]
    the_array[second] = the_array[first] - the_array[second]
    the_array[first] = the_array[first] - the_array[second]

def generate_array(length):
    the_array = []
    for i in range(length):
        the_array.append(random.randint(0, length * 10))
    return the_array

def show_array(the_array, message):
    print(message, the_array)

def compare(the_array, first, second):
    if the_array[first] > the_array[second]:
        return True
    else:
        return False
        
def shell_sort(main_array)
    array_size = len(main_array)
    gap = math.floor(array_size/2)
    i = 0
    j = gap
    needs_swap = False
    
    while gap >= 1:    
        needs_swap = compare(main_array, i, j):
        if needs_swap:
            swap(main_array, i, j)
            
            if i - gap >= 0:
                
        
        
    return main_array

def main():

    length = args.length
    unsorted_array = generate_array(length)
    show_array(unsorted_array, "generated random array: ")
    unsorted_array = shell_sort(unsorted_array)
    show_array(unsorted_array, "sorted array: ")
