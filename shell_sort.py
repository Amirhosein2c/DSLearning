""" Simple code to learn how to implement Shell sort algorithm
    This code is written only for the purpose of learning, obviously it is 
    so naive in the sense of performance """

import random
import math
import argparse

def parse_args():
    """To be written"""
    return

    
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

        
def shell_sort(main_array):
    array_size = len(main_array)
    gap = math.floor(array_size/2.0)
    while gap >= 1:
        i = 0
        j = i + gap
        needs_swap = False
        while j < array_size:    
            needs_swap = compare(main_array, i, j)
            if needs_swap:
                swap(main_array, i, j)
                temp_i = i
                temp_j = j
                while True:
                    i = i - gap
                    j = j - gap
                    if i < 0:
                        break
                    else:
                        needs_swap = compare(main_array, i, j)
                        if needs_swap:
                            swap(main_array, i, j)
                        else:
                            pass
                i = temp_i
                j = temp_j
            i += 1
            j += 1
        gap = math.floor(gap/2.0)
    return main_array


def main():
    # length = args.length
    length = 20
    unsorted_array = generate_array(length)
    # unsorted_array = [79, 76, 45, 41, 32, 1, 5, 19, 2]
    length = len(unsorted_array)
    show_array(unsorted_array, "generated random array: ")
    unsorted_array = shell_sort(unsorted_array)
    show_array(unsorted_array, "sorted array: ")


if __name__ == "__main__":
    main()
