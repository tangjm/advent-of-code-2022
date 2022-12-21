#!/usr/bin/python3
import sys
import re
import math
from typing import *
from logger import log
from collections import deque
import helpers
from schemas import Expression, Monkey, Constant

filename = './puzzle_input.txt' if len(sys.argv) < 2 else sys.argv[1]


with open(filename, 'rt') as f:
    lines = f.read().rstrip().split('\n')
    split = list(map(lambda x:x.split(': '), lines))

    monkeys = [ monkey for monkey, job in split ]
    jobs = [ job for monkey, job in split]

    parsed_jobs = list(map(helpers.parse_job, jobs))

    zipped = list(zip(monkeys, parsed_jobs))
    log('zipped', zipped)

    monkey_to_job = dict(zipped) 
    log('mapping', monkey_to_job)


def make_tree(root): 
    """Construct tree from preorder traversal"""
    if isinstance(root, Expression):
        root.left = make_tree(root.left)
        root.right = make_tree(root.right)
        make_tree(root.left)
        make_tree(root.right)
    
    if isinstance(root, Monkey): 
        return monkey_to_job[root.name]

    if isinstance(root, Constant): 
        return root

    return root

operators = {
    '+': lambda a, b: a + b, 
    '-': lambda a, b: a - b,
    '/': lambda a, b: a // b,
    '*': lambda a, b: a * b
}

def evaluate_expression(root): 
    """
    Evaluate expression by using a postorder traversal
    that propogates intermediate results up to the tree root.
    """
    if isinstance(root, Expression): 
        right = evaluate_expression(root.right)
        left = evaluate_expression(root.left)
        return operators[root.op](left, right)
    
    if isinstance(root, Constant): 
        return root.value


def part_one():
    # Build our tree 
    root_monkey = monkey_to_job['root']
    print(root_monkey)

    tree = make_tree(root_monkey)
    result = evaluate_expression(tree)
    print(tree)
    print('Part One:', result)




    


if __name__ == '__main__':
    part_one()





