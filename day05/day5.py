import sys 
import pprint
import operator
import re 

filename = sys.argv[1]
pp = pprint.PrettyPrinter()
pprint = pp.pprint

def accumulate(op, transform, initial, seq):
    if len(seq) == 0:
        return initial
    return op(transform(seq[0]), 
              accumulate(op, transform, initial, seq[1:]))

def accumulate_n(op, transform, init, seqs):
    # Size of first seq determines the number of rows
    if len(seqs[0]) == 0:
        return init 
    else: 
        return operator.concat(
                transform(accumulate(op, transform, init, [*map(lambda x:x[0], seqs)])),
                accumulate_n(op, transform, init, [*map(lambda x:x[1:], seqs)])
               )

def transpose_matrix(m):
    return accumulate_n(operator.concat, lambda x:[x], [], m)

def flip_vertically(m):
    return [*map(lambda y: list(reversed(y)), m)]
        
def rotate_clockwise_90(m):
    return flip_vertically(transpose_matrix(m))

def rotate_anticlockwise_90(m):
    return transpose_matrix(flip_vertically(m))

def remove_empty_strings(m):
    return [*map(lambda y: list(filter(lambda x:x.isalpha(), y)), m)]

def read_input(file):
    with open(file, 'rt') as f:
        data = f.read().split('\n\n')
    return data
        
def prepare_data(input_data):
    """
    Split input into two parts: a representation of the data; instructions for manipulating the data
    """
    data, instructions = input_data
    lines = data.split('\n')

    stacks = []
    for line in lines:
        current_stack = []
        for j in range(1, len(line), 4):
            current_stack.append(line[j])
        while len(current_stack) < 9:
            current_stack.append(' ')
        stacks.append(current_stack)
    print('stacks')
    pprint(stacks)
    print()

    rotated = rotate_clockwise_90(stacks[:-1])
    initial_stacks = remove_empty_strings(rotated)

    print('initial_stacks')
    pprint(initial_stacks)
    print()
    
    return initial_stacks, instructions

def part_one():
    initial_stacks, instructions = prepare_data(read_input(filename))
    pattern = '\D+(\d+)\D+(\d+)\D+(\d+)'
    instructions = instructions.split('\n')
    for instruction in instructions:
        result = re.search(pattern, instruction)
        count, src, dst = map(int, result.groups())
        while count > 0:
            removed = initial_stacks[src - 1].pop()
            initial_stacks[dst - 1].append(removed)
            count -= 1

    rearranged = initial_stacks
    final_stacks = rotate_anticlockwise_90(rearranged)
    answer = ''.join(final_stacks[0])

    # Logging
    print('rearranged')
    pprint(rearranged)
    print()

    print('answer')
    pprint(answer)

    return answer

def part_two():
    initial_stacks, instructions = prepare_data(read_input(filename))
    pattern = '\D+(\d+)\D+(\d+)\D+(\d+)'
    instructions = instructions.split('\n')
    for instruction in instructions:
        result = re.search(pattern, instruction)
        count, src, dst = map(int, result.groups())
        temp_stack = []
        while count > 0:
            removed = initial_stacks[src - 1].pop()
            temp_stack.append(removed)
            count -= 1
        while temp_stack:
            removed = temp_stack.pop()
            initial_stacks[dst - 1].append(removed)

    rearranged = initial_stacks
    final_stacks = rotate_anticlockwise_90(rearranged)
    answer = ''.join(final_stacks[0])

    # Logging
    print('rearranged')
    pprint(rearranged)
    print()

    print('answer')
    pprint(answer)

    return answer

if __name__ == '__main__':
    p1 = part_one()
    p2 = part_two()
    print('Part One:', p1)
    print('Part Two:', p2)

