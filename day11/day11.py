#!/usr/bin/python3
import sys
import re
import pprint 
import functools 
import operator
from collections import Counter
from monkeyclass import Monkey
from parser import parse_input

printer = pprint.PrettyPrinter()

filename = './puzzle_input.txt' if len(sys.argv) < 2 else sys.argv[1]

def throw_to_monkey(monkeys, monkey_to, item):
  monkeys[monkey_to].receive_item(item) 

with open(filename, 'rt') as f:
  lines = f.read().rstrip().split('\n')


def part_one():
  monkeys = parse_input(lines)
  monkey_to_inspections = Counter()

  # Single round
  def start_rounds(rounds):
    for i in range(rounds):
      for monkey in monkeys:
        while monkey.items:
          # 1. Inspect item
          item = monkey.items.popleft()
          monkey_to_inspections[monkey] += 1

          # 2. Update worry level
          item = monkey.op(item)

          # 3. Apply 'monkey gets bored'
          item = monkey.apply_gets_bored(item)

          # 4. Run test
          if monkey.test(item):
            throw_to_monkey(monkeys, monkey.success_monkey, item)
          else:
            throw_to_monkey(monkeys, monkey.failure_monkey, item)
  start_rounds(20)
        
  two_most_active = monkey_to_inspections.most_common(2)
  active1, active2 = [ i for m, i in two_most_active ]
  monkey_business_level = active1 * active2 

  printer.pprint(monkey_to_inspections)
  print('Part One', monkey_business_level) 


def part_two():
  monkeys = parse_input(lines)

  # The product of primes is their lowest common multiple
  worry_level_upper_bound = 1
  for monkey in monkeys:
    worry_level_upper_bound *= monkey.test_val

  monkey_to_inspections = Counter()

  # Single round
  def start_rounds(rounds):
    for i in range(rounds):
      for monkey in monkeys:
        while monkey.items:
          # 1. Inspect item
          item = monkey.items.popleft()
          monkey_to_inspections[monkey] += 1

          # 2. Update worry level
          item = monkey.op(item)

          # 3. Apply 'monkey gets bored'
          # item = monkey.apply_gets_bored(item)

          # 3b. Apply upper bound to item worry levels
          item %= worry_level_upper_bound

          # 4. Run test
          if monkey.test(item):
            throw_to_monkey(monkeys, monkey.success_monkey, item)
          else:
            throw_to_monkey(monkeys, monkey.failure_monkey, item)

  start_rounds(10_000)
  two_most_active = [count for (m, count) in monkey_to_inspections.most_common(2) ]
  monkey_business_level = functools.reduce(operator.mul, two_most_active, 1)

  printer.pprint(monkey_to_inspections)
  print('Part Two:', monkey_business_level) 


part_one()
part_two()