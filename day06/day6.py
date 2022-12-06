import sys 
from collections import Counter

file = sys.argv[1] 


def read_input(input_file):
    with open(input_file, 'rt') as f:
        s = f.read().rstrip()
        return s

def part_one():
    """
    The order of growth of number of steps is kn
    where k is the window size and n is the number of characters.

    In Python we don't need to worry about the slice end index being out of bounds.
    """
    s = read_input(file)
    print('input length', len(s))
    processed_chars = 0
    for i in range(len(s)):
        if len(set(s[i : i + 4])) == 4:
            processed_chars = i + 4
            break
        
    print(processed_chars)         


def part_two():
    s = read_input(file)
    processed_chars = 0
    for i in range(len(s)):
        if len(set(s[i : i + 14])) == 14:
            processed_chars = i + 14
            break
        
    print(processed_chars)         



if __name__ == '__main__':
    part_one()
    part_two()
