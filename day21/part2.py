#!/usr/bin/python3
import sys
import re
from logger import log
import parser
from schemas import Expression, Monkey, Constant

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


def lookup_monkey(tree, monkey_to_job, monkey_name):
    """
    Determine if a given monkey exists in a tree.
    Assumes the tree comprises Expressions, Monkeys and Constants.
    """
    def lookup(tree): 
        if isinstance(tree, Expression): 
            found_left = lookup(tree.left)
            if found_left: 
                return 1
            found_right = lookup(tree.right)
            if found_right: 
                return 1
            return 0

        if isinstance(tree, Monkey): 
            if tree.name == monkey_name:
                return 1
            return lookup(monkey_to_job[tree.name])

        if isinstance(tree, Constant): 
            return 0

    return lookup(tree)



def compute_monkey_value(tree, target, operators, monkey_to_job, monkey_name):
    def inverse_op(op): 
        to_inverse = {
            '+': '-', 
            '-': '+', 
            '/': '*', 
            '*': '/'
        }
        return to_inverse[op] 
    def traverse(tree, target): 
        """Walk down tree and update the target until we reach our desired monkey"""
        if isinstance(tree, Constant): 
            return target
        if isinstance(tree, Monkey): 
            return traverse(monkey_to_job[tree.name], target)
        if isinstance(tree, Expression):
            found_left = lookup_monkey(tree.left, monkey_to_job, monkey_name) 
            if found_left:
                tree_right = make_tree(monkey_to_job[tree.right.name])
                operand = evaluate_expression(tree_right, operators)
                return traverse(tree.left, operators[inverse_op(tree.op)](target, operand))
            tree_left = make_tree(monkey_to_job[tree.left.name])
            operand = evaluate_expression(tree_left, operators)
            if tree.op == '/' or tree.op == '-': 
                return traverse(tree.right, operators[tree.op](operand, target))
            return traverse(tree.right, operators[inverse_op(tree.op)](target, operand))
    return traverse(tree, target)



def part_two():
    root_monkey = monkey_to_job['root']
    expr_left = monkey_to_job[root_monkey.left.name]
    expr_right = monkey_to_job[root_monkey.right.name]

    human = 'humn'
    left_side = lookup_monkey(expr_left, monkey_to_job, human)

    target = None 
    result = None 
    if left_side: 
        print('humn is on left side')
        target = evaluate_expression(make_tree(expr_right), operators)
        result = compute_monkey_value(expr_left, target, operators, monkey_to_job, human)
    else:
        print('humn is on right side')
        target = evaluate_expression(make_tree(expr_left), operators)
        result = compute_monkey_value(expr_right, target, operators, monkey_to_job, human)

    print('target', target)
    print('Part Two:', result)

if __name__ == '__main__':
    part_two()


