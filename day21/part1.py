#!/usr/bin/python3
import sys
import re
from schemas import Expression, Monkey, Constant
import parser 

filename = './puzzle_input.txt' if len(sys.argv) < 2 else sys.argv[1]

monkey_to_job = parser.parse_file(filename)

operators = {
    '+': lambda a, b: a + b, 
    '-': lambda a, b: a - b,
    '/': lambda a, b: a // b,
    '*': lambda a, b: a * b
}

def make_tree(root): 
    """
    Construct tree from preorder traversal.
    The resulting tree will comprise only Expressions and Constants.
    """
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

def evaluate_expression(root, operators): 
    """
    Evaluate expression by using a postorder traversal
    that propogates intermediate results up to the tree root.

    Expects a tree as an argument that comprises Expressions and Constants only.
    """
    if isinstance(root, Expression): 
        right = evaluate_expression(root.right, operators)
        left = evaluate_expression(root.left, operators)
        return operators[root.op](left, right)
    
    if isinstance(root, Constant): 
        return root.value


def part_one():
    root_monkey = monkey_to_job['root']
    tree = make_tree(root_monkey)
    result = evaluate_expression(tree, operators)

    print('syntax tree\n', tree)
    print('Part One:', result)

if __name__ == '__main__': 
    part_one()