import re 
from monkeyclass import Monkey

pattern_monkey = r'(\d+)'
pattern_items = r'(\d+,|\d+)'
pattern_operation = r'new = old (.*)$'
pattern_test = r'divisible by (\d+)'
pattern_success = r'true: throw to monkey (\d+)'
pattern_failure = r'false: throw to monkey (\d+)'

def mult(x):
  if x == 'variable':
    return lambda y : y * y
  return lambda y : y * x

def add(x):
  return lambda y : y + x

op_table = {
  '*': mult,
  '+': add
}

def divides(x):
  return lambda y : y % x == 0

def parse_input(lines):
  monkeys = [] 
  for line in lines:
    if line.strip().startswith('Monkey'):
      res = re.search(pattern_monkey, line)
      num = int(res.group(1))
      monkeys.append(Monkey(num))

    if line.strip().startswith('Starting items'):
      items = list(map(int, re.findall(pattern_monkey, line)))
      monkeys[-1].set_items(items)

    if line.strip().startswith('Operation'):
      res = re.search(pattern_operation, line)
      op, operand = res.group(1).split(' ')
      if operand.isdigit():
        operand = int(operand)
      else: 
        operand = 'variable' 
      func = op_table[op](operand)
      monkeys[-1].set_op(func)
    
    if line.strip().startswith('Test'):
      res = re.search(pattern_test, line)
      x = int(res.group(1))
      monkeys[-1].set_test(divides(x))
      monkeys[-1].set_test_val(x)

    if line.strip().startswith('If true'):
      res = re.search(pattern_success, line)
      success_monkey = int(res.group(1))
      monkeys[-1].set_success_monkey(success_monkey)

    if line.strip().startswith('If false'):
      res = re.search(pattern_failure, line)
      failure_monkey = int(res.group(1))
      monkeys[-1].set_failure_monkey(failure_monkey)
  return monkeys