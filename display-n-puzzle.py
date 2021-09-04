import itertools
import numpy as np
import math
import sys
from tabulate import tabulate


def get_quantity_combinations(list_combinations):
    return len(list_combinations)

def setup_list_combinations(n):
    my_list = list (range(1,n))
    my_list.append(' ')
    all_list = list(itertools.permutations(my_list))
    return all_list

def split_list(alist, wanted_parts):
    length = len(alist)
    return [ alist[i*length // wanted_parts: (i+1)*length // wanted_parts] 
             for i in range(wanted_parts) ]

def split_list_combinations(list_combinations, n_parts):
    new_list = []
    for item in list_combinations:
        new_list.append(split_list(item, n_parts))
    return new_list

def generate_tables (list_combinations):
    for item in list_combinations:
        # table = tabulate(item, tablefmt="fancy_grid")
        table = tabulate(item, tablefmt="grid")
        print(table)
        print('\n')

def n_puzzle(n, n_parts):
    list_combinations = setup_list_combinations(n)
    table = split_list_combinations(list_combinations, n_parts)
    generate_tables(table)
    print ("All States:",get_quantity_combinations(list_combinations))


def get_data():
    print('*** WELCOME to N PUZZLE ***')
    print('Insert the size of Puzzle: ')
    n = int(input()) + 1
    n_parts = math.isqrt(n)
    return n, n_parts


if __name__ == '__main__':
    n, n_parts = get_data()
    sys.stdout = open('N_Puzzle_Output.csv', 'w')
    n_puzzle(n, n_parts)
    sys.stdout.close()


# N = 15 -> 1 307 674 368 000
# N = 8 -> 362 880
# N = 3 -> 24
